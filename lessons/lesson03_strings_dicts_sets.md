# Lesson 3: Strings, Dicts & Sets

**Goal:** work with text, and learn the two tools that make interview answers fast: **dictionaries** and **sets**.
**Time:** about 2–2.5 hours.

In Lesson 2 you searched through lists with loops. This lesson shows how to look things up almost instantly instead. The **counting pattern** in section 2 is used in a huge number of interview problems.

---

## 0. Open a terminal

```bash
cd ~/algolab
source .venv/bin/activate
```

Try the examples below in the Python playground (type `python`).

## 1. Strings

A string is text. It works a lot like a list of characters.

```python
s = "hello"
len(s)        # 5
s[0]          # 'h'
s[-1]         # 'o'
s[1:4]        # 'ell'   (slicing works just like lists)
s[::-1]       # 'olleh' (a step of -1 reverses it)
"ell" in s    # True

for ch in s:  # loop over each character
    print(ch)
```

⚠️ **Strings can't be changed** ("immutable"). `s[0] = "H"` is an error. Instead you build a **new** string:

```python
s = "H" + s[1:]       # 'Hello'
```

### Useful string methods

Each of these returns a **new** string (or list). The original stays the same.

```python
"Hello".lower()             # 'hello'
"Hello".upper()             # 'HELLO'
"  hi  ".strip()            # 'hi'   (removes spaces at both ends)
"a-b-c".replace("-", "")    # 'abc'

"a".isalpha()               # True: is it a letter?
"7".isdigit()               # True: is it a digit?
"a".isalnum()               # True: is it a letter OR digit? (False for spaces, commas, "!")
```

### `split` and `join`: going between strings and lists

```python
"the quick fox".split()        # ['the', 'quick', 'fox']  (splits on spaces)
"a,b,c".split(",")             # ['a', 'b', 'c']

" ".join(["the", "quick"])     # 'the quick'
"".join(["a", "b", "c"])       # 'abc'
```

`join` looks backwards at first: the **separator** comes first, then `.join(list)`.

## 2. Dictionaries (dicts) ⭐

A **dict** stores **key → value** pairs. You look up a value by its key, the way you look up a word in a dictionary to find its meaning.

```python
ages = {"Ada": 36, "Grace": 85}

ages["Ada"]          # 36
ages["Linus"] = 54   # add a new key (or change an existing one)
"Ada" in ages        # True: checks the KEYS
ages["Bob"]          # KeyError! "Bob" isn't a key
ages.get("Bob")      # None: .get doesn't crash
ages.get("Bob", 0)   # 0: or give it a default value
len(ages)            # 3
```

Looping over a dict:

```python
for name in ages:                 # loops over the keys
    print(name, ages[name])

for name, age in ages.items():    # keys and values together
    print(name, age)
```

**Why dicts matter:** `x in some_list` has to check items one by one, so it's slow on a long list. `key in some_dict` goes straight to the answer, no matter how big the dict is. You'll learn how that works when you build your own hash map in Lesson 11.

### The counting pattern

This is how you count how many times each thing appears. You'll use it constantly.

```python
counts = {}
for ch in "banana":
    counts[ch] = counts.get(ch, 0) + 1

counts    # {'b': 1, 'a': 3, 'n': 2}
```

`counts.get(ch, 0)` means "the count so far, or 0 if we haven't seen this character yet". It's the accumulator pattern from Lesson 2, with one accumulator per key.

## 3. Sets

A **set** is a collection with **no duplicates** and no order. Like dict keys, checking `in` is instant.

```python
s = {1, 2, 3}
empty = set()            # NOT {}, which makes an empty dict!

s.add(4)                 # {1, 2, 3, 4}
s.add(2)                 # still {1, 2, 3, 4}: duplicates are ignored
3 in s                   # True, and fast

set([1, 2, 2, 3, 3])     # {1, 2, 3}: a quick way to remove duplicates
len(set(nums)) != len(nums)   # True if nums has any duplicates

a = {1, 2, 3}
b = {2, 3, 4}
a & b    # {2, 3}         in both ("intersection")
a | b    # {1, 2, 3, 4}   in either ("union")
a - b    # {1}            in a but not b
```

Sets have no order, so `s[0]` doesn't work. To get a sorted list, use `sorted(s)`.

## 4. Which one do I use?

| You need to… | Use |
|---|---|
| Keep items in order, allow repeats | **list** `[]` |
| Check "have I seen this before?" quickly | **set** `set()` |
| Remember something **about** each item (a count, an index, a name) | **dict** `{}` |

Interview tip: when your solution loops through a list inside another loop to *find* something, ask yourself "could a set or dict remember this for me instead?"

---

## ✏️ Your turn

Open `exercises/lesson03_strings_dicts_sets.py`. There are 8 functions to fill in.

**Rule for this lesson:** any built-in is allowed now, except `collections.Counter` (it does the counting pattern for you, and you should learn it by hand first).

```bash
pytest tests/test_lesson03.py -v
```

**Stuck?** Ask me for a hint on a specific function.

## 🎤 Interview corner

`is_anagram`, `first_unique_char` and `contains_duplicate` are real LeetCode problems (242, 387 and 217). All three are solved with the tools from this lesson:
- **Anagram:** do two words have the same character counts? Compare two counting dicts.
- **First unique character:** count first, then loop again to find the first character with a count of 1. "Loop once to gather information, loop again to use it" is a pattern worth remembering.
- **Contains duplicate:** a set of "seen" items.

When you explain them in an interview, say *why* you picked a dict or set: "checking `in` a set is instant, so I only go through the list once."
