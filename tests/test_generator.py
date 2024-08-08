from langchain_groq import ChatGroq
import yaml
import sys
import os

# Add the parent directory to the module search path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

# Function to read the configuration file
def read_config(config_path):
    try:
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
        return config
    except Exception as e:
        print(f"Error reading config file: {e}")
        raise

# Test function
def test_generator():
    try:
        config_path = os.path.join(os.path.dirname(__file__), '..', 'src', 'config', 'config.yaml')
        config = read_config(config_path)
        
        model_name = config['models']['llm']['name']
        groq_api_key =config['models']['llm']['api_key']
        
        llm = ChatGroq(model=model_name, groq_api_key=groq_api_key, temperature=0)  # Creating ChatGroq instance with the API key
        
        print(f"Returned Model Name: {llm.model_name}")
        
        # Assertions to verify the values
        assert isinstance(llm, ChatGroq), "Failed to create ChatGroq instance"
        assert llm.model_name.strip() == model_name.strip(), "Model name does not match"
        print("All tests passed.")
    
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the test
if __name__ == "__main__":
    test_generator()
