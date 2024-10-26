import threading
import time
import random

class Fork:
    def __init__(self):
        self.lock = threading.Lock()

class Philosopher(threading.Thread):
    def __init__(self, name, left_fork, right_fork):
        super().__init__()
        self.name = name
        self.left_fork = left_fork
        self.right_fork = right_fork

    def eat(self):
        # Determina el orden de recogida de tenedores
        if self.name == "Nietzsche":
            self.right_fork.lock.acquire()
            self.left_fork.lock.acquire()
        else:
            self.left_fork.lock.acquire()
            self.right_fork.lock.acquire()

        print(f"{self.name} está comiendo.")
        time.sleep(random.uniform(0.5, 1.5))  # Simula el tiempo comiendo
        print(f"{self.name} ha terminado de comer.")

        self.left_fork.lock.release()
        self.right_fork.lock.release()

    def run(self):
        while True:
            self.eat()
            print(f"{self.name} está pensando.")
            time.sleep(random.uniform(0.5, 1.5))  # Simula el tiempo pensando

def main():
    forks = [Fork() for _ in range(5)]
    philosophers = [
        Philosopher("Sócrates", forks[0], forks[1]),
        Philosopher("Platón", forks[1], forks[2]),
        Philosopher("Aristóteles", forks[2], forks[3]),
        Philosopher("Kant", forks[3], forks[4]),
        Philosopher("Nietzsche", forks[4], forks[0]),
    ]

    for philosopher in philosophers:
        philosopher.start()

    # Deja que los filósofos coman por un tiempo y luego detén el programa
    time.sleep(10)
    for philosopher in philosophers:
        philosopher.join(timeout=1)

if __name__ == "__main__":
    main()
