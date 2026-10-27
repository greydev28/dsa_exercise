def find_number(numbers, target):
    for index, number in enumerate(numbers):
        if number == target:
               return index
    return -1
         
       
numbers = [10, 25, 30, 45]
target = 30

numbers2 = [5, 8, 5, 9]
target2 = 5

numbers3 = [10, 20, 30]
target3 = 99

print(find_number(numbers,target))
print(find_number(numbers2,target2))
print(find_number(numbers3,target3))
