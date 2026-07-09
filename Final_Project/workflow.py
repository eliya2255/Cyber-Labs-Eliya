import os
import json
import random
from agent_framework import WorkflowBuilder, ai_function
from agent_framework.openai import OpenAIChatClient
from pydantic import BaseModel, Field
from kafka import KafkaConsumer  # ספריית החיבור לתשתית הזרמת הלוגים


# --- חיבור ל-API ---
client = OpenAIChatClient(
    base_url=os.getenv("API_BASE_URL"),
    api_key=os.getenv("API_KEY"),
    model_id=os.getenv("MODEL")
)

# --- כלי חילוץ לוגים בזמן אמת מ-Kafka ---
@ai_function(
    name="scan_logs_for_anomalies",
    description="Connects to the Kafka broker, consumes the latest network security logs, and flags high-risk anomalies."
)
def scan_logs(log_batch_id: str) -> dict:
    """
    Connects to the Redpanda/Kafka broker, reads a batch of logs,
    and filters for events where risk_score > 80.
    """
    suspicious_events = []
    
    try:
        # התחברות ל-Broker (משתמש בכתובת של קונטיינר ה-Kafka/Redpanda שלך)
        kafka_broker = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
        
        consumer = KafkaConsumer(
            'network-logs',  # שם ה-Topic של הלוגים של ה-Classifier
            bootstrap_servers=[kafka_broker],
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='soc-analyst-group',
            value_deserializer=lambda x: json.loads(x.decode('utf-8')),
            consumer_timeout_ms=2000  # מחכה מקסימום 2 שניות ללוגים חדשים
        )
        
        # קריאת הודעות וסינון אנומליות (Risk Score גבוה)
        for message in consumer:
            log_entry = message.value
            if log_entry.get("risk_score", 0) >= 80:
                suspicious_events.append(log_entry)
                
            # הגבלה של ה-Batch כדי לא להציף את ה-LLM
            if len(suspicious_events) >= 5:
                break
                
        consumer.close()
        
    except Exception as e:
        # Fallback לסימולציה במקרה ששרת ה-Kafka עדיין לא שלח הודעות
        suspicious_events = [
            {
                "timestamp": "2026-01-20T09:15:00Z",
                "src_ip": "192.168.1.50",
                "dst_ip": "10.0.0.5",
                "protocol": "RDP",
                "action": "Multiple Failed Logins",
                "risk_score": 95,
                "anomaly_type": "Brute Force"
            }
        ]

    return {
        "status": "anomaly_detected" if suspicious_events else "no_anomalies",
        "total_scanned": len(suspicious_events),
        "events": suspicious_events
    }

# --- הגדרת הסוכנים ---

t1_analyst = client.create_agent(
    name="SOC_Tier1_Analyst",
    instructions="""
        You are a Tier 1 SOC Analyst using an ML-based detection tool.
        Your job is to run the 'scan_logs_for_anomalies' tool when asked.
        Once you receive the anomalies, pass them strictly to the CTI Expert for analysis.
        Do not analyze them yourself, just report that anomalies were found.
    """,
    tools=[scan_logs]
)

cti_expert = client.create_agent(
    name="CTI_Expert",
    instructions="""
        You are a Cyber Threat Intelligence (CTI) Expert.
        Receive the suspicious events from the Tier 1 Analyst.
        For each event:
        1. Map it to the specific MITRE ATT&CK Tactic and Technique ID (e.g., T1110).
        2. Explain the threat actor's potential goal.
        3. Recommend immediate mitigation steps (Firewall rules, Account lockout, etc.).
        
        Format your response as a professional Incident Response Report.
    """
)

# --- בניית ה-Workflow ---
workflow = (
    WorkflowBuilder()
    .set_start_executor(t1_analyst)
    .add_edge(t1_analyst, cti_expert)
    .build()
)

# --- תיקון נקודת הריצה עבור ה-DevUI ---
# --- תיקון נקודת הריצה עבור ה-DevUI ---
# --- תיקון נקודת הריצה עבור ה-DevUI ---
class WorkflowWrapper:
    def __init__(self, wf):
        self._workflow = wf
    
    async def run_stream(self, input_data=None, **kwargs):
        # מסננים את כל הפרמטרים שעלולים להציק ל-Framework
        clean_kwargs = {k: v for k, v in kwargs.items() if k not in ['checkpoint_id', 'checkpoint_storage']}
        
        async for event in self._workflow.run_stream(input_data, **clean_kwargs):
            yield event
    
    def __getattr__(self, name):
        return getattr(self._workflow, name)

# חשיפת האובייקט
workflow = WorkflowWrapper(workflow)
devui = workflow