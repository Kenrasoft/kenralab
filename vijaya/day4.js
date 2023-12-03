// Exercise 1:
// Write a function calculator that takes two numbers and a callback function. The callback function should define a mathematical operation (e.g., add, subtract, multiply, divide), and the calculator function should return the result of applying the callback to the two numbers.
function calculate(number1, number2,callback) {

    return callback(number1,number2);

}

function add(number1, number2){
    return number1 + number2;
}
function subtract(number1, number2){
    return number1 - number2;
}
function multiply(number1, number2){
    return number1 * number2;
}
function divide(number1, number2){
    return number1 / number2;
}

const number1=40;
const number2=35;

const sumResult = calculate(number1,number2,add);
const subtractResult = calculate(number1,number2,subtract);
const multiplyResult = calculate(number1,number2,multiply);
const divideResult = calculate(number1,number2,divide);
console.log("add:" +sumResult);
console.log("subtract:" +subtractResult);
console.log("multiply:" +multiplyResult);
console.log("divide:" +divideResult);



// Exercise 2:
// Create a function stringTransformer that takes a string and a callback function. The callback function should transform the string in the ways 1. capitalize, 2. reverse, and the stringTransformer function should return the transformed string.
function stringTransformer(str, callback) {
    return callback(str);
}

function capitalize(str) {
    return str.toUpperCase();
}

function reverse(str){
    return str.split('').reverse().join('');
}

const originalString = "Hello, world!";

const capitalizeString = stringTransformer(originalString,capitalize);
const reverseString = stringTransformer(originalString,reverse);

console.log("capitalize:" + capitalizeString);
console.log("reverse:" + reverseString);
// Exercise 3:
// Implement a function repeat that takes a callback function and a number n. The callback function should be executed n times.

function repeat(n, callback) {
    
    for (i=0; i<n; i++) {
        callback();
    }
}
function sayhello(){
    console.log("Hello");
}
repeat(3, sayhello);


// Exercise 4:
// Create a function counter that returns a closure. The closure should be a function that, when called, increments a counter and returns the current count.
function counter(){
    return function increaseCounter(counter){
        return ++counter;

    }
}
const increamenter = counter();
console.log(increamenter(5));




// Exercise 5:
// Write a function powerOf that takes an exponent n and returns a function. The returned function should take a base x and calculate x raised to the power of n.

function powerOf(n){
    return function calculatePowerof(x) {
        return (x**n);

    }
   
}

const powerOf1 = powerOf(3);
console.log(powerOf1(2));


// Exercise 6:
// Create a function accumulator that returns a closure. The closure should be a function that, when called with a number, adds it to the accumulated sum and returns the updated sum.

function accumulator(sum){
    return function sumAccumulator(number){
        return sum +number;
    }
}

const accumulator1 = accumulator(5);
console.log(accumulator1(4));

// Exercise 7:
// Create a function customLogger that returns a closure. The closure should be a function that, when called with a message, logs the message along with a timestamp.
function customLogger(){
    return function logMessage(message){
        const timestamp = new Date().toUTCString();
        console.log(`[${timestamp}] ${message}`);
    }
}

const logMessage = customLogger()
logMessage("hello world");