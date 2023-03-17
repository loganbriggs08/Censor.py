from typing import Union

from handlers.checkerHandler import checker
from handlers.censorHandler import censor as censor_handler

class censor:
    def __init__(self, remove_zero_width_spaces: Union[bool, None], remove_symbols: Union[bool, None],
                 words: list[str], change_character: str):
        self.remove_zero_width_spaces = remove_zero_width_spaces
        self.remove_symbols = remove_symbols
        self.words_list = words
        self.change_character = change_character

    def config(self) -> str:
        """Get your configuration for censorpy.

        Returns:
            dict: returns dict with configuration.
        """
        return {"remove_zero_width_spaces": self.remove_zero_width_spaces, "remove_symbols": self.remove_symbols,
                "words": self.words_list}

    def check(self, string: str) -> list[str]:
        """Check a string for words in your words list.

        Args:
            string (str): string that you would like to check.

        Returns:
            list (str): list of words that have triggered the checker.
        """
        return checker(string, self.remove_zero_width_spaces, self.remove_symbols, self.words_list)
    
    def censor(self, string: str) -> str:
        """Check a string for words in your wordlist and replace them with your custom char.

        Args:
            string (str): string that you would like to check and change.

        Returns:
            str: str with any changed words.
        """
        return censor_handler(string, self.remove_zero_width_spaces, self.remove_symbols, self.words_list, self.change_character)

