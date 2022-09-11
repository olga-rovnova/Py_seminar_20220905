#Задание 5. Реализуйте алгоритм перемешивания списка.

numbers = [11,22,33,44,55,66,77,88,99]
print(f'список:\n{numbers}')
items = list(range(0,len(numbers)))

numbers_mixed = []
while len(numbers_mixed) <= len(numbers):
    import random
    a = random.randint(0,(len(numbers)-1))
    if a in items:
        numbers_mixed.append(numbers[a])
        items.remove(a)
        if len(numbers_mixed) == len(numbers):  #строки 14, 15 - для выхода
            break                               #из бесконечного цикла
print(f'перемешанный список:\n{numbers_mixed}')