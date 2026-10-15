"""Lesson 1 exercises: fill in each TODO, then run:  pytest tests/test_lesson01.py -v"""


def greet(name):
    """Return a greeting for name.

    greet("Ada") -> "Hello, Ada!"
    Hint: an f-string.
    """
    return f"Hello, {name}!"


def is_even(n):
    """Return True if n is even, otherwise False.

    is_even(4) -> True
    is_even(7) -> False
    Hint: the % operator. Bonus: can you write it in one line?
    """
    return n % 2 == 0


def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit. Formula: F = C * 9/5 + 32

    celsius_to_fahrenheit(100) -> 212.0
    """
    return c * 9 / 5 + 32

def max_of_three(a, b, c):
    """Return the largest of three numbers WITHOUT using Python's built-in max().

    max_of_three(1, 9, 4) -> 9
    Hint: if/elif/else with 'and', or keep track of a "biggest so far" variable.
    """
    biggest = a
    if (b > biggest):
        biggest = b

    if (c > biggest):
        biggest = c
    
    return biggest

def letter_grade(score):
    """Return the letter grade for a score from 0 to 100.

    90 and above -> "A", 80-89 -> "B", 70-79 -> "C", 60-69 -> "D", below 60 -> "F"
    letter_grade(85) -> "B"
    """
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'
    


def fizzbuzz(n):
    """The classic interview question (single-number version).

    Return "FizzBuzz" if n is divisible by both 3 and 5,
           "Fizz"     if divisible by 3 only,
           "Buzz"     if divisible by 5 only,
           otherwise the number as a string, e.g. "7".
    Hint: str(7) turns the number 7 into the text "7".
    """
    if (n % 15 == 0 ):
        return f'FizzBuzz'
    elif (n % 3 == 0):
        return f'Fizz'
    elif (n % 5 == 0):
        return f'Buzz'
    else:
        return str(n)

# This block runs only when you run the file directly (python exercises/lesson01_basics.py).
# Use it to try your functions by hand.
if __name__ == "__main__":
    print(greet("Ada"))
    print(is_even(10))
    print(fizzbuzz(15))
