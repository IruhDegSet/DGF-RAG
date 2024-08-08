from langchain_community.embeddings import HuggingFaceInferenceAPIEmbeddings
import yaml
import sys
import os

# Ajoutez le répertoire parent au chemin de recherche des modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from indexing.embeddings import create_embeddings  # Correction de l'importation

# Fonction pour lire le fichier de configuration
def read_config(config_path):
    try:
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
        return config
    except Exception as e:
        print(f"Error reading config file: {e}")
        raise

# Fonction de test
def test_create_embeddings():
    try:
        config_path = os.path.join(os.path.dirname(__file__), '..', 'src', 'config', 'config.yaml')
        config = read_config(config_path)
        
        api_key = config['models']['embeddings']['api_key']
        model_name = config['models']['embeddings']['name']
        
        embeddings = create_embeddings(api_key, model_name)
        
        # Essayez d'obtenir la clé API en texte clair
        try:
            returned_api_key = embeddings.api_key.get_secret_value()  # Méthode potentielle
        except AttributeError:
            returned_api_key = str(embeddings.api_key)  # Si get_secret_value() n'existe pas

        print(f"Returned API Key: {returned_api_key}")
        print(f"Returned Model Name: {embeddings.model_name}")
        
        # Assertions pour vérifier les valeurs
        assert isinstance(embeddings, HuggingFaceInferenceAPIEmbeddings), "Failed to create HuggingFaceInferenceAPIEmbeddings instance"
        
        # Comparaison des valeurs
        assert returned_api_key.strip() == api_key.strip(), "API key does not match"
        assert embeddings.model_name.strip() == model_name.strip(), "Model name does not match"

        print("All tests passed.")
    
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Exécuter le test
if __name__ == "__main__":
    test_create_embeddings()
