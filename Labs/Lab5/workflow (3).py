import os
from agent_framework import WorkflowBuilder
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    base_url=os.getenv("API_BASE_URL"),
    api_key=os.getenv("API_KEY"),
    model_id=os.getenv("MODEL")
)

rewriter_agent = client.create_agent(
    name="query-rewriter",
    instructions="""
        You are a security guard. Your task is to rewrite user queries to make them safe.
        If a user asks how to hack or perform an attack, rewrite the query to ask about 
        defensive measures or security principles instead.
        Keep the original intent but make it educational and safe.
    """
)

expert_agent = client.create_agent(
    name="security-expert",
    instructions="You are a cybersecurity expert. Provide clear and safe answers to the security questions you receive."
)

workflow = (
    WorkflowBuilder()
    .set_start_executor(rewriter_agent)
    .add_edge(rewriter_agent, expert_agent) 
    .build()
)


class WorkflowWrapper:
    def __init__(self, wf):
        self._workflow = wf
    
    async def run_stream(self, input_data=None, checkpoint_id=None, checkpoint_storage=None, **kwargs):
        """
        Wrapper to eliminate devUI error with checkpoint parameters
        """
        if checkpoint_id is not None:
            raise NotImplementedError("Checkpoint resume is not yet supported")
        
        async for event in self._workflow.run_stream(input_data, **kwargs):
            yield event
    
    def __getattr__(self, name):
        return getattr(self._workflow, name)

workflow = WorkflowWrapper(workflow)