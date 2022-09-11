# Задание 6/ Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.
# Пример:     Для "abababb" и "aba" -> 2

a = 'abababb'
b = 'aba'
count = 0

for i in range (0,len(a)-len(b)+1):
    element = (a[i:i+len(b)])
    print(element)
    i = 1
    if element == b:
        count += 1

print(f'количество вхождений = {count}')

