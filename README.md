 Report — ybersecurity Pipeline
by: Eliya Hugi

Project Overview
In this laboratory, I constructed a simplified cybersecurity analysis pipeline based on event streaming and asynchronous processing. The system simulates a real-world SOC (Security Operations Center) workflow where security telemetry is ingested, classified against the MITRE ATT&CK framework, and analyzed for patterns.

Conceptual Questions and Answers
1. Why is Kafka used instead of direct function calls?
Kafka is used to ensure decoupling between pipeline stages. In a direct function call, if the processing stage fails or slows down, it immediately impacts the data source. By using Kafka as a message queue, the producer can continue to send events independently of the consumer's status, ensuring fault tolerance and asynchronous processing.

2. What happens if the consumer is slower than the producer?
If the consumer processes data slower than the producer generates it, a Lag is created. Kafka acts as a buffer, safely storing the messages in a queue until the consumer is ready to process them. This prevents data loss during high-load periods or spikes in security events.

3. How does tracing (using Jaeger) help debug pipeline behavior?
Tracing provides visibility into the entire lifecycle of an event. By using Jaeger, we can observe the end-to-end execution of the pipeline, measure latency per stage (e.g., how long the classification logic takes), and identify bottlenecks where data might be getting stuck.

4. Which pipeline stages could be scaled independently?
Thanks to the decoupling provided by Kafka, the Producer and Consumer stages can be scaled independently. If the volume of logs increases, we can add more consumer instances to handle the classification load without modifying the producer.

5. How would this pipeline change in a real SOC system?
In a production environment, the pipeline would be more complex:

Data Sources: Instead of a synthetic generator, data would come from real EDR agents, OS logs, and network forwarders.

Storage: Local CSV files would be replaced by distributed databases or SIEM platforms (like Splunk or Elasticsearch).

Logic: The classification would involve complex Machine Learning models and real-time correlation across multiple data sources.