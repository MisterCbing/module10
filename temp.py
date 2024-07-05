import queue
from threading import Thread
from time import sleep

class Cafe:

    def __init__(self, table_list):
        self.customers = []
        self.q = queue.Queue()
        self.table_list = table_list

    def customer_arrival(self):
        for i in range(1, 21):
            print(f'Посетитель номер {i} прибыл')
            self.serve_customer(i)
            sleep(1)
        print(self.q)

    def serve_customer(self, i):
        # self.q.put(i)
        # if any(not t.is_busy for t in self.table_list):
        #     j = self.q.get()
        #     for t in tables:
        #         if not t.is_busy:
        #             self.customers.append(Customer(j, t))
        #             self.customers[-1].start()
        #             break
        # if not self.q.empty():
        #     print(f'Посетитель номер {i} ожидает свободный стол.')


    def run(self):
        while True:

            try:
                i = self.q.get(timeout=1)
                for t in tables:
                    if not t.is_busy:
                        self.customers.append(Customer(i, t))
                        self.customers[-1].start()
                        break
            except:
                break
            for c in self.customers:
                c.join()



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
        # print(f'Посетитель номер {self.number} сел за стол {self.table.number}.')
        # self.table.is_busy = True
        # sleep(5)
        # print(f'Посетитель номер {self.number} покушал и ушёл. ')
        # self.table.is_busy = False


table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

# Инициализируем кафе
cafe = Cafe(tables)

# Запускаем поток для прибытия посетителей
customer_arrival_thread = Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

# Ожидаем завершения работы прибытия посетителей
customer_arrival_thread.join()