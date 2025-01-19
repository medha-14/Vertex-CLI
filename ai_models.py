import google.generativeai as genai


models_api = {
            "gemini-1.5-flash": "AIzaSyCWKme9gf6v_9aqQWCC7tUyYZxoqXVHIfQ",
              "gemini-1.5-interactive": None,
              "gpt-4o": None,
              "gemini-1.5-creative": None
              }


def api_key_model_selection(model_name):
    if model_name in models_api:
        return models_api[model_name]
    else:
        raise ValueError("Model is not available, please add it to the models_api dictionary")
    
    
def add_model(model_name, api_key):
    models_api[model_name] = api_key
    
    
def remove_model(model_name):
    if model_name in models_api:
        del models_api[model_name] 
    else:
        raise ValueError("Model is not available, please add it to the models_api dictionary")
    
    
def configure_model(model_name, api_key):
    models_api[model_name] = api_key
    
    
def generate_output(model_name , prompt_by_user):
    YOUR_API_KEY = api_key_model_selection(model_name)
                                                                                                                                            
    genai.configure(api_key=YOUR_API_KEY)
    model = genai.GenerativeModel(model_name)
    response = model.generate_content(prompt_by_user)
    return response.text

