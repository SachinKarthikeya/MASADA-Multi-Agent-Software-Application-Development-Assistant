from crewai import LLM

def llm_model():
    llm = LLM(
        model="ollama/gemma3:4b",
        base_url="http://localhost:11434"
    )
    return llm 
