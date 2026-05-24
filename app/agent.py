from langchain.agents import AgentExecutor, create_react_agent
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

from app.core.config import settings
from app.tools.lab_tools import analyze_lab_values
from app.tools.patient_tools import get_patient_record

TOOLS = [get_patient_record, analyze_lab_values]


prompt = PromptTemplate.from_template(
    """
You are a healthcare follow-up assistant.

You have access to the following tools:

{tools}

Use the following format:

Question: the input question you must answer

Thought: think about what to do

Action: the action to take, should be one of [{tool_names}]

Action Input: the input to the action

Observation: the result of the action

... (this Thought/Action/Observation can repeat)

Thought: I now know the final answer

Final Answer: the final answer to the original question

Question: {input}

Thought:{agent_scratchpad}
"""
)


def create_agent_executor():
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=settings.GEMINI_API_KEY,
        temperature=0.3,
    )

    agent = create_react_agent(llm=llm, tools=TOOLS, prompt=prompt)

    return AgentExecutor(
        agent=agent,
        tools=TOOLS,
        verbose=True,
        max_iterations=5,
        handle_parsing_errors=True,
    )


def ask_healthcare_agent(query: str) -> str:
    try:
        agent_executor = create_agent_executor()

        response = agent_executor.invoke({"input": query})

        return response["output"]

    except Exception as e:
        return f"Healthcare agent failed to process request: {str(e)}"
