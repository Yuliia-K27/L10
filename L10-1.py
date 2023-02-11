# Написати функцію, яка б приймала номер місяця, і вертала б його назву. Реалізувати у функції декілька обробок виключень.

# створюємо словник:
months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August',
          9: 'September', 10: 'October', 11: 'November', 12: 'December'}


# створюєм функцію, яка повертатиме назву місяця за його номером.
def get_months():
    while True:
        try:
            month = int(input('Enter a number to get the name of a month: '))
            if month == 1 or month == 2 or month == 3 or month == 4 \
                    or month == 5 or month == 6 or month == 7 \
                    or month == 8 or month == 9 or month == 10 or month == 11 \
                    or month == 12:
                print(months[month], '\n')
                return get_months()
            elif month > 12:
                raise
            elif month <= 0:
                print('Sorry! it was a wrong number! The program will be closed')
                break

        # створюєм блок перехоплення виключень
        except ValueError as val:
            print('Could not convert data to an integer:'.upper(), val, '\n')
        except Exception:
            print('Please enter a valid number'.upper(), "[from 1 to 12]\n")


get_months()
