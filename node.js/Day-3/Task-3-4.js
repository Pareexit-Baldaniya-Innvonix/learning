// Task 3:
// 4. Method Overriding:

class A {
    func1() {
        console.log("Feature 1 of class A");
    }

    func2() {
        console.log("Feature 2 of class A");
    }
}

class B extends A {
    func1() {
        console.log("Modified feature 1 of class A by class B");
    }

    func3() {
        console.log("Feature 3 of class B");
    }
}

const obj = new B();
obj.func1();
obj.func2();