from app.agent import ask_healthcare_agent


def process_healthcare_query(query: str) -> str:
    return ask_healthcare_agent(query)
