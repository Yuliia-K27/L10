list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 3, 5, 100, 1]

unique_elem = []  # виводимо список унікальних чисел
duplicate_elem = []  # Виводимо список повторюваних чисел


def get_list():  # функція для визначення унікальності цифр у списку.
    print('The current list is:', list)
    try:
        if len(list) == len(set(list)):
            print('This list is unique')
        else:
            print('Is the list unique? No, this is', False)
            for item in list:
                if item not in unique_elem:
                    unique_elem.append(item)
                elif item not in duplicate_elem:
                    duplicate_elem.append(item)
            print('Duplicated numbers:', duplicate_elem)
            print('Set of the unique numbers:', unique_elem)
            print('Set of the unique numbers:', unique_el)  # перевірка виключення NameError.

    except NameError as err:  # виключення
        print('Error:'.upper(), err)


get_list()