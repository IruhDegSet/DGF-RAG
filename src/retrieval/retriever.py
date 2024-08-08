from langchain_community.embeddings import HuggingFaceInferenceAPIEmbeddings
from langchain_community.vectorstores import Qdrant
import qdrant_client

def initialize_vectorstore(
    embedding_function: HuggingFaceInferenceAPIEmbeddings,
    QDRANT_URL: str,
    QDRANT_API_KEY: str,
    collection_name: str
) -> Qdrant:
    """
    Initializes the Qdrant vector store.

    Args:
        embedding_function (HuggingFaceInferenceAPIEmbeddings): The embedding function to use.
        qdrant_url (str): The URL of the Qdrant server.
        qdrant_api_key (str): The API key for accessing Qdrant.
        collection_name (str): The name of the collection in Qdrant.

    Returns:
        Qdrant: An instance of the Qdrant vector store configured with the provided parameters.
    """
    qdrantClient = qdrant_client.QdrantClient(
        url=QDRANT_URL,
        prefer_grpc=True,
        api_key=QDRANT_API_KEY)

    return Qdrant(
        qdrantClient,
        collection_name,
        embedding_function
    )
