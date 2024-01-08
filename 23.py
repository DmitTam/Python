# Дан массив, состоящий из целых чисел. 
# Напишите программу, которая подсчитает количество элементов массива, 
# больших предыдущего (элемента с предыдущим номером) 

# Input: [0, -1, 5, 2, 3]

# Output: 2 

# Пояснение: (-1 < 5, 2 < 3)

array = [0, -1, 5, 2, 3]
count = 0

for i in range(len(array) - 1):
    if array[i] < array[i + 1]:
        count +=1
print(count)

print(sum([1 for i in range(len(array) - 1) if array[i] < array[i + 1]]))