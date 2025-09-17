class ArgParser:    
    @staticmethod
    def parse(argv: list[str]) -> dict[str, str]:
        parsed_args = {}
        params = []
        option = "--"            

        if ArgParser.__is_option(argv[0]):
            option = argv[0]
        else:
            return {option: argv}

        if option == "--":
            return {option: argv[1:]}

        for idx, arg in enumerate(argv[1:]):
            if ArgParser.__is_option(arg):
                option = ArgParser.__valid_eq(option, len(params))
                parsed_args[option] = params
                params = []
                option = arg  
            else:
                params.append(arg)

            if option == "--":
                params = argv[idx + 1:]
                break

        option = ArgParser.__valid_eq(option, len(params))
        parsed_args[option] = params
        return parsed_args

    @staticmethod
    def __is_option(arg: str) -> bool:
        return arg[0] == '-'

    @staticmethod
    def __valid_eq(arg: str, paramlen: int) -> str:
        if arg[-1] == '=':
            arg = arg[:-1]
            if paramlen != 1:
                raise ValueError(f"Option expects 1 argument but {paramlen} was given")
        return arg

    @staticmethod
    def tokenize(string: str) -> list[str]:
        tokens = []
        temp_token = ""

        quote_sep = None
        in_token = False
        on_equal = False

        def flush():
            nonlocal temp_token
            if temp_token:
                tokens.append(temp_token)
                temp_token = ""
                return True
            return False
        
        for char in string:        
            if char in ["'", '"']:
                quote_set = {None: char, char: None}
                if quote_sep in quote_set:
                   quote_sep = quote_set[quote_sep]
                   continue

            if char == '=' and not on_equal:
                if flush():
                    tokens.append('=')
                    on_equal = True
                    continue

            in_token = not char.isspace() or (quote_sep != None)
            if in_token:
                temp_token += char
            elif flush():
                on_equal = False
                
        if quote_sep != None:
            error_msg = f"Unclosed quote ({quote_sep})"
            raise ValueError(error_msg)
        flush()
        return tokens
    
