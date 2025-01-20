#!/usr/bin/env python3

import sys
import ai_models
from ai_models import configure_model, remove_model, load_models_api
from prettify_llm_output import prettify_llm_output

def user_command_line_prompt():
    """
    Parses the command-line arguments provided by the user.

    Returns:
        tuple: A tuple containing the user's prompt (str) and a list of input flags (list).
    """
    args = [x for x in sys.argv]
    load_models_api()
    
    if len(args) > 1 and not args[1].startswith('-s'):
        prompt_by_user = args[1]
    else:
        prompt_by_user = None
    entire_cmd_command = ' '.join(args[2:])
        
    all_input_flags = entire_cmd_command.split('--')
    all_input_flags = [x.strip() for x in all_input_flags]
    return prompt_by_user, all_input_flags  

prompt_by_user, all_input_flags = user_command_line_prompt()

def prompt_for_llm(prompt_by_user):
    """
    Generates and prints the output from the language model based on the user's prompt.

    Args:
        prompt_by_user (str): The prompt provided by the user.
    """
    if prompt_by_user:
        prompt_by_user += " give response in such a way that is outputted on a command-line interface "
        
        r = ai_models.generate_output("gemini-1.5-flash", prompt_by_user)
        prettify_llm_output(r)

def handle_input_flags(all_input_flags):
    """
    Handles the input flags provided by the user.

    Args:
        all_input_flags (list): A list of input flags provided by the user.
    """
    if all_input_flags:
        if not all_input_flags[0] == '':
            print("Prompt should be quoted in double quotes, and the flags must be spaced out") 

        for flag in all_input_flags:
            if flag.startswith('config'):
                flags_list = flag.split(' ')
                configure_model(flags_list[1], flags_list[2])
                print(f"Configured model: {flags_list[1]} with API key: {flags_list[2]}")

            elif flag.startswith('remove'):
                flags_list = flag.split(' ')
                print("Removing model:", flags_list[1])
                remove_model(flags_list[1])

            elif flag == 'help':
                print("Usage: python3 main.py <prompt>")
                print("Example: python3 main.py 'How are you?'")
                print("Flags are: add <model_name> <api_key>, remove <model_name>")
                print()

# Outputs LLM output
prompt_for_llm(prompt_by_user)

# Handle input flags 
handle_input_flags(all_input_flags)