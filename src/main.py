import fire  # ignore: import-error


class MinecraftServerAdminTools:
    """Minecraft Server Admin Tools
    A tool to manage minecraft server

    """

    def __init__(self):
        super().__init__()
        self.name = "Minecraft Server Admin Tools"
        self.version = "0.1.0"
        self.author = "Diego Rivera"
        self.about = ""
        self.commands = {}

    def translate(
        self,
        lang: str,
        to: str,
        file_name: str = "",
        text: str = "",
        output: str = "console",
    ) -> str:
        """Translate text from one language to another, or from a file.
        use google translate library.

        Args:
            langs (str): the language to translate from
            to (str): the language to translate to
            file_name (str, optional): the file name to translate. Defaults to "".
            text (str, optional): the text to translate. Defaults to "".
            output (str, optional): the output format. can be console or file. Defaults to "console".

        Raises:
            ValueError: either file_name or text must be provided
            ValueError: either file_name or text must be provided, not both

        Returns:
            str: the translated text
        """  # noqa: E501
        if file_name == "" and text == "":
            msg = "Either file_name or text must be provided"
            raise ValueError(msg)

        if file_name != "" and text != "":
            msg = "Either file_name or text must be provided, not both"
            raise ValueError(msg)

        return ""

    def help(self):
        """Show help message"""
        return ""


if __name__ == "__main__":
    fire.Fire(MinecraftServerAdminTools)
