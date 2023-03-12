from typing import Union
from handlers.checkerHandler import checker

class censor:
    def __init__(self, check_ascii: Union[bool, None], remove_zero_width_spaces: Union[bool, None], words: list[str]):
        self.check_ascii = check_ascii
        self.remove_zero_width_spaces = remove_zero_width_spaces
        self.words_list = words

    def config(self) -> str:
        return {"check_ascii": self.check_ascii, "remove_zero_width_spaces": self.remove_zero_width_spaces, "words": self.words_list}
    
    def check(self, string: str) -> list[str]:
        return checker(string, self.check_ascii, self.remove_zero_width_spaces, self.words_list)


