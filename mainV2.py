def validation(number, date, departure_t, flight, departure_a, arrival_a, price):
    if len(number) != 4:
        return 0
    elif len(date) != 10:
        return 0
    elif len(departure_t) != 5:
        return 0
    elif len(flight) != 5:
        return 0
    elif len(departure_a) != 3:
        return 0
    elif len(arrival_a) != 3:
        return 0
    elif '-' in price and len(price) == 0:
        return 0
    else:
        string = f'{number} {date} {departure_t} {flight} {departure_a} {arrival_a} {price}*'
        return string


def flight_creation():
    while True:
        print('Введите данные рейса:')
        number = input('XXXX - номер рейса: ').upper()
        date = input('ДД/ММ/ГГГГ - дата рейса: ')
        departure_t = input('ЧЧ:ММ - время вылета: ')
        flight = input('ЧЧ.ММ - длительность перелета: ')
        departure_a = input('XXX - аэропорт вылета: ').upper()
        arrival_a = input('XXX - аэропорт прилета: ').upper()
        price = input('.XX - стоимость билета (> 0): ')
        temp_string = validation(number, date, departure_t, flight, departure_a, arrival_a, price)
        if temp_string == 0:
            print('\nОшибка. Ввод данных нужно выполнять в указанном программой формате.')
        else:
            print(f'Информация о рейсе: {temp_string} добавлена')
            return temp_string


def all_flights(t_string):
    string = ''
    if len(t_string) == 0:
        print('Информация о рейсах отсутствует')
    else:
        for index in range(len(t_string)):
            if '*' not in t_string[index]:
                string += t_string[index]
            else:
                print(f'Информация о рейсе: {string}')
                string = ''
                continue


def search_by_flight_number(t_string):
    string = ''
    flight_number = input('Введите номер рейса в формате ХХХХ: ').upper()
    for index in range(len(t_string)):
        if '*' not in t_string[index]:
            string += t_string[index]
        else:
            total_str = string
            if flight_number in total_str:
                print(f'Информация о рейсе: {total_str}')
                break
            else:
                string = ''
                continue
    else:
        print(f'Рейс {flight_number} не найден')


def main():
    print('Сервис поиска авиабилетов')
    total_string = ''
    while True:
        print('\n\nГлавное меню:')
        print('\n1 - ввод рейса'
              '\n2 - вывод всех рейсов'
              '\n3 - поиск рейса по номеру'
              '\n0 - завершение работы')
        answer = int(input('\nВведите номер пункта меню: '))
        if answer == 1:
            temp_string = flight_creation()
            total_string += temp_string
        elif answer == 2:
            all_flights(total_string)
        elif answer == 3:
            search_by_flight_number(total_string)
        elif answer == 0:
            print('Завершение работы...')
            break
        else:
            print('Неверный пункт меню.')


main()
