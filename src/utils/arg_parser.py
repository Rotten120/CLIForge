class ArgParser:    
    @staticmethod
    def parse(tokens: list[str]) -> dict[str, str]:
        args = {}
        params = []
        
        option = "--"
        in_equal = False

        def flush():
            nonlocal option
            nonlocal in_equal
            nonlocal params
            if in_equal:
                if len(params) != 1:
                    raise ValueError(f"Option expects 1 positional argument {len(params)} was given")
                in_equal = False
            args[option] = params
            option = token
            params = []

        for idx, token in enumerate(tokens):
            if token == '=':
                if in_equal:
                   raise TypeError(f"Only one '=' is possible each option")
                in_equal = True
                continue

            # checks if token is an option
            if token[0] == '-':
                flush()
            else:
                params.append(token)

            if token == "--":
                params = tokens[idx + 1:]
                break

        flush()
        return args

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
    
