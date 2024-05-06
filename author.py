import colorama
from colorama import Back, Fore, Style
colorama.init
colorama.init(autoreset=True)

class Author:
    def __init__(self, name, bio):
        self.name = name
        self.bio = bio

    def get_info(self):
        return f"Name: {self.name.title()}, Bio: {self.bio.title()}"
