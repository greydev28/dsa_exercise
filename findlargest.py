def find_largest(numbers):
    if len(numbers) <= 0:
        return None
    largest_number = numbers[0]
    for number in numbers:
        if largest_number < number:
           largest_number = number
    return largest_number



numbers =[3, 41, 56, 21, 76, 9]
numbers2 = [-10, -5, -2, -18]


print(find_largest(numbers))
print(find_largest(numbers2))
print(find_largest([]))


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





