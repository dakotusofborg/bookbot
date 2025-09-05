# stats.py

def count_words(text: str) -> int:
    """
    Counts the number of words in the provided text.
    """
    return len(text.split())


def count_characters(text: str) -> dict[str, int]:
    """
    Counts the number of times each character (letters, symbols, spaces, etc.)
    appears in the text. Characters are normalized to lowercase.
    Returns a dictionary {character: count}.
    """
    chars: dict[str, int] = {}
    for ch in text.lower():
        if ch in chars:
            chars[ch] += 1
        else:
            chars[ch] = 1
    return chars
 


