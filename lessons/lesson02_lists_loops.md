# Lesson 2: Lists & Loops

**Goal:** store many values in one list, and use loops to go through them and build up results.
**Time:** about 2 hours.

Lists and loops come up in almost every interview problem. Many of the data structures you'll build later are lists underneath.

---

## 0. Open a terminal

```bash
cd ~/algolab
source .venv/bin/activate
```

Try the examples below in the Python playground (type `python`).

## 1. Lists

A **list** is an ordered collection of values in square brackets.

```python
nums = [4, 8, 15, 16]
empty = []
mixed = ["a", 2, True]    # allowed, but you'll usually keep one type per list

len(nums)        # 4, the number of items
```

### Indexing: getting one item

Positions start at **0**, not 1.

```python
nums = [4, 8, 15, 16]
#       0  1   2   3    <- positive index
#      -4 -3  -2  -1    <- negative index counts from the end

nums[0]     # 4   (first)
nums[3]     # 16
nums[-1]    # 16  (last, a very common shortcut)
nums[4]     # IndexError! There is no position 4
```

The last valid index is always `len(nums) - 1`. Going past the end is one of the most common bugs, called an "off-by-one" error.

### Slicing: getting a piece

`nums[start:stop]` gives a **new** list from `start` up to, but **not including**, `stop`.

```python
nums[1:3]    # [8, 15]
nums[:2]     # [4, 8]      (from the start)
nums[2:]     # [15, 16]    (to the end)
```

### Changing a list

```python
nums.append(23)      # add to the end    -> [4, 8, 15, 16, 23]
nums[0] = 99         # replace an item   -> [99, 8, 15, 16, 23]
nums.pop()           # remove and return the last item (23)
15 in nums           # True: checks whether a value is in the list
```

## 2. `for` loops

A `for` loop runs its indented block once for each item.

```python
for n in [4, 8, 15]:
    print(n)          # prints 4, then 8, then 15
```

### `range`: loop over numbers

```python
range(5)          # 0, 1, 2, 3, 4      (stops BEFORE 5)
range(2, 5)       # 2, 3, 4
range(10, 0, -2)  # 10, 8, 6, 4, 2     (the third number is the step)
```

When you need the **position** of each item, loop over `range(len(...))`:

```python
names = ["Ada", "Grace", "Linus"]
for i in range(len(names)):
    print(i, names[i])        # 0 Ada, 1 Grace, 2 Linus
```

`enumerate` gives you both at once, and reads more cleanly:

```python
for i, name in enumerate(names):
    print(i, name)
```

## 3. The accumulator pattern ⭐

This is the most important idea in this lesson. To compute something from a whole list:

1. **Before** the loop, create a variable to hold the answer so far.
2. **Inside** the loop, update it with each item.
3. **After** the loop (not indented), return it.

```python
def product(nums):
    result = 1            # 1. starting value
    for n in nums:
        result = result * n   # 2. update
    return result         # 3. return AFTER the loop
```

It works the same way for building a new list: start with `[]` and `append` inside the loop.

```python
def doubled(nums):
    result = []
    for n in nums:
        result.append(n * 2)
    return result

doubled([1, 2, 3])    # [2, 4, 6]
```

⚠️ **Watch the indentation of `return`.** If `return` is indented inside the loop, the function stops after the first item.

You already used a version of this in `max_of_three`, with your "biggest so far" variable. A loop lets the same idea work for a list of any length.

## 4. `while` loops

A `while` loop keeps going as long as its condition is `True`. Use it when you don't know in advance how many times to loop.

```python
n = 3
while n > 0:
    print(n)
    n = n - 1       # without this line the loop never ends!
print("liftoff")
```

If you get stuck in an endless loop, press **Ctrl + C** to stop it.

Two keywords work in both kinds of loop:
- `break` leaves the loop right away.
- `continue` skips to the next time round the loop.

## 5. Nested loops

You can put a loop inside a loop. This is how you compare **every pair** of items:

```python
nums = [1, 2, 3]
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):   # j starts after i, so no pair is repeated
        print(nums[i], nums[j])         # (1,2) (1,3) (2,3)
```

## 6. Bonus: list comprehensions

Python has a one-line shortcut for building a list:

```python
[n * 2 for n in nums]            # same as doubled(nums)
[n for n in nums if n > 5]       # keep only items greater than 5
```

Get comfortable with the full loop first. The one-line version is optional.

---

## ✏️ Your turn

Open `exercises/lesson02_lists_loops.py`. There are 7 functions to fill in.

**Rule for this lesson:** don't use the built-ins `sum()`, `max()`, `reversed()`, `.reverse()`, `[::-1]` or `set()`. Interviewers often ask you to write these yourself, and doing it is how you learn loops.

```bash
pytest tests/test_lesson02.py -v
```

**Stuck?** Ask me for a hint on a specific function.

## 🎤 Interview corner

`two_sum` is the **#1 most-asked** interview question (LeetCode problem 1). The nested-loop solution you'll write here is the "brute force" answer, and it's a perfectly good first answer in an interview. In Lesson 11 you'll solve it again with a hash map, and learn to explain why that version is much faster. That comparison is exactly the conversation interviewers want to have.
