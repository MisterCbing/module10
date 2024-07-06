from threading import Thread
from time import sleep
from queue import Queue


class Customer(Thread):
    def __init__(self, cafe, number):
        super().__init__()
        self.cafe = cafe
        self.number = number

    def service(self, tab):
        tab.is_busy = True
        i = self.cafe.q.get()
        print(f'Посетитель {i} сел за стол {tab.number}')
        sleep(5)
        print(f'Посетитель {i} покушал и ушёл')
        tab.is_busy = False

    def run(self):
        if self.cafe.free_tables():
            print(f'Посетитель {self.number} встал в очередь')
            # self.cafe.q.put(self.number)
        while True:
            if not self.cafe.free_tables():
                for t in self.cafe.tables:
                    if not t.is_busy:
                        self.service(t)
                        break

                break
            sleep(1)


class Table:
    is_busy = False

    def __init__(self, number):
        self.number = number


class Cafe:
    cc = []
    q = Queue()

    def __init__(self, tables):
        self.tables = tables

    def customer_arrival(self):
        for i in range(1, 21):
            print(f'Прибыл посетитель №{i}')
            self.serve_customer(i)
            sleep(1)

    def serve_customer(self, cus):
        self.cc.append(Customer(self, cus))
        self.q.put(cus)
        self.cc[-1].start()

    def free_tables(self):
        return all(map(lambda x: x.is_busy, self.tables))


# Создаем столики в кафе
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
