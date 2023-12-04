from random import randint


count = int(input("Введите количество чисел"))
current_num = randint(1, 10)
max_num = current_num
min_num = current_num

for _ in range(count - 1):
    current_num = randint(1, 10)
    print(current_num, end=" ")
    max_num = max(max_num, current_num)
    min_num = min(min_num, current_num)
        

print()
print(min_num, max_num)