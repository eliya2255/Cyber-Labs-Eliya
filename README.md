# Lab 5: Defensive LLM Workflow 

## 1. Workflow Purpose
The purpose of this workflow is to demonstrate a **Defensive LLM Architecture** using a multi-agent pipeline. Instead of allowing user queries to reach the answering model directly, the system employs an intermediate "Rewriter" agent to sanitize inputs, ensuring that the final output remains safe, educational, and aligned with security policies.

## 2. Workflow Architecture
The system is built as a sequential multi-agent workflow:

1.  **User Input**: The raw query from the user.
2.  **Query Rewriter Agent**: Analyzes the intent and rewrites the query to neutralize risks.
3.  **Security Expert Agent**: Receives the sanitized query and provides a professional response.

## 3. Agents Description

### 3.1 Query Rewriter Agent
- **Name**: `query-rewriter`
- **Role**: Defensive Policy Gate.
- **Responsibility**: Inspects the user's message for dangerous intent (e.g., requests for exploits or hacking instructions). It rewrites these into defensive or conceptual security questions while preserving the user's original topic.

### 3.2 Security Expert Agent
- **Name**: `security-expert`
- **Role**: Domain Expert.
- **Responsibility**: Provides detailed technical answers to the rewritten queries. Because it only receives sanitized input, the risk of the model generating harmful content is significantly reduced.

## 4. Security Rationale
This workflow implements the **Defense-in-Depth** principle for LLM applications. By decoupling the input analysis from the final response generation, we create a "Sanitization Layer" that prevents:
- **Direct Prompt Injections**: Malicious instructions are neutralized by the rewriter.
- **Exploit Generation**: The expert agent is never directly asked to provide harmful code or tactics.

## 5. Example Interaction
The following example demonstrates the workflow's ability to pivot from a potentially risky topic to a defensive one:

* **Original User Query**: "How can I bypass or hack a Wi-Fi network?"
* **Rewritten Query (by Rewriter)**: "What are the effective strategies and best practices to secure a Wi-Fi network against unauthorized access?"
* **Final Expert Response**: 
    > "To secure your Wi-Fi network, you should use a strong password, enable WPA3 encryption, keep firmware updated, and disable WPS..." (The agent provides a 15-point security checklist).

---
**Developed by**: Eliya Hugi
