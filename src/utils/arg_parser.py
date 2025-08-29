class ArgParser:
    @staticmethod
    def parse(argv: list[str]) -> dict[str, str]:
        parsed_args = {}
        params = []
        option = "--"            

        for idx, arg in enumerate(argv):
            if ArgParser.__is_option(arg):
                if idx != 0:
                    parsed_args[option] = params
                    params = []
                option = arg
            else:
                params.append(arg)

        parsed_args[option] = params
        return parsed_args

    @staticmethod
    def __update_parsed_args(parsed_args: dict[str, str], option: str, params: list[str]) -> None:
        if option in parsed_args:
            parsed_args[option] += params
        else:
            parsed_args[option] = params
        params = []

    @staticmethod
    def __is_option(arg: str) -> bool:
        return arg[0] == '-'

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

    #ignores empty strings
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
