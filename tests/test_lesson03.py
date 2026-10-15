from exercises.lesson03_strings_dicts_sets import (
    char_count,
    common_elements,
    contains_duplicate,
    count_vowels,
    first_unique_char,
    is_anagram,
    is_palindrome,
    reverse_words,
)


def test_count_vowels():
    assert count_vowels("Hello World") == 3
    assert count_vowels("AEIOU") == 5
    assert count_vowels("rhythm") == 0
    assert count_vowels("") == 0


def test_reverse_words():
    assert reverse_words("the quick fox") == "fox quick the"
    assert reverse_words("hello") == "hello"
    assert reverse_words("a b") == "b a"


def test_is_palindrome():
    assert is_palindrome("racecar") is True
    assert is_palindrome("A man, a plan, a canal: Panama") is True
    assert is_palindrome("No lemon, no melon") is True
    assert is_palindrome("hello") is False
    assert is_palindrome("race a car") is False
    assert is_palindrome("") is True


def test_char_count():
    assert char_count("banana") == {"b": 1, "a": 3, "n": 2}
    assert char_count("aaa") == {"a": 3}
    assert char_count("") == {}


def test_is_anagram():
    assert is_anagram("listen", "silent") is True
    assert is_anagram("anagram", "nagaram") is True
    assert is_anagram("rat", "car") is False
    assert is_anagram("aab", "abb") is False
    assert is_anagram("ab", "abc") is False


def test_first_unique_char():
    assert first_unique_char("leetcode") == 0
    assert first_unique_char("loveleetcode") == 2
    assert first_unique_char("aabb") == -1
    assert first_unique_char("z") == 0
    assert first_unique_char("") == -1


def test_contains_duplicate():
    assert contains_duplicate([1, 2, 3, 1]) is True
    assert contains_duplicate([1, 2, 3]) is False
    assert contains_duplicate([7, 7]) is True
    assert contains_duplicate([]) is False


def test_common_elements():
    assert common_elements([1, 2, 2, 3], [2, 3, 4]) == [2, 3]
    assert common_elements([5, 1, 3], [3, 5, 9]) == [3, 5]
    assert common_elements([3, 10], [10, 3]) == [3, 10]
    assert common_elements([1, 2], [3, 4]) == []
    assert common_elements([], [1]) == []
