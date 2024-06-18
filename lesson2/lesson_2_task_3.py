import math

def square (a):
    sumSquare = a*a
    return sumSquare

a = math.ceil(float(input('Введите сторону квадрата:')))
print ('Площадь квадрата равна ', square(a))