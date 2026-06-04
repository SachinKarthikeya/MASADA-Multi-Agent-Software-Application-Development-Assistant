from crewai import LLM

def llm_model():
    llm = LLM(
        model="ollama/llama3.2:1b",
        base_url="http://localhost:11434"
    )
    return llm 