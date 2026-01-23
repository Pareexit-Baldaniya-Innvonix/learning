// Task 5:

class Calculator {
    constructor(a, b) {
        this.a = a;
        this.b = b;
    }

    add() {
        console.log(`${this.a} + ${this.b} =`, this.a + this.b);
    }

    sub() {
        console.log(`${this.a} - ${this.b} =`, this.a - this.b);
    }

    mul() {
        console.log(`${this.a} * ${this.b} =`, this.a * this.b);
    }

    div() {
        console.log(`${this.a} / ${this.b} =`, this.a / this.b);
    }
}

const calc = new Calculator(423, 64);
calc.add();
calc.sub();
calc.mul();
calc.div();