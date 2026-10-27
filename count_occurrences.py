def count_occurences(numbers, target):
    counter = 0 
    for number in numbers:
        if number == target:
            counter+=1
    return counter

numbers = [2, 5, 2, 8, 2]

target = 2

numbers2 = [1, 4, 7]

target2 = 10
print(count_occurences(numbers,target))
print(count_occurences(numbers2,target2))

