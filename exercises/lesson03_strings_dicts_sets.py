"""Lesson 3 exercises: fill in each TODO, then run:  pytest tests/test_lesson03.py -v

Rule: any built-in is allowed, except collections.Counter.
"""


def count_vowels(s):
    """Return how many vowels (a, e, i, o, u) are in s. Count upper and lower case.

    count_vowels("Hello World") -> 3
    Hint: loop over the characters. Is ch.lower() 'in' a string of vowels?
    """
    vowels = 'aeiou'
    count = 0
    for ch in s:
        if ch.lower() in vowels:
            count += 1
    return count
            

def reverse_words(sentence):
    """Return the sentence with the order of the words reversed.

    reverse_words("the quick fox") -> "fox quick the"
    Hint: split, reverse, join.
    """
    s = sentence.split()
    s = s[::-1]
    s = " ".join(s)
    return s

def is_palindrome(s):
    """Return True if s reads the same forwards and backwards, ignoring
    case and anything that isn't a letter or digit.

    is_palindrome("racecar") -> True
    is_palindrome("A man, a plan, a canal: Panama") -> True
    is_palindrome("hello") -> False
    Hint: first build a cleaned-up, lowercase string. Then compare it with its reverse.
    """
    string = s.lower()
    cleaned = ""
    for ch in string:
        if ch.isalnum():
            cleaned += ch
    return cleaned == cleaned[::-1]
        

def char_count(s):
    """Return a dict mapping each character in s to how many times it appears.

    char_count("banana") -> {"b": 1, "a": 3, "n": 2}
    Hint: the counting pattern from section 2.
    """
    counts = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    return counts


def is_anagram(s, t):
    """Return True if t uses exactly the same letters as s (same counts), else False.

    is_anagram("listen", "silent") -> True
    is_anagram("rat", "car") -> False
    Hint: you just wrote something that makes this easy. Two dicts can be compared with ==.
    """
    return char_count(s) == char_count(t)


def first_unique_char(s):
    """Return the INDEX of the first character that appears exactly once in s,
    or -1 if there isn't one.

    first_unique_char("leetcode") -> 0        ('l' appears once)
    first_unique_char("loveleetcode") -> 2    ('v')
    first_unique_char("aabb") -> -1
    Hint: count first. Then loop again, with positions, to find the first count of 1.
    """
    counted = char_count(s)
    for i in range(len(s)):
        if counted[s[i]] == 1:
            return i
    return -1


def contains_duplicate(nums):
    """Return True if any value appears more than once in nums.

    contains_duplicate([1, 2, 3, 1]) -> True
    contains_duplicate([1, 2, 3]) -> False
    Hint: keep a set of numbers you've already seen. Or: think about len() and set().
    """
    return len(nums) != len(set(nums))

def common_elements(a, b):
    """Return a SORTED list of the values that appear in both lists, without duplicates.

    common_elements([1, 2, 2, 3], [2, 3, 4]) -> [2, 3]
    Hint: section 3 of the lesson has a set operator for "in both".
    """
    new_list = list(set(a) & set(b))
    return sorted(new_list)



# Try your functions by hand:  python exercises/lesson03_strings_dicts_sets.py
if __name__ == "__main__":
    print(char_count("banana"))
    print(is_palindrome("A man, a plan, a canal: Panama"))
    print(first_unique_char("loveleetcode"))
