def bank (x, y):
    x0 = x
    for current_year in range(1, y + 1):
        profit = x * 0.1
        x = x + profit
        print(str(current_year) + '-й год - ' + str(x) + ' руб')
    print('Вклад ' + str(x0) + ' руб на ' + str(y) + ' лет. Итог ' + str(x) + ' руб. Доход ' + str(round(x-x0, 2)) + ' руб.')

bank(10, 2)