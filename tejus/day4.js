//1

function calculator(num1, num2, calculate) {
  if (typeof num1 !== 'number' || typeof num2 !== 'number') {
    return "invalid numbers.";
  }

  if (typeof calculate !== 'function') {
    return "invalid callback function.";
  }

  return calculate(num1, num2);
}

const addCallback = (a, b) => a + b;
const subCallback = (a, b) => a - b;
const mulCallback = (a, b) => a * b;
const divCallback = (a, b) => a / b;

const addResult = calculator(5, 3, addCallback);
console.log("Addition Result:", addResult); 
const subResult = calculator(10, 4, subCallback);
console.log("Subtraction Result:", subResult);

//2

function capRev(str) {
    str = str.toUpperCase();
    return str.split('').reverse().join('');
}

function stringTransformer(inputString, transform) {
    if (typeof inputString !== 'string') {
        return "invalid string.";
    }
    if (typeof transform !== 'function') {
        return "invalid callback function.";
    }

    return transform(inputString);
}
  
const result = stringTransformer("trisquare", capRev);
console.log("capitalized and reversed Result:", result);

//3

function repeat(count, n) {
    if (typeof count !== 'function') {
        return "Please provide a valid callback function.";
    }

    if (!Number.isInteger(n) || n < 0) {
        return "Please provide a valid positive integer for n.";
    }
    for (let i = 0; i < n; i++) {
        count();
    }
}

function callb() {
console.log("callback function");
}

repeat(callb, 3);

//4

function counter() {
    let count = 0; 
    function closure() {
      count++; 
      return count; 
    }

    return closure;
}
  
const myCounter = counter();

console.log(myCounter());
console.log(myCounter());
console.log(myCounter());

//5

function powerOf(n) {
    // Define the closure function
    function power(x) {
      return Math.pow(x, n); 
    }

    return power;
}

const square = powerOf(2);
console.log(square(4));

//6

function accumulator() {
    let sum = 0;
    function addNum(number) {
      sum += number; 
      return sum;
    }
  
    return addNum;
}

const myAccumulator = accumulator();

console.log(myAccumulator(5)); 
console.log(myAccumulator(8));

//7

function customLogger() {
    function logMessage(msg) {
      const timestamp = new Date().toLocaleString();
      console.log(`${timestamp} - ${msg}`); 
    }
  
    return logMessage;
}

const Logger = customLogger();

Logger("log message."); 