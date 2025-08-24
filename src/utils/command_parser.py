class CommandParser:
    def parse(argv):
        parsed_args = {}
        params = []
        option = "cmd_arg"

        for idx, arg in enumerate(argv):
            if CommandParser.__is_option(arg):
                if idx != 0:
                    parsed_args[option] = params
                    params = []
                option = arg
            else:
                params.append(arg)
        else:
            parsed_args[option] = params

        return parsed_args

    def __is_option(arg):
        return arg[0] == '-'

    def split(string):
        li = []
        word = ""
        idx = 0
        string = string.lstrip()
        
        while idx < len(string):
            char = string[idx]
            if char == '"' or char == '\'':
                idx_end = string.find(char, idx + 1)
                if idx_end == -1:
                    raise Exception("String not properly enclosed")
                li.append(string[idx + 1:idx_end])
                idx = idx_end + 1
            else:
                space = string.find(' ', idx + 1)
                if space == -1:
                    li.append(string[idx:])
                    break
                else:
                    li.append(string[idx:space])
                    idx = space
            idx += 1
        return li
