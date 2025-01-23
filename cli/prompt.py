#!/usr/bin/env python3

import subprocess
import os
import shutil
import sys
import ai_models
from ai_models import configure_model, remove_model, load_models_api
from prettify_llm_output import prettify_llm_output

def user_command_line_prompt():
    """
    Parses command-line arguments provided by the user.

    Returns:
        tuple: A tuple containing:
            - prompt_by_user (str or None): The user's prompt, if provided.
            - all_input_flags (list): A list of input flags provided by the user.
    """
    args = [x for x in sys.argv]
    load_models_api()

    # Check if the user provided a prompt
    if len(args) > 1 and not args[1].startswith("-"):
        prompt_by_user = args[1]
        entire_cmd_command = " ".join(args[2:])
    else:  # If the user did not provide a prompt
        prompt_by_user = None
        entire_cmd_command = " ".join(args[1:])

    all_input_flags = entire_cmd_command.split("--")
    all_input_flags = [x.strip() for x in all_input_flags]

    return prompt_by_user, all_input_flags

prompt_by_user, all_input_flags = user_command_line_prompt()

def last_command_line_prompt(last_number_of_commands):
    """
    Retrieves the last N commands from the user's shell history.

    Args:
        last_number_of_commands (int): The number of recent commands to retrieve.

    Returns:
        str: A string containing the last N commands.
    """
    history_file = os.path.expanduser('~/.bash_history')  

    with open(history_file, 'r') as file:
        history_lines = file.readlines()
    
    last_commands = history_lines[-last_number_of_commands:]

    return ''.join(last_commands)

def prompt_for_llm(prompt_for_llm):
    """
    Generates and displays the output from the language model based on the user's prompt.

    Args:
        prompt_for_llm (str): The prompt to send to the language model.
    """
    prompt_for_llm += " give response in such a way that is outputted on a command-line interface "

    response = ai_models.generate_output("gemini-1.5-flash", prompt_for_llm)
    prettify_llm_output(response)

def debug_last_command_line_prompt(prompt_by_user, all_input_flags):
    """
    Analyzes the last few shell commands to identify errors and suggests corrections.

    Args:
        prompt_by_user (str or None): The prompt provided by the user, if any.
        all_input_flags (list): A list of input flags provided by the user.
    """
    if len(all_input_flags) == 3:
        last_number_of_commands = int(all_input_flags[2])
    else:
        last_number_of_commands = 3

    if prompt_by_user:
        prompt_by_vertex = last_command_line_prompt(last_number_of_commands) + prompt_by_user + " basically output what is wrong with the commands used and suggest right ones"
    else:
        prompt_by_vertex = last_command_line_prompt(last_number_of_commands) + " output what is wrong with the commands used and suggest right ones, don’t explain about tex command"

    print("Prompt by vertex:", prompt_by_vertex)
    print()
    prompt_for_llm(prompt_by_vertex)

def handle_input_flags(all_input_flags):
    """
    Processes the input flags provided by the user and performs corresponding actions.

    Args:
        all_input_flags (list): A list of input flags provided by the user.
    """
    if all_input_flags:
        if not all_input_flags[0] == "":
            print("Prompt should be quoted in double quotes, and the flags must be spaced out")

        for flag in all_input_flags:
            if flag.startswith("config"):
                flags_list = flag.split(" ")
                configure_model(flags_list[1], flags_list[2])
                print(f"Configured model: {flags_list[1]} with API key: {flags_list[2]}")

            elif flag == "list":
                print("Listing all models:")
                ai_models.list_models()

            elif flag.startswith("remove"):
                flags_list = flag.split(" ")
                print("Removing model:", flags_list[1])
                remove_model(flags_list[1])

            elif flag == "help":
                print("Usage: python3 main.py <prompt>")
                print("Example: python3 main.py 'How are you?'")
                print("Flags are: --config <model_name> <api_key>, remove <model_name>")
                print()

def setup():
    """
    Sets up the script for easy execution by creating a symbolic link in /usr/local/bin as 'tex'.

    Ensures the script can be run directly using the 'tex' command.
    """
    from ai_models import create_json_file

    create_json_file()

    script_path = os.path.abspath(sys.argv[0])
    symlink_path = "/usr/local/bin/tex"
    try:
        os.chmod(script_path, 0o755)

        if os.path.islink(symlink_path) or os.path.exists(symlink_path):
            print(f"A symlink or file named 'tex' already exists at {symlink_path}.")
            return

        # Create the symbolic link
        subprocess.run(["sudo", "ln", "-s", script_path, symlink_path], check=True)
        print(f"Symbolic link created: {symlink_path} -> {script_path}")

    except PermissionError:
        print("Permission denied. Try running the script with 'sudo'.")
    except Exception as e:
        print(f"An error occurred: {e}")

if len(sys.argv) > 1 and sys.argv[1] == "--setup":
    setup()
else:
    # Outputs LLM output
    if prompt_by_user:
        prompt_for_llm(prompt_by_user)
    elif all_input_flags[1] == "debug":
        debug_last_command_line_prompt(prompt_by_user, all_input_flags)

    # Handle input flags
    handle_input_flags(all_input_flags)
