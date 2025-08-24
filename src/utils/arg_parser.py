class ArgParser:
    @staticmethod
    def parse(argv: list[str]) -> dict[str, str]:
        parsed_args = {}
        params = []
        option = "cmd_arg"

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
    def __is_option(arg: str) -> bool:
        return arg[0] == '-'

    @staticmethod
    def split(string: str) -> list[str]:
        string = string.strip()
        strlen = len(string)
        li = []
        
        space_idx = -1
        idx = 0
        
        while idx < strlen:
            char = string[idx]
            
            if char == '"' or char == "'":
                argstr = ArgParser.__get_argstr(string, char, idx)
                li.append(argstr[0])
                idx = argstr[1] + 1
                space_idx = idx
            elif char == ' ':
                if idx - space_idx != 1:
                    li.append(string[space_idx + 1:idx])
                space_idx = idx
                
            idx += 1
        li.append(string[space_idx + 1:])
        return li

    def __get_argstr(string: str, quote: chr, idx: int) -> str:
        idx_end = string.find(quote, idx + 1)
        if idx_end == -1:
            raise Exception("String not properly enclosed")
        return (string[idx + 1:idx_end], idx_end)
