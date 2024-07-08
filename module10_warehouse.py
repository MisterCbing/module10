from multiprocessing import Process, Pipe, Queue, Lock


lock = Lock()

class WarehouseManager:
    data = {}

    def process_request(self, *request):

        with lock:
            if request[1] == "receipt":
                self.data[request[0]] = self.data.get(request[0], 0) + request[2]
            elif request[1] == "shipment":
                self.data[request[0]] = self.data.get(request[0], 0) - request[2]


    def run(self, requests):
        for i in requests:
            proc = Process(target=self.process_request, args=i)
            proc.start()
            proc.join()


if __name__ == '__main__':

    # Создаем менеджера склада
    manager = WarehouseManager()

    # Множество запросов на изменение данных о складских запасах
    requests = [
        ("product1", "receipt", 100),
        ("product2", "receipt", 150),
        ("product1", "shipment", 30),
        ("product3", "receipt", 200),
        ("product2", "shipment", 50)
    ]

    # Запускаем обработку запросов
    manager.run(requests)

    # Выводим обновленные данные о складских запасах
    print(manager.data)