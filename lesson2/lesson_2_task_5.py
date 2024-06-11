def month_to_season (monthNum):
    if (monthNum == "12" or monthNum == "1" or monthNum == "2"):
       print("Это зима")
    elif (monthNum == "3" or monthNum =="4" or monthNum =="5"):
        print("Это весна")
    elif (monthNum == "6" or monthNum =="7" or monthNum =="8"):
        print("Это лето")
    elif (monthNum == "9" or monthNum =="10" or monthNum =="11"):
        print("Это осень")
    else:
        print("Это ошибка")

Month = input('Введите номер месяца:')
month_to_season(Month)