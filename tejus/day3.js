// 1
const strLength = (s) => s.length;
const input = "trisquare";

console.log(`Length of the string: ${strLength(input)}`);

//2
const square = (x) => x*x;
console.log(`square : ${square(5)}`);

//3
function reverseString(str) {
    return str.split('').reverse().join('');
}

const original = "trisquare";
const reversed = reverseString(original);

console.log(`Original String: ${original}`);
console.log(`Reversed String: ${reversed}`);

//4
const factArrow = (n) => (n === 0 || n === 1) ? 1 : n * factArrow(n - 1);
console.log(`Factorial arrow: ${factArrow(5)}`);

function factorial(n) {
    return (n === 0 || n === 1) ? 1 : n * factorial(n - 1);
}
console.log(`Factorial : ${factorial(5)}`) 

//5
const c = 25;

const cfArrow = (celsius) => (celsius * 9/5) + 32;
console.log(`Farenheit : ${cfArrow(c)}°F (Arrow Function)`);

const cfExpression = function(celsius) {
    return (celsius * 9/5) + 32;
};
console.log(`Farenheit : ${cfExpression(c)}°F (Function Expression)`);

function cfFunction(celsius) {
    return (celsius * 9/5) + 32;
}
console.log(`Farenheit : ${cfFunction(c)}°F (Regular Function)`);

//6
// Function declaration:
// Defined using function keyword and followed by a function name
// Can be hoisted, meaning they are moved to top of the code during compilation.
// Which means we can use this function before the declaration in code.

// Function expression:
// defined by assigning a function to a variable
// not hoisted in the same way as function declarations

// Arrow function:
// introduced in ES6
// shorter syntax using the => notaion
// suitable for concise and inline functions

// Generator functions
// introduced in ES6
// defined using function* syntax
// can pause and resume execution using yield keyword
// suitable for scenarios where the function needs to produce a sequence of values over time.