import sys
import ai_models
from ai_models import configure_model, add_model, remove_model

def user_command_line_prompt():
    args = [x for x in sys.argv]
    prompt_by_user = args[1]
    entire_cmd_command = ' '.join(args[2:])
    all_input_flags = entire_cmd_command.split('--')
    all_input_flags = [x.strip() for x in all_input_flags]
    return prompt_by_user, all_input_flags  

def prompt_for_llm(prompt_by_user):
    # Modify the prompt and send it to the model
    prompt_by_user += " give response in such a way that is outputted on a command-line interface "
    r = ai_models.generate_output("gemini-1.5-flash", prompt_by_user)
    print()
    print(r)

prompt_by_user, all_input_flags = user_command_line_prompt()

prompt_for_llm(prompt_by_user)

if all_input_flags:
    if not all_input_flags[0] == '':
        print("Prompt should be quoted in double quotes, and the flags must be spaced out") 

    for flag in all_input_flags:
        if flag.startswith('config'):
            flags_list = flag.split(' ')
            configure_model(flags_list[1], flags_list[2])
            print(f"Configured model: {flags_list[1]} with API key: {flags_list[2]}")

        elif flag.startswith('add'):
            flags_list = flag.split(' ')
            add_model(flags_list[1], flags_list[2])
            print(f"Added model: {flags_list[1]} with API key: {flags_list[2]}")

        elif flag.startswith('remove'):
            flags_list = flag.split(' ')
            print("Removing model:", flags_list[1])
            remove_model(flags_list[1])

        elif flag == 'help':
            print("Usage: python3 main.py <prompt>")
            print("Example: python3 main.py 'How are you?'")
            print("Flags are: config <model_name> <api_key>, add <model_name> <api_key>, remove <model_name>")
            print()

    print("Updated models_api dictionary:", ai_models.models_api)  # Print to verify
