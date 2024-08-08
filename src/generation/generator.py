# src/generation/generate.py
#from config import load_config
from typing import Any, Dict
from langchain_groq import ChatGroq

def generate_llm(config: Dict[str, Any]) -> Any:
    """
    Initialize and return the LLM.

    Parameters:
    - config (dict): Configuration dictionary.

    Returns:
    - llm: The initialized LLM.
    """
    #config = load_config() 
    model_name = config['models']['llm']['name']
    groq_api_key =config['models']['llm']['api_key']
    temperature = 0
    
    llm = ChatGroq(model_name=model_name, groq_api_key=groq_api_key, temperature=temperature)
    return llm
