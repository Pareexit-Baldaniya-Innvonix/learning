// Task 3:
// 1. Inheritance:

class Animal {
    constructor(name) {
        this.name = name;
    }

    info() {
        console.log(`Animal name: ${this.name}`);
    }
}

class Dog extends Animal {
    constructor(name) {
        super(name);    // call the parent class
    }

    sound() {
        console.log(`${this.name} Barks..`);
    }
}

const dog = new Dog("Tommy");
dog.info();
dog.sound();