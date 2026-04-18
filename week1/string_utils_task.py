def count_vowels(text: str) -> int:
    if text is None: raise TypeError("Input cannot be None")
    return sum(1 for char in text if char.lower() in 'aeiou')

def reverse_string(text: str) -> str:
    if text is None: raise TypeError("Input cannot be None")
    return text[::-1]

def is_palindrome(text: str) -> bool:
    if text is None: raise TypeError("Input cannot be None")
    clean = "".join(text.split()).lower()
    return clean == clean[::-1]

def word_count(text: str) -> int:
    if text is None: raise TypeError("Input cannot be None")
    return len(text.split())

def capitalise_words(text: str) -> str:
    if text is None: raise TypeError("Input cannot be None")
    return ' '.join(word.capitalize() for word in text.split())

def remove_duplicates(text: str) -> str:
    if text is None: raise TypeError("Input cannot be None")
    if not text: return ""
    result = [text[0]]
    for char in text[1:]:
        if char != result[-1]:
            result.append(char)
    return "".join(result)