"""Lesson 2 exercises: fill in each TODO, then run:  pytest tests/test_lesson02.py -v

Rule: don't use sum(), max(), reversed(), .reverse(), [::-1] or set().
"""


def sum_list(nums):
    """Return the total of all numbers in the list.

    sum_list([1, 2, 3]) -> 6
    sum_list([]) -> 0
    Hint: the accumulator pattern. What should the total start at?
    """
    total = 0
    for n in nums:
        total += n
    return total

def count_evens(nums):
    """Return how many numbers in the list are even.

    count_evens([1, 2, 4, 7]) -> 2
    Hint: you wrote a way to check "even" in Lesson 1.
    """
    count = 0
    for n in nums:
        if n % 2 == 0:
            count += 1
    return count


def find_max(nums):
    """Return the largest number in the list, or None if the list is empty.

    find_max([3, 9, 2]) -> 9
    find_max([-5, -2, -8]) -> -2
    find_max([]) -> None
    Hint: like your max_of_three, with a loop. Careful: why is starting at 0 a bug?
    """
    if not nums:
        return None
    
    biggest = nums[0]
    for n in nums:
        if n > biggest:
            biggest = n
    return biggest

def reverse_list(nums):
    """Return a NEW list with the items in reverse order. Don't change the original.

    reverse_list([1, 2, 3]) -> [3, 2, 1]
    Hint: range() can count backwards. What is the index of the last item?
    """
    reverse = []
    for n in range(len(nums)-1, -1, -1):
        reverse.append(nums[n])
    return reverse


def count_down(n):
    """Use a while loop to return a list counting down from n to 1.

    count_down(3) -> [3, 2, 1]
    count_down(0) -> []
    """
    result = []
    while n > 0:
        result.append(n)
        n -= 1
    return result

def remove_duplicates(nums):
    """Return a new list with duplicates removed, keeping the first time each value appears.

    remove_duplicates([1, 2, 1, 3, 2]) -> [1, 2, 3]
    Hint: build a result list. Before adding an item, check whether it's already 'in' the result.
    """
    result = []
    for n in nums:
        if n not in result:
            result.append(n)
    return result


def two_sum(nums, target):
    """Interview classic! Return the indexes [i, j] (with i < j) of the two numbers
    that add up to target. Assume exactly one answer exists.

    two_sum([2, 7, 11, 15], 9) -> [0, 1]     because nums[0] + nums[1] == 9
    two_sum([3, 2, 4], 6) -> [1, 2]
    Hint: nested loops over every pair (see section 5 of the lesson). Don't pair an item with itself.
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]




# Try your functions by hand:  python exercises/lesson02_lists_loops.py
if __name__ == "__main__":
    print(sum_list([1, 2, 3]))
    print(reverse_list([1, 2, 3]))
    print(two_sum([2, 7, 11, 15], 9))
