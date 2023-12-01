/*
1. Create an arrow function that returns the length of a string.
*/

let length = s => s.length;
console.log(length("vijaya"));


/*
2. Convert the following function to an arrow function.

function square(x) {
  return x * x;
}*/

let func = (x) => x*x;
console.log(func(5));


/*3. Implement a function that reverses a string.*/

function reverseString(str) {
    return str.split('').reverse().join('');
}

  let str= 'Javascript';
  let reversedStr = reverseString(str);
  console.log(reversedStr); 

/*4. Write a arrow and normal function that calculates the factorial of a number.*/
let func1 =(a) => {
    let factorial=1;
    for (let i = 2; i <= a; i++){
        factorial *=i;
        
    }
    return factorial;
}
console.log(func1(6));


function fact(a){
    let factorial=1;
    for (let i = 1; i <= a; i++){
        factorial *=i;
    }
    return factorial;
}
 console.log(fact(5));

/*5. Write arrow function, function expression, function that accepts a temperature in Celsius and converts it to Fahrenheit.*/
//arrow function
let fahrenheit=c =>(c * 9 / 5) + 32;
console.log("convertcelciusToFahrenheit:"+ fahrenheit(35));

//function expression
let fahrenheit1= function(c){
    return (c * 9 / 5)+32;
}
console.log("convertcelciusToFahrenheit:"+ fahrenheit1(35));

//function 
function fahrenheitConverter(c){
    return (c * 9 / 5)+32;
}
console.log("convertcelciusToFahrenheit:"+ fahrenheitConverter(35));


/*6. Write differences between all four types of functions in javascript.*/


/*function Declaratioin:

The function keyword followed by a name and a code block.
Can be declared anywhere in the scope before they are called due to hoisting.
Can have their function names used within the function body.

/*Function Expressions:

Defined by assigning a function to a variable, either named or anonymous.
Typically used when functions are treated as data.
Not hoisted, so they can only be called after the assignment.
Can be named or anonymous.

/*Arrow Functions:

 Arrow functions have a simpler and more concise syntax than traditional function expressions.
 Arrow functions make your syntax shorter. Shorter syntax means less writing and reading.
 Arrow functions help make your code pure and testable. And that just makes you a better developer.


/*Anonymous Functions:

An anonymous function in JavaScript is a function that has no name.
 An anonymous function has no identification when it is created.*/