// Task 4:

class Employee {
    constructor() {
        this.name = "Virat";
        this.add = new Address();
    }

    info() {
        console.log(`Name: ${this.name}`);
        this.add.display();
    }
}

class Address {
    constructor() {
        this.country = "India";
    }
    
    display() {
        console.log(`Address: ${this.country}`);
    }
}

const emp = new Employee();
emp.info();