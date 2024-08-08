import sys
import os
import yaml
from typing import Dict, Any, Optional


# Ajoute le dossier src au chemin PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from src.retrieval.retriever import initialize_vectorstore
from src.indexing.embeddings import create_embeddings

def load_config()-> Optional[Dict[str, Any]]:
    config_path: str = os.path.join(os.path.dirname(__file__), '..', 'src', 'config', 'config.yaml')
    with open(config_path, 'r') as file:
        config: Dict[str, Any] = yaml.safe_load(file)
    return config

def test_retriever()-> None:
    # Charge la configuration
    config = load_config()
    
    if config is None:
        print("Impossible de charger la configuration.")
        return
    
    # Extrait les paramètres de configuration de Qdrant
    vector_db_config = config['storage']['vector_db']
    cloud_config = vector_db_config['cloud']
    
    # Extrait les paramètres de configuration et Initialise le modèle d'embeddings
    api_key = config['models']['embeddings']['api_key']
    model_name = config['models']['embeddings']['name'] 
    embeddings = create_embeddings(api_key, model_name)

    # Initialise le vector store avec les paramètres de configuration
    db = initialize_vectorstore(
        embeddings,
        cloud_config['url'],
        cloud_config['api_key'],
        cloud_config['collection_name']
    )
    
    # Vérifie si le vector store a été initialisé correctement
    if db is not None:
        try:
            collections = db.client.get_collections()
            collection_count = len(collections.collections)
            print(f"Nombre total de collections dans Qdrant: {collection_count}")
            print("Liste des collections:")
            for collection in collections.collections:
                print(f"- {collection.name}")
        except Exception as e:
            print(f"Erreur lors de la récupération des collections: {e}")
            
        # Tentative de récupération du nombre de vecteurs
        try:
            vector_count = db.client.count(collection_name=cloud_config['collection_name'])
            print(f"Number of vectors in the collection '{cloud_config['collection_name']}': {vector_count.count}")
        except Exception as e:
            print(f"Erreur lors de la récupération du nombre de vecteurs: {e}")

         # Tentative de récupération de la liste des collections

    else:
        print("Le vector store n'est pas initialisé.")

if __name__ == "__main__":
    test_retriever()