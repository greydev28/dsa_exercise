
def list_sum(numbers):
    total = 0
    if len(numbers) < 0:
        return None
    for number in numbers:
        total += number
    return total

numbers5 = [2, 4, 6, 8]
numbers6 = [-5, 10, -2]

print(list_sum(numbers5))
print(list_sum(numbers6))