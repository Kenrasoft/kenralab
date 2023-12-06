//1

function calculator(num1, num2, callback) {
    return callback(num1, num2);
}
const additionResult = calculator(5, 3, (a, b) => a + b);
console.log(additionResult); 

const subResult = calculator(5, 3, (a, b) => a - b);
console.log(subResult); 

const multiplicationResult = calculator(5, 3, (a, b) => a * b);
console.log(multiplicationResult); 

const divisionResult = calculator(5, 3, (a, b) => a / b);
console.log(divisionResult); 

//2

function stringTransformer(str, callback) {
    return callback(str);
}
const capitalize = str => str.toUpperCase();
const reversed = str => str.split('').reverse().join('');
const transformedString1 = stringTransformer("hello", capitalize);
const transformedString2 = stringTransformer("world", reversed);
console.log(transformedString1); 
console.log(transformedString2); 

//3

function repeat(callback, n) {
    for (let i = 0; i < n; i++) {
        callback();
    }
}
const greet = () => console.log("Hello!");
repeat(greet, 3);

//4

function counter() {
    let count = 0;

    return function () {
        count++;
        return count;
    };
}
const incrementCounter = counter();
console.log(incrementCounter());
console.log(incrementCounter()); 

//5

function powerof(n) {
    return function (x) {
        return Math.pow(x, n);
    };
}
const square = powerof(2);
console.log(square(4)); 

//6

function accumulator() {
    let sum = 0;

    return function (number) {
        sum += number;
        return sum;
    };
}
const addNumbers = accumulator();
console.log(addNumbers(5)); 
console.log(addNumbers(3)); 

//7

function customLogger() {
    return function (message) {
        const timestamp = new Date().toISOString();
        console.log(`${timestamp} - ${message}`);
    };
}
const logMessage = customLogger();
logMessage("This is a log message");






