// Task 3: Decorators

function changeCase(func) {
    return function() {
        const result = func();
        return result.toUpperCase();
    };
}

function myFunction() {
    return "Hello World!";
}

// decorator
const decoratorFunction = changeCase(myFunction);

console.log(decoratorFunction());