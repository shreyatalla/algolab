# Lesson 1: Python Basics

**Goal:** remember how to write and run small Python functions.
**Time:** about 1.5–2 hours.

---

## 0. Open a terminal in the project

In VS Code, go to **Terminal → New Terminal** and run:

```bash
cd ~/algolab
source .venv/bin/activate
```

`(.venv)` should now appear at the start of your prompt. It means you're using this project's own Python, which has the tools installed. **Run the `source` line each time you open a new terminal.**

## 1. The Python "playground" (REPL)

Type `python` and press Enter. You'll see `>>>`, which means Python is waiting for you to type a line of code. Try each line below:

```python
>>> 2 + 3
5
>>> print("hello")
hello
```

Type `exit()` to leave the playground. Use it anytime you want to test an idea quickly.

## 2. Variables and types

A **variable** is a name that points to a value.

```python
name = "Shreya"      # str: text, always in quotes
age = 25             # int: whole number
height = 5.4         # float: decimal number
is_student = False   # bool: True or False (capital T/F)

type(age)            # <class 'int'>
```

Math operators: `+  -  *  /` (this one always returns a float), `//` (whole-number division), `%` (remainder), `**` (power).

```python
7 / 2    # 3.5
7 // 2   # 3
7 % 2    # 1    <- remainder. "n % 2 == 0" is how you check whether n is even
2 ** 3   # 8
```

**f-strings** put variables inside text. Put an `f` before the quotes and the variables in `{}`:

```python
f"Hi {name}, you are {age}"   # 'Hi Shreya, you are 25'
```

## 3. Comparisons and if / elif / else

Comparisons give back `True` or `False`: `==` (equal), `!=` (not equal), `<  >  <=  >=`.
You can combine them with `and`, `or`, and `not`.

```python
temp = 72
if temp > 85:
    print("hot")
elif temp > 60:        # "else if": checked only if the line above was False
    print("nice")
else:
    print("cold")
```

⚠️ **Indentation matters in Python.** The 4 spaces tell Python which lines belong to the `if`. There are no `{ }` braces.

## 4. Functions

A **function** is reusable code with a name. It takes **parameters** (inputs) and uses `return` to send back a result (output).

```python
def add(a, b):
    return a + b

result = add(2, 3)   # result is 5
```

- `return` ends the function right away.
- If a function never reaches a `return`, it gives back `None` (Python's "nothing").
- **`print` is not `return`.** `print` only shows text on the screen. `return` hands the value back so the rest of your code can use it. The tests check what you *return*.

---

## ✏️ Your turn

Open `exercises/lesson01_basics.py` and fill in each function marked `# TODO`. Delete the `pass` line and write your code in its place.

Check your work:

```bash
pytest tests/test_lesson01.py -v
```

- **Red `FAILED`** means not yet done. Read the `assert` line in the output: it shows what your function returned next to what the test expected.
- **Green `PASSED`** means that function is done 🎉

You can also run the file directly to try your functions by hand:
`python exercises/lesson01_basics.py`

**Stuck?** Ask me: "I'm stuck on `max_of_three`, here's what I tried…". I'll give you a hint rather than the answer, unless you ask for the answer.

## 🎤 Interview corner

`fizzbuzz` is one of the most famous screening questions. It checks whether you can use `%` and whether you think about the **order** of your `if` checks. Once it passes, ask yourself: what goes wrong if you check `% 3` before `% 15`?
