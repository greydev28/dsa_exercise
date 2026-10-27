def move_zeros(numbers):
   zero_number = 0 
   for i in range(len(numbers)):
      if numbers[i] != 0:
         numbers[zero_number] = numbers[i]
         zero_number+=1
   for i in range(zero_number,len(numbers)):
      numbers[i] = 0
   return numbers

print(move_zeros([0, 1, 0, 3, 12]
))
print(move_zeros( [1, 2, 3]
))
print(move_zeros( [0, 0, 5]))
    

