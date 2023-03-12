from typing import Union 
from unidecode import unidecode


common_symbols = ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', '{', ']', '}', '\\', '|', ';', ':', "'", '"', ',', '<', '.', '>', '/', '?', " "]
less_common_symbols = [chr(169), chr(174), chr(8482), chr(8364), chr(163), chr(165), chr(8486), chr(9827), chr(9829), chr(9830)]

letter_changes = {
    "@": "a", 
    "!": "i",
    "$": "s",
    "0": "o"
}

letter_changed_list = ["@", "!", "$", "0"]


def _removeAccents(string: Union[str, list[str]]) -> str: 
    """Remove accents from string to prevent bypasses.

    Args:
        string (str): text that you want to remove accents from.

    Returns:
        str: returns text without accents.
    """
    new_words_arr = []

    if type(string) == list:
        for word in string:
            new_words_arr.append(unidecode(word))
        return new_words_arr
    else:
        return unidecode(string)
    

def removeSymbols(words: list[str]) -> list[str]:
    """Remove symbols from word list.
    
    Args:
        words (list[str]): list of words to remove symbols from.

    Returns:
        list (str): returns list of words without the symbols.
    """
    new_words_arr: list[str] = []
    
    for word in words:
        for letter in word:
            if letter in common_symbols or letter in less_common_symbols:
                word: str = word.replace(letter, '').lower()
                new_words_arr.append(word)

        else: 
            if word not in new_words_arr:
                new_words_arr.append(word)
    
    return new_words_arr


def lowerCase(words: list[str]) -> list[str]: 
    """Make all words in words list lowercase.

    Args:
        words (list[str]): list of words to make lowercase.

    Returns: 
        words (list[str]): list of words made lowercase.
    """
    new_word_list: list[str] = []

    for word in words:
        new_word_list.append(word.lower())

    return new_word_list


def letterSwitchChecker(text: str, words: list[str]) -> list[str]:
    """Check for words were symbols have been put there instead of letters.

    Args:
        text (str): text to be checked.
        words (list[str]): words to check the text for

    Returns:
        list[str]: returns a list of words that triggered the checker.
    """
    new_word_list: list[str] = []
    changed_text: str = ""

    words: list[str] = lowerCase(words)
    words: list[str] = _removeAccents(words)

    for letter in text:
        if letter in letter_changed_list:
            changed_to_char: str = letter_changes[letter]
            changed_text += changed_to_char
        else:
            changed_text += letter

    for word in words:
        if word in changed_text: 
            new_word_list.append(word)

    return new_word_list

    



def checker(text: str, remove_zero_width_spaces: Union[bool, None], remove_symbols: Union[bool, None], words: list[str]) -> list[str]:
    """Check for words that are in the words list.

    Args:
        text (str): text you want to check for words.
        remove_zero_width_spaces (bool, None): if zero width spaces are removed or not.
        words (list[str]): words to check the string for.

    Returns: 
        list (str): list of words that triggered the checker.
    """
    original_text = text
    matching_words: list[str] = []

    word_list: list[str] = _removeAccents(words)
    word_list: list[str] = lowerCase(word_list)

    if remove_symbols == True:
        word_list: list[str] = removeSymbols(word_list)

    text: str = text.lower()
    text: str = _removeAccents(text)

    if remove_zero_width_spaces == True or remove_zero_width_spaces == None: 
        text: str = (text.encode('ascii', 'ignore')).decode("utf-8")


    for letter in text:
        if letter in common_symbols or letter in less_common_symbols:
            text: str = text.replace(letter, '')

    for word in word_list:
        if word in text:
            matching_words.append(word)

    result = letterSwitchChecker(original_text, words)
    
    for result in result:
        matching_words.append(result)
    
    return matching_words