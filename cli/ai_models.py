import json
import google.generativeai as genai

FILE_NAME = "models_api.json"


def load_models_api():
    try:
        with open(FILE_NAME, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("File not found")    
                
        
def update_models_api_json(updated_json_data):
    with open(FILE_NAME, 'w') as f:
        json.dump(updated_json_data, f, indent=4)

def api_key_model_selection(model_name):
    models_api_dict = load_models_api()
    if model_name in models_api_dict and models_api_dict[model_name]:
        return models_api_dict[model_name]
    else:
        raise ValueError(f"Model '{model_name}' is not available or has no API key. Please add it.")


def remove_model(model_name):
    models_api_dict = load_models_api()
    if model_name in models_api_dict:
        del models_api_dict[model_name]
        update_models_api_json(models_api_dict)
        print(f"Model '{model_name}' removed successfully.")
    else:
        raise ValueError(f"Model '{model_name}' is not found.")

def configure_model(model_name, api_key):
    models_api_dict = load_models_api()
    models_api_dict[model_name] = api_key
    update_models_api_json(models_api_dict)
    print("Model added successfully.")


def generate_output(model_name, prompt_by_user):
    # api_key = api_key_model_selection(model_name)
    api_key = "AIzaSyCWKme9gf6v_9aqQWCC7tUyYZxoqXVHIfQ"
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(model_name)
    response = model.generate_content(prompt_by_user)
    return response.text
