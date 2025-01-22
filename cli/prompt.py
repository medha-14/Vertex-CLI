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
    Parses the command-line arguments provided by the user.

    Returns:
        tuple: A tuple containing the user's prompt (str) and a list of input flags (list).
    """
    args = [x for x in sys.argv]
    load_models_api()

    if len(args) > 1 and not args[1].startswith("-s"):
        prompt_by_user = args[1]
    else:
        prompt_by_user = None
    entire_cmd_command = " ".join(args[2:])

    all_input_flags = entire_cmd_command.split("--")
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
        if not all_input_flags[0] == "":
            print(
                "Prompt should be quoted in double quotes, and the flags must be spaced out"
            )

        for flag in all_input_flags:
            if flag.startswith("config"):
                flags_list = flag.split(" ")
                configure_model(flags_list[1], flags_list[2])
                print(
                    f"Configured model: {flags_list[1]} with API key: {flags_list[2]}"
                )

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
    Creates a symbolic link for this script in /usr/local/bin as 'tex'.
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
    prompt_for_llm(prompt_by_user)

    # Handle input flags
    handle_input_flags(all_input_flags)
