from langchain_community.embeddings import HuggingFaceInferenceAPIEmbeddings

def create_embeddings(api_key: str, model_name: str) -> HuggingFaceInferenceAPIEmbeddings:
    """
    Creates and returns an instance of HuggingFaceInferenceAPIEmbeddings.

    Args:
        api_key (str): The API token for accessing the Hugging Face Inference API.
        model_name (str): The model name to be used for generating embeddings.

    Returns:
        HuggingFaceInferenceAPIEmbeddings: An instance of the embeddings class configured with the specified API token and model name.
    """
    
    return HuggingFaceInferenceAPIEmbeddings(api_key=api_key, model_name=model_name)


