from handlers.checkerHandler import checker

class censor:
    def __init__(self, check_ascii: bool, remove_zero_width_spaces: bool, words: list[str]):
        self.check_ascii = check_ascii
        self.remove_zero_width_spaces = remove_zero_width_spaces
        self.words = words


    def config(self):
        print(self.check_ascii, self.remove_zero_width_spaces, self.words)


