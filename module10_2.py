from threading import Thread
from time import sleep

class Knight(Thread):
    enemies = 100

    def __init__(self, name, skill):
        super().__init__()
        self.name = name
        self.skill = skill

    def run(self):
        print(f'{self.name}, на нас напали!')
        i = 0
        while True:
            sleep(1)
            i += 1
            self.enemies -= self.skill if self.enemies >= self.skill else 0
            print(f'{self.name} сражается {i} день(дня)..., осталось {self.enemies} воинов.')
            sleep(1)
            if self.enemies == 0:
                break
        print(f'{self.name} одержал победу спустя {i} дней!')

knight1 = Knight("Sir Lancelot", 10) # Низкий уровень умения
knight2 = Knight("Sir Galahad", 20) # Высокий уровень умения
knight1.start()
knight2.start()
knight1.join()
knight2.join()