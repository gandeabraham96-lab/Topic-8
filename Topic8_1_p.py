def find_max(numbers):
    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    return largest

from list_utils import find_max

numbers = [3, 9, 4, 1, 7]

print("Largest value:", find_max(numbers))