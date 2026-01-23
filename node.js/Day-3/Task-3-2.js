// Task 3:
// 2. Constructors:
class Parent {
    constructor(...args) {
        console.log(`Parent's class ${args}`);
        this.data = x;
    }
}

class SubClass extends Parent {
    constructor(...args) {
        super(...args);
    }
}

const newclass = new SubClass(1, 2, 3, 4);
console.log(newclass);