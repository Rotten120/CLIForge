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

        for idx, arg in enumerate(argv[1:]):
            if ArgParser.__is_option(arg):
                arg = ArgParser.__valid_eq(arg, len(params))
                parsed_args[option] = params
                params.clear()
                option = arg  
            else:
                params.append(arg)

            if option == "--":
                params = argv[idx + 1:]
                break

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
    def split(string: str) -> list[str]:
        string = string.strip()
        strlen = len(string)
        
        splitstr = []
        substr = ""

        idx = 0
        while idx < strlen:
            char = string[idx]

            if char in ['"', "'"]:
                strlit = ArgParser.get_strlit(string, char, idx)
                substr += strlit
                idx += len(strlit) + 1
            elif char != ' ':
                substr += char

            if char in [' ', '=']:
                ArgParser.noempty_append(splitstr, substr)
                substr = ""

            idx += 1
        splitstr.append(substr)
        return splitstr

    @staticmethod
    def noempty_append(splitstr, substr):
        if substr != "":
            splitstr.append(substr)

    @staticmethod
    def get_strlit(string: str, quote: chr, idx: int) -> str:
        strlit_end = string.find(quote, idx + 1)
        if strlit_end == -1:
            raise Exception("String not properly enclosed")
        return string[idx + 1:strlit_end]
