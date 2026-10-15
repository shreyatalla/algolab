from exercises.lesson01_basics import (
    celsius_to_fahrenheit,
    fizzbuzz,
    greet,
    is_even,
    letter_grade,
    max_of_three,
)


def test_greet():
    assert greet("Ada") == "Hello, Ada!"
    assert greet("Shreya") == "Hello, Shreya!"


def test_is_even():
    assert is_even(4) is True
    assert is_even(7) is False
    assert is_even(0) is True
    assert is_even(-2) is True


def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(100) == 212
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(-40) == -40


def test_max_of_three():
    assert max_of_three(1, 9, 4) == 9
    assert max_of_three(9, 1, 4) == 9
    assert max_of_three(1, 4, 9) == 9
    assert max_of_three(5, 5, 2) == 5
    assert max_of_three(-3, -1, -2) == -1


def test_letter_grade():
    assert letter_grade(95) == "A"
    assert letter_grade(90) == "A"
    assert letter_grade(89) == "B"
    assert letter_grade(75) == "C"
    assert letter_grade(60) == "D"
    assert letter_grade(59) == "F"


def test_fizzbuzz():
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(30) == "FizzBuzz"
    assert fizzbuzz(7) == "7"
