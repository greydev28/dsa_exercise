def first_duplicate(numbers):
    seen =set()
    for item in  numbers:
        if item in seen:
            return item
        seen.add(item)
    return None

numbers =[4, 7, 2, 7, 5, 4]
numbers2 = [1, 2, 3, 4]

print(first_duplicate(numbers))
print(first_duplicate(numbers2))

