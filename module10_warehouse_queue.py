from multiprocessing import Process, Pipe, Queue


class WarehouseManager:
    data = {}


    def process_request(self, *request):
        request, temp = request[0], request[1].get()
        if request[1] == "receipt":
            temp[request[0]] = temp.get(request[0], 0) + request[2]
        elif request[1] == "shipment":
            temp[request[0]] = temp.get(request[0], 0) - request[2]
        q.put(temp)

    def run(self, requests):

        for i in requests:
            proc = Process(target=self.process_request, args=(i, q))
            proc.start()
            proc.join()
        self.data = q.get()

if __name__ == '__main__':
    q = Queue()
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