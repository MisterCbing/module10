import queue
from threading import Thread
from time import sleep

class Cafe:
    def __init__(self, table_list):
        self.q = queue.Queue()
        self.table_list = table_list
        self.с = []

    def customer_arrival(self):
        for i in range(1, 21):
            print(f'Посетитель номер {i} прибыл')
            self.serve_customer(i)
            sleep(1)

    def serve_customer(self, i):
        for t in tables:
            if not t.is_busy:
                Customer(i, t).start()
                break
        self.q.put(i)

    def waiting(self, i):


class Table:
    is_busy = False

    def __init__(self, number):
        self.number = number

class Customer(Thread):

    def __init__(self, number, table):
        super().__init__()
        self.number = number
        self.table = table

    def run(self):
        print(f'Пришёл посетитель {self.number} за столик {self.table.number}.')
        self.table.is_busy = True
        sleep(5)
        print(f'Ушёл посетитель {self.number} из-за столика {self.table.number}.')
        self.table.is_busy = False

tables = []
for i in range(1, 21):
    tables.append(Table(i))

# Инициализируем кафе
cafe = Cafe(tables)

# Запускаем поток для прибытия посетителей
customer_arrival_thread = Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

# Ожидаем завершения работы прибытия посетителей
customer_arrival_thread.join()

# cc = []
# for i in range(10):
#     cc.append(Customer(i, tables[i]))
#
# for i in cc:
#     i.start()
#
# for i in cc:
#     i.join()