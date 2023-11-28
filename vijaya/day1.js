//console.log("Hello world!");
//Variables:
//1. Declare a variable name and assign the value "John" to it.
var name="John";
//2.Create a variable age and set it to 25.
var age=25;
//3. What is the difference between let, const, and var in JavaScript? List all differences

/*In JavaScript, var, let, and const are used to declare variables, but they differ in terms of scope, hoisting, and mutability:
var has function-level scope and allows both redeclaration and reassignment, while let and const have block-level scope, 
and const additionally ensures that the variable reference remains constant (though not the value itself for objects or arrays).
 The choice between them depends on the desired scope and whether you need to reassign the variable or keep it constant.*/


 //Data Types:
// /1.List the primitive data types in JavaScript.
/*

In JavaScript, there are six primitive data types:

Number: Represents numeric data, including integers and floating-point numbers. Example: let num = 10;

String: Represents textual data enclosed in single (') or double (") quotes. Example: let str = 'Hello';

Boolean: Represents a logical entity, true or false. Example: let isTrue = true;

Null: Represents the intentional absence of any value. Example: let nullValue = null;

Undefined: Represents a variable that has been declared but not assigned a value yet. Example: let undefinedValue;

Symbol: Represents a unique and immutable value often used as an identifier for object properties. Example: let sym = Symbol('description');
*/


// 2. Create a variable isStudent and set it to true. What data type is isStudent?

let isStudent = true;// Boolean


// 3. What is the typeof operator used for in JavaScript?

console.log(typeof 42); 
console.log(typeof 'Hello'); 
console.log (typeof true); 

//The typeof operator in JavaScript is used to determine the data type of a given variable or expression. It returns a string indicating the type of the operand.



// Type Conversions:
// 1. Convert the string "50" to a number.
let stringNum = "50";
let number = +stringNum;
console.log(number); 

// 2. Change the boolean value isLogged to a string.
let isLogged = true;
let stringIsLogged = isLogged.toString();
console.log(stringIsLogged);
// 3. Perform a type conversion to convert a number to a boolean.

let number1 = 0;
let booleanFromNumber = !!number1; // Using double negation (!!) to convert to boolean
console.log(booleanFromNumber); 

let number2 = 5;
let booleanFromNumber1 = Boolean(number2);
console.log(booleanFromNumber1); 



// Basic Operators:
// 1. Create two variables, num1 and num2, with values 10 and 5. Perform addition, subtraction, multiplication, and division operations on them.
let num1 =10;
let num2 =5;
let sum=num1+num2;
let sub=num1-num2;
let mul=num1*num2;
let div=num1/num2;

console.log("sum:"+sum);

console.log("sub:"+sub);

console.log("mul:"+mul);

console.log("div:"+div);


// 2. Concatenate two strings, "Hello" and "World", using the + operator.
console.log("Hello"+"World");

// 3. What does the % operator do in JavaScript?
/*In JavaScript, the % operator is the modulo operator. It returns the remainder of a division operation between two numbers.*/

