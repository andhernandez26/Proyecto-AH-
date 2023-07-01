
def get_date():
        year = input('Ingrese el año (en numeros): ')
        while not year.isnumeric() or not len(year)== 4:
                year = input("Ingrese un valor valido: ")
        month = input('Ingrese el mes (en numeros): ')
        while not month.isnumeric() and int(month) not in range(1, 12):
                month= input("Ingrese un valor valido: ")
        day = input('Ingrese el dia (en numeros): ')
        if month == "2":
                while not day.isnumeric() and int(year) not in range(1, 29):
                        day = input("Ingrese un valor valido: ")
        elif month in ["4", "6", "9", "11"]:
                while not day.isnumeric() and int(year) not in range(1, 31):
                        day = input("Ingrese un valor valido: ")
        else: 
                while not day.isnumeric() and int(year) not in range(1, 31):
                        day = input("Ingrese un valor valido: ")
        date = f'{year}/{month}/{day}'

        return date