import os
from agent_framework import ChatAgent, ai_function
from agent_framework.openai import OpenAIChatClient

@ai_function(
    name="check_password_strength",
    description="Analyzes a password and returns its length and if it is safe (8+ chars)."
)
def check_password(password: str) -> dict:
    is_safe = len(password) >= 8
    return {"length": len(password), "safe": is_safe}

base_url = os.getenv("API_BASE_URL")
api_key = os.getenv("API_KEY")
model_id = os.getenv("MODEL")
client = OpenAIChatClient(base_url=base_url, api_key=api_key, model_id=model_id)

agent = client.create_agent(
    name="Password Agent",
    instructions="You are a security assistant. Use the check_password_strength tool to help users evaluate their passwords.",
    tools=[check_password],
)