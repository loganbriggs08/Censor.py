from typing import Union
from handlers.checkerHandler import checker

def censor(text: str, remove_zero_width_spaces: Union[bool, None], remove_symbols: Union[bool, None],
            words: list[str], change_character: str):
    """Add the custom char to strings that contain words in the word list.

    Args:
        -

    Returns:
        -
    """
    
    results: list[str] = checker(text, remove_zero_width_spaces, remove_symbols, words)
    new_text: str = ""
    
    for result in results: 
        result_length: int = len(result)
        char_position: int = 0
        

        for char in result: 
            char_position += 1

            if char_position != 1 and char_position != result_length:
                new_text += change_character
            elif char_position == result_length:
                new_text += char + " "
            else:
                new_text += char

    print(new_text)