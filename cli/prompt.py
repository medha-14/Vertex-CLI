import os
import sys
from cli.ai_models import (
    configure_model,
    remove_model,
    load_models_api,
    generate_output,
    create_json_file,
)
from cli.prettify_llm_output import prettify_llm_output
import cli.ai_models as ai_models


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

    if len(args) > 1 and not args[1].startswith("--"):
        prompt_by_user = args[1]
        entire_cmd_command = " ".join(args[2:])
    else:
        prompt_by_user = None
        entire_cmd_command = " ".join(args[1:])

    all_input_flags = entire_cmd_command.split("--")
    all_input_flags = [x.strip() for x in all_input_flags]

    return prompt_by_user, all_input_flags


def last_command_line_prompt(last_number_of_commands):
    """
    Retrieves the last N commands from the user's shell history.

    Args:
        last_number_of_commands (int): The number of recent commands to retrieve.

    Returns:
        str: A string containing the last N commands.
    """
    history_file = os.path.expanduser("~/.bash_history")
    with open(history_file, "r") as file:
        history_lines = file.readlines()
    last_commands = history_lines[-last_number_of_commands:]
    return "".join(last_commands)


def prompt_for_llm(prompt_for_llm):
    """
    Generates and displays the output from the language model based on the user's prompt.

    Args:
        prompt_for_llm (str): The prompt to send to the language model.
    """
    prompt_for_llm += " give response in short form, if asked for commands then give commands and dont explain too much"
    response = generate_output("gemini-1.5-flash", prompt_for_llm)
    prettify_llm_output(response)


def debug_last_command_line_prompt(prompt_by_user, all_input_flags):
    last_number_of_commands = (
        int(all_input_flags[2]) if len(all_input_flags) == 3 else 3
    )
    if prompt_by_user:
        prompt_by_vertex = (
            last_command_line_prompt(last_number_of_commands)
            + prompt_by_user
            + " basically output what is wrong with the commands used and suggest right ones"
        )
    else:
        prompt_by_vertex = (
            last_command_line_prompt(last_number_of_commands)
            + " output what is wrong with the commands used and suggest right ones, don’t explain about tex command"
        )
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


def handle_all_quries():
    """
    Handles all user queries from the command line prompt.

    This function performs the following steps:
    1. Retrieves the user command line prompt and input flags.
    2. If a prompt is provided by the user, it processes the prompt for the LLM.
    3. If no prompt is provided but the 'debug' flag is present, it triggers the debug function for the last command line prompt.
    4. Handles any additional input flags provided by the user.

    Returns:
        None
    """
    prompt_by_user, all_input_flags = user_command_line_prompt()
    if prompt_by_user:
        prompt_for_llm(prompt_by_user)
    elif len(all_input_flags) > 1 and all_input_flags[1] == "debug":
        debug_last_command_line_prompt(prompt_by_user, all_input_flags)
    handle_input_flags(all_input_flags)


def install_google_generativeai():
    import subprocess

    try:
        subprocess.run(
            ["pip", "install", "-U", "-q", "google-generativeai"], check=True
        )
        print("Successfully installed/updated google-generativeai.")
    except subprocess.CalledProcessError as e:
        print(f"Installation failed: {e}")


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--setup":
        create_json_file()
        install_google_generativeai()
    else:
        handle_all_quries()


if __name__ == "__main__":
    main()
