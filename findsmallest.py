
def find_smallest(numbers):
    if len(numbers) <= 0:
        return None
    smallest_number = numbers[0]
    for number in numbers:
        if  number < smallest_number:
           smallest_number = number
    return smallest_number

numbers3 = [8, 3, 12, 1, 7]
numbers4 = [-3, -10, -1, -6]
print(find_smallest(numbers3))
print(find_smallest(numbers4))

