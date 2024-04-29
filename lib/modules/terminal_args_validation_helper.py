import validators

def terminal_args_validator(args: list[str]):
    if (args_count := len(args)) != 3:
        print(f"Two argument expected [URL and recursion depth limit (a positive integer)], got {args_count - 1}")
        raise SystemExit(2)
    elif not validators.url(args[1]):
        print("Argument 1 must be a valid URL")
        raise SystemExit(2)
    elif args_count < 3:
        print("You must specify the recursion depth limit")
        raise SystemExit(2)
    