


def input_flag():
    args = [ x for x in sys.argv]
    for arg in args:
        if arg == '-h' or arg == '--help':
            print('Usage: python3 main.py <prompt>')
            print('Example: python3 main.py "How are you?"')
            sys.exit(0)
        if arg == '-v' or arg == '--version':
            print('v1.0.0')
            sys.exit(0) 
        if arg.startswith('--'):
            arg = arg[2:]
            input_flag = arg 
    return input_flag

if input_flag() == 'config':
    prompt_by_user = ' '.join(args[1:])
    prompt_by_user += (" give response in bulllets points and with proper grammar in 5 line ")
    r = ai_models.generate_output("gemini-1.5-flash", prompt_by_user)
    print(r)