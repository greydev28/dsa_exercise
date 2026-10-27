def has_duplicates(numbers):
  set_numbers = set()
  for number in numbers:
        if number  in set_numbers:
            return True
        set_numbers.add(number)
  return False
        
      

numbers = [1, 2, 3, 2]
numbers2 = [1, 2, 3, 4]
numbers3 = []
print(has_duplicates(numbers))
print(has_duplicates(numbers2))
print(has_duplicates(numbers3))