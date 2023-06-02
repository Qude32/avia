def flight_creation():
    string = ''
    print('Введите данные рейса:')
    while True:
        number = input('XXXX - номер рейса: ').upper()
        if len(number) != 4:
            print('Номер рейса должен состоять из 4х символов.')
        else:
            string += number + ' '
            break
    while True:
        date = input('ДД/ММ/ГГГГ - дата рейса: ')
        if len(date) != 10:
            print('Дата должна содержать 10 символов.')
        else:
            string += date + ' '
            break
    while True:
        departure_t = input('ЧЧ:ММ - время вылета: ')
        if len(departure_t) != 5:
            print('Время должно содержать 5 символов.')
        else:
            string += departure_t + ' '
            break
    while True:
        flight = input('ЧЧ.ММ - длительность перелета: ')
        if len(flight) != 5:
            print('Длительность перелета должна содержать 5 символов и не быть отрицательной.')
        elif '-' in flight:
            print('Длительность перелета не может быть отрицательной')
        else:
            string += flight + ' '
            break
    while True:
        departure_a = input('XXX - аэропорт вылета: ').upper()
        if len(departure_a) != 3:
            print('Аэропорт вылета должен содержать 3 символа.')
        else:
            string += departure_a + ' '
            break
    while True:
        arrival_a = input('XXX - аэропорт прилета: ').upper()
        if len(arrival_a) != 3:
            print('Аэропорт вылета должен содержать 3 символа.')
        else:
            string += arrival_a + ' '
            break
    while True:
        price = input('.XX - стоимость билета (> 0): ')
        if '-' in price:
            print('Стоимость не может быть отрицательной.')
        elif len(price) == 0:
            print('Стоимость не может быть равна 0.')
        else:
            string += price + '*'
            break
    print(f'\nИнформация о рейсе {number} {date} {departure_t} {flight} {departure_a} {arrival_a} {price}* добавлена')
    return string


def all_flights(t_string):
    string = ''
    if len(t_string) == 0:
        print('Информация о рейсах отсутствует')
    else:
        for i in range(len(t_string)):
            if '*' not in t_string[i]:
                string += t_string[i]
            else:
                print(f'Информация о рейсе: {string}')
                string = ''
                continue


def search_by_flight_number(t_string):
    string = ''
    flight_num = input('Введите номер рейса в формате ХХХХ: ').upper()
    for i in range(len(t_string)):
        if '*' not in t_string[i]:
            string += t_string[i]
        else:
            total_str = string
            if flight_num in total_str:
                print(f'Информация о рейсе: {total_str}')
                break
            else:
                string = ''
                continue
    else:
        print(f'Рейс {flight_num} не найден')


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
            temp_str = flight_creation()
            total_string += temp_str
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
