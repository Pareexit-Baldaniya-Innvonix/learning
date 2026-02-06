// Task 2:

const add = require('./math_operation/basic/add');
const sub = require('./math_operation/basic/sub');
const mul = require('./math_operation/advanced/mul');
const div = require('./math_operation/advanced/div');

console.log("Addition: ", add(20, 5));
console.log("Subtraction: ", sub(12, 2));
console.log("Multiplication: ", mul(5, 43));
console.log("Division: ", div(43, 3));