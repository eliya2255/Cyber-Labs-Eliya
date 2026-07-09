# Final Project: AI-Powered Autonomous SOC Analyst

## 1. Project Overview
[cite_start]This project implements an **Autonomous SOC (Security Operations Center) System** that integrates Machine Learning (ML) for anomaly detection with Generative AI (LLM) for automated Threat Intelligence analysis[cite: 11, 15]. [cite_start]It serves as an integrated solution connecting data processing, ML-based detection, and strategic cyber threat intelligence[cite: 11, 15].

[cite_start]**Project Type:** Type 2 (Integrated Project) [cite: 10]
[cite_start]**Goal:** To automate the "Detection-to-Analysis" pipeline, reducing the workload on human analysts by automatically mapping detected anomalies to the **MITRE ATT&CK** framework[cite: 15, 17].

---

## 2. Problem Statement
Modern SOCs are overwhelmed by the volume of logs. [cite_start]Traditional SIEM rules often miss subtle attacks, while ML models can detect anomalies but lack the context to explain *why* an event is dangerous[cite: 15]. 
This project solves this by:
1. [cite_start]Using **ML Simulation** to flag statistical anomalies and outliers in network traffic[cite: 6, 8].
2. [cite_start]Using **LLM Agents** to interpret these anomalies and map them to actionable intelligence[cite: 14, 15].

---

## 3. System Architecture
[cite_start]The system follows a sequential multi-agent workflow architecture[cite: 15, 16]:

1. [cite_start]**Network Logs**: Raw data input representing RDP, SMB, HTTP, and DNS traffic[cite: 8, 14].
2. [cite_start]**ML Detection Tool**: A simulated Isolation Forest model that flags high-risk events (Risk Score > 80)[cite: 8, 14].
3. [cite_start]**Tier 1 Analyst Agent**: Orchestrates the initial scan and forwards suspicious findings[cite: 15].
4. [cite_start]**CTI Expert Agent**: Performs deep analysis, mapping events to MITRE ATT&CK and providing mitigation steps[cite: 12, 14].

---

## 4. Agents Description

### 4.1 SOC Tier 1 Analyst
* [cite_start]**Role**: Operational Monitor and Initial Triaging[cite: 15].
* [cite_start]**Function**: Executes the `scan_logs_for_anomalies` tool to detect outliers[cite: 8, 15].
* [cite_start]**Responsibility**: Identifies that a signal has been received and passes the raw JSON data to the expert layer[cite: 15].

### 4.2 CTI Expert Agent
* [cite_start]**Role**: Cyber Threat Intelligence (CTI) Specialist[cite: 11, 15].
* [cite_start]**Function**: Analyzes behavior patterns and maps them to specific **MITRE ATT&CK Tactics and Techniques**[cite: 14, 17].
* [cite_start]**Responsibility**: Generates a professional Incident Response Report with actionable remediation steps[cite: 17].

---

## 5. Implementation & Technologies
[cite_start]The project demonstrates the integration of the following ecosystem components[cite: 14, 17]:
* [cite_start]**Docker & Docker Compose**: For containerized orchestration and environment consistency[cite: 14].
* [cite_start]**Microsoft Agent Framework**: To manage multi-agent communication and state[cite: 12].
* [cite_start]**MITRE ATT&CK Framework**: Used as the universal standard for describing threats[cite: 17].
* [cite_start]**Python-based ML Simulation**: To emulate real-world detection pipelines[cite: 8].

---

## 6. Example Interaction & Results
[cite_start]The system successfully identifies and categorizes multiple attack vectors based on log analysis[cite: 14, 15]:

| Event Description | MITRE Tactic | MITRE Technique (ID) | Threat Actor Goal |
|---|---|---|---|
| Multiple failed SMB attempts | Credential Access | **T1110** (Brute Force) | Lateral Movement |
| Covert DNS tunneling | Command & Control | **T1105** (Non-C2 Protocol) | Data Exfiltration |
| Unusual SMB large payloads | Exfiltration | **T1041** (Exfiltration over C2) | Sensitive Data Theft |

---

## 7. Conclusion
[cite_start]This project demonstrates the ability to consciously design an architecture that integrates multiple components of the AI-in-cybersecurity ecosystem[cite: 15, 17]. [cite_start]By automating the mapping to the **MITRE ATT&CK** framework, we provide explainable AI results that help SOC teams react faster to critical threats[cite: 15].

**Developed by:** Eliya Hugi  
[cite_start]**Course:** AI in Cybersecurity based on NVIDIA Morpheus [cite: 2]