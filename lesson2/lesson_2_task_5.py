def month_to_season (monthNum):
    if (monthNum in ("12", "1", "2")):
       print("Это зима")
    elif (monthNum in ("3", "4", "5")):
        print("Это весна")
    elif (monthNum in ("6", "7", "8")):
        print("Это лето")
    elif (monthNum in ("9", "10", "11")):
        print("Это осень")
    else:
        print("Это ошибка")

month = input('Введите номер месяца:')
month_to_season(month)