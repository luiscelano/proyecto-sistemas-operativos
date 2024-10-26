class Philosopher {
    constructor(name, leftFork, rightFork) {
        this.name = name;
        this.leftFork = leftFork;
        this.rightFork = rightFork;
    }

    async eat() {
        console.log(`${this.name} está pensando.`);
        await this.getForks();
        console.log(`${this.name} está comiendo.`);
        await this.sleep(1000); // Simula el tiempo comiendo
        this.putForks();
        console.log(`${this.name} ha terminado de comer.`);
    }

    async getForks() {
        await this.leftFork.pickUp();
        await this.rightFork.pickUp();
    }

    putForks() {
        this.leftFork.putDown();
        this.rightFork.putDown();
    }

    sleep(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }
}

class Fork {
    constructor() {
        this.lock = false;
    }

    async pickUp() {
        while (this.lock) {
            await this.sleep(100); // Espera si el tenedor está en uso
        }
        this.lock = true; // Tenedor en uso
    }

    putDown() {
        this.lock = false; // Libera el tenedor
    }

    sleep(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }
}

async function dinner(philosophers) {
    const promises = philosophers.map(philosopher => philosopher.eat());
    await Promise.all(promises);
}

const forks = [new Fork(), new Fork(), new Fork(), new Fork(), new Fork()];
const philosophers = [
    new Philosopher("Sócrates", forks[0], forks[1]),
    new Philosopher("Platón", forks[1], forks[2]),
    new Philosopher("Aristóteles", forks[2], forks[3]),
    new Philosopher("Kant", forks[3], forks[4]),
    new Philosopher("Nietzsche", forks[4], forks[0]),
];

dinner(philosophers);
