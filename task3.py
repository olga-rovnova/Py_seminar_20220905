# Задание 3. Задайте список из n чисел последовательности (1+1/n)^n 
# и выведите на экран их сумму, округлённую до трёх знаков после точки.
# Пример:  Для n = 6 -> 14.072

n=int(input('введите целое положительное число n= '))
sum = 0
num =(1 + 1/n)**n
for i in range (1, n+1):
    num =(1 + 1/i)**i
    print(i)
    print(num)
    sum += num
print(round(sum, 3))