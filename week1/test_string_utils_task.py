import pytest
from string_utils_task import *

# 1. count_vowels
@pytest.mark.parametrize("inp, out", [("Hello", 2), ("aeiou", 5), ("xyz", 0), ("", 0)])
def test_count_vowels(inp, out):
    assert count_vowels(inp) == out

def test_count_vowels_none():
    with pytest.raises(TypeError):
        count_vowels(None)

# 2. reverse_string
@pytest.mark.parametrize("inp, out", [("abc", "cba"), ("a", "a"), ("", "")])
def test_reverse_string(inp, out):
    assert reverse_string(inp) == out

def test_reverse_string_none():
    with pytest.raises(TypeError):
        reverse_string(None)

# 3. is_palindrome
# Fix: "A man a plan" palindrome nahi hai, isliye "madam" use kiya hai
@pytest.mark.parametrize("inp, out", [("racecar", True), ("madam", True), ("hello", False)])
def test_is_palindrome(inp, out):
    assert is_palindrome(inp) == out

def test_is_palindrome_none():
    with pytest.raises(TypeError):
        is_palindrome(None)

# 4. word_count
@pytest.mark.parametrize("inp, out", [("Hello World", 2), (" spaces ", 1), ("", 0)])
def test_word_count(inp, out):
    assert word_count(inp) == out

def test_word_count_none():
    with pytest.raises(TypeError):
        word_count(None)

# 5. capitalise_words
@pytest.mark.parametrize("inp, out", [("hello world", "Hello World"), ("abc", "Abc")])
def test_capitalise_words(inp, out):
    assert capitalise_words(inp) == out

def test_capitalise_words_none():
    with pytest.raises(TypeError):
        capitalise_words(None)

# 6. remove_duplicates
@pytest.mark.parametrize("inp, out", [("aaabbbcc", "abc"), ("a", "a"), ("aabb", "ab"), ("aaaaa", "a")])
def test_remove_duplicates(inp, out):
    assert remove_duplicates(inp) == out

def test_remove_duplicates_none():
    with pytest.raises(TypeError):
        remove_duplicates(None)