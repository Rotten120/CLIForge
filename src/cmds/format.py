from core.cliforge import CliForge

class Format:
    CASING = 0
    ITALIC = False
    STRONG = False
    SOURCE = None
    def execarg(parsed_args: dict[str, str]) -> None:
        optli = {
            "--upper": Format.__upper,
            "--lower": Format.__lower,
            "-i": Format.__italic,
            "-b": Format.__strong,
            "--source": Format.__source
        }
        
        for opt in parsed_args:
            if opt in optli:
                optli[opt](parsed_args[opt])
            elif opt != "cmd_arg":
                raise Exception("option not exist")

        Format.run(parsed_args["cmd_arg"])        

    def __upper(args: list[str]) -> None:
        Format.CASING = 1

    def __lower(args: list[str]) -> None:
        Format.CASING = -1

    def __italic(args: list[str]) -> None:
        Format.ITALIC = True

    def __strong(args: list[str]) -> None:
        Format.STRONG = True

    def __source(args: list[str]) -> None:
        if len(args) == 0:
            raise Exception("did not provided an string")
        Format.SOURCE = args[0]

    def run(cmd_args: list[str]) -> None:
        string = cmd_args[0]
        if Format.CASING == 1:
            string.upper()
        elif Format.CASING == -1:
            string.lower()

        if Format.ITALIC:
            string = "<i>" + string

        if Format.STRONG:
            string = "<b>" + string

        if Format.SOURCE != None:
            string = Format.SOURCE + ": " + string

        print(string)
            
            

        
