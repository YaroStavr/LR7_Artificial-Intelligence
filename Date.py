"""
Использовать словарь, содержащий следующие ключи:
    - название пункта назначения;
    - номер поезда;
    - время отправления.
Написать программу, выполняющую следующие действия:
    - ввод с клавиатуры данных в список, состоящий из словарей заданной структуры;
    - записи должны быть упорядочены по времени отправления поезда;
    - вывод на экран информации о поездах, направляющихся в пункт, название которого введено с клавиатуры;
    - если таких поездов нет,выдать на дисплей соответствующее сообщение.
"""
import sys
from __init__ import __all__
from datetime import datetime

def get_route():
    # Запросить данные о маршруте.
    destination = input("\nНазвание пункта назначения: ")
    numTrain = input("Номер поезда: ")
    time = input("Время отправления (часы минуты): ")

    t = datetime.strptime(time, "%H %M")
    time = str(datetime.time(t))

    # Создать словарь.
    return {
        'destination': destination,
        'numTrain': numTrain,
        'time': time,
    }

def display_routes(routes):
    if routes:
        # Заголовок таблицы.
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 20
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^20} |'.format(
                "№",
                "Пунк назначения",
                "Номер поезда",
                "Время отправления"
            )
        )
        print(line)
        # Вывести данные о всех маршрутах.
        for idx, route in enumerate(routes, 1):
            print(
                '| {:>4} | {:<30} | {:<20} | {:>20} |'.format(
                    idx,
                    route.get('destination', ''),
                    route.get('numTrain', ''),
                    route.get('time', '')
                )
            )
        print(line)
    else:
        print("Список маршрутов пуст")

def select_routes(routes, station):
    # Инициализировать счетчик.
    #count = 0
    # Проверить сведения работников из списка.
    result = []
    for employee in routes:
        if employee.get('destination') == station:
            result.append(employee)
    return result

def print_help():
    print("Список команд:\n")
    print("add - добавить название пункта назначения;")
    print("list - вывести список пунктов назначения;")
    print("select <пункт назначения> - запросить информацию о поездах, направляющихся в пункт;")
    print("help - отобразить справку;")
    print("exit - завершить работу с программой.")

def main():
    # Список пунктов назначения.
    routes = []

    print_help()
    """print("Список команд:\n")
    print("add - добавить название пункта назначения;")
    print("list - вывести список пунктов назначения;")
    print("select <пункт назначения> - запросить информацию о поездах, направляющихся в пункт;")
    print("help - отобразить справку;")
    print("exit - завершить работу с программой.")"""

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input("\ncomand->>> ").lower()
        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break
        elif command == 'add':
            route = get_route()

            # Добавить словарь в список.
            routes.append(route)
            # Отсортировать список в случае необходимости.
            if len(routes) > 1:
                routes.sort(key=lambda item: item.get('time', ''))

        elif command == 'list':
            display_routes(routes)

        elif command.startswith('select '):

            parts = command.split(' ', maxsplit=1)
            # Получить наименования пункта назначения.
            station = str(parts[1])

            selected = select_routes(routes,station)
            display_routes(selected)

        elif command == 'help':
            # Вывести справку о работе с программой.
            print_help()
            """print("Список команд:\n")
            print("add - добавить название пункта назначения;")
            print("list - вывести список пунктов назначения;")
            print("select <пункт назначения> - запросить информацию о поездах, направляющихся в пункт;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")"""
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)



