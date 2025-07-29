"""
List: Find Max Min ( ** Interview Question)
Write a Python function that takes a list of integers as input and
returns a tuple containing the maximum and minimum values in the list.

The function should have the following signature:

def find_max_min(myList):

Where myList is the list of integers to search for
the maximum and minimum values.

The function should traverse the list and keep track
of the current maximum and minimum values.
It should then return these values as a tuple,
with the maximum value as the first element and
the minimum value as the second element.

For example, if the input list is [5, 3, 8, 1, 6, 9],
the function should return (9, 1) since 9
is the maximum value and 1 is the minimum value.
"""


def find_max_min(nums) -> tuple:
    max = nums[0]
    min = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > max:
            max = nums[i]

        if nums[i] < min:
            min = nums[i]

    return (max, min)


print(find_max_min([5, 3, 8, 1, 6, 9]))


"""
    EXPECTED OUTPUT:
    ----------------
    (9, 1)

"""
