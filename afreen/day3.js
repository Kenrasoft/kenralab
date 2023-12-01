const String = (str) => str.length;
console.log(String("Hello")); 


const square = (x) => x * x;
console.log(square(10)); 


const reverseString = (str) => str.split("").reverse().join("");
console.log(reverseString("Hello")); 


const factorialArrow = (n) => (n === 0 || n === 1) ? 1 : n * factorialArrow(n - 1);
function factorialRegular(n) {
    return (n === 0 || n === 1) ? 1 : n * factorialRegular(n - 1);
}
console.log(factorialArrow(7)); 
console.log(factorialRegular(7)); 


const celsiusToFahrenheitArrow = (celsius) => (celsius * 9/5) + 32;
const celsiusToFahrenheitExpression = function(celsius) {
    return (celsius * 9/5) + 32;
};
function celsiusToFahrenheitFunction(celsius) {
    return (celsius * 9/5) + 32;
}
console.log(celsiusToFahrenheitArrow(25)); 
console.log(celsiusToFahrenheitExpression(25)); 
console.log(celsiusToFahrenheitFunction(25)); 


/*Regular Function:

Declared using the function keyword.
Can be declared before they are used (hoisting).
Has its own this value.
Suitable for object methods and constructors.
Function Expression:

Created by assigning a function to a variable.
Cannot be hoisted; must be defined before usage.
May have an anonymous name or be named.
Provides a more flexible approach in terms of when and where the function is defined.
Arrow Function:

Introduced in ES6.
Has a more concise syntax.
Does not have its own this value (inherits from the enclosing context).
Cannot be used for constructors.
Arrow Function in Detail:

Does not have its own arguments object.
Cannot be used with new to create instances.
Cannot be used as a method in an object (lacks its own this).*/