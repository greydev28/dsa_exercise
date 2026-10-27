def count_even(numbers):
    counter = 0
    for number in numbers:
        if number % 2 == 0:
            counter+=1     
    return counter


numbers7 = [1, 2, 3, 4, 6]
numbers8 = [1, 3, 5, 7]

print(count_even(numbers7))
print(count_even(numbers8))