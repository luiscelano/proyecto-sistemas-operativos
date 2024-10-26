import time
import threading
import random

# Variables de control para el algoritmo de Dekker
turn = 0
flag = [False, False]  # Bandera para cada proceso

# Recurso crítico simulado
#shared_resource = 0

# Función para el proceso 1
def proceso1():
    global turn, flag
    for _ in range(1):  # Número de veces que el proceso intenta entrar a la sección crítica
        # Proceso 1 intenta entrar a la sección crítica
        flag[0] = True
        while flag[1]:  # Espera si el proceso 2 quiere entrar
            if turn != 0:
                flag[0] = False
                while turn != 0:
                    pass
                flag[0] = True
        # Sección crítica
        print("Proceso 1: Entrando a la sección crítica")
        print("Proceso 2: En espera...")
        time.sleep(5)  # Simula el trabajo en la sección crítica
        print("Proceso 1: Saliendo de la sección crítica")
        # Fin de la sección crítica
        turn = 1
        flag[0] = False
        # Fin del ciclo
        print("Proceso 1: Fin del ciclo\n")

# Función para el proceso 2
def proceso2():
    global turn, flag
    for _ in range(1):  # Número de veces que el proceso intenta entrar a la sección crítica
        # Proceso 2 intenta entrar a la sección crítica
        flag[1] = True
        while flag[0]:  # Espera si el proceso 1 quiere entrar
            if turn != 1:
                flag[1] = False
                while turn != 1:
                    pass
                flag[1] = True
        # Sección crítica
        print("Proceso 2: Entrando a la sección crítica")
        time.sleep(5)  # Simula el trabajo en la sección crítica
        print("Proceso 2: Saliendo de la sección crítica")
        # Fin de la sección crítica
        turn = 0
        flag[1] = False
        # Fin del ciclo
        print("Proceso 2: Fin del ciclo\n")

# Función para ejecutar el algoritmo de Dekker simple
def algoritmo_dekker_simple():
    # Crear hilos para los procesos
    hilo1 = threading.Thread(target=proceso1)
    hilo2 = threading.Thread(target=proceso2)

    # Iniciar los hilos
    hilo1.start()
    hilo2.start()

    # Esperar a que ambos hilos terminen
    hilo1.join()
    hilo2.join()

# Clase tenedor - Cena de los filosofos
class Fork:
    def __init__(self):
        self.lock = threading.Lock()

# Clase filosofo - Cena de los filosofos
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


# Algoritmo que replica la cena de los filosofos
def algoritmo_filosofos():
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

# Menú sin la opción de ingresar iteraciones
def mostrar_menu():
    print("\nSeleccione una opción:")
    print("1. Algoritmo de Dekker")
    print("2. Problema de los Filósofos Comensales")
    print("3. Salir\n\n")

while True:
    mostrar_menu()
    opcion = input("Ingrese el número de su opción: ")

    if opcion == "1":
        algoritmo_dekker_simple()
    elif opcion == "2":
        algoritmo_filosofos()
    elif opcion == "3":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, seleccione nuevamente.")
