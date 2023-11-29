let name = "john";
let age = 10;

// difference between var,let and const:
// scope:
// Variables declared with var are function-scoped. They are visible throughout the entire function in which they are declared. 
// If declared outside any function, they become globally scoped.
// Variables declared with let and const are block-scoped. They are only visible within the block (statements enclosed in curly braces) 
// in which they are defined
// Reassignment:
// var: Variables declared with var can be reassigned and updated.
// let: Variables declared with let can be reassigned, but they cannot be re-declared in the same scope.
// const: Variables declared with const cannot be reassigned or re-declared in the same scope. They are constant.
// Initialization:
// var: Variables declared with var are initialized with undefined by default.
// let and const: Variables declared with let and const are not automatically initialized. Accessing them before assignment results 
// in a ReferenceError.


// primitive data types: number,string,boolean,null,undefined,symbol

let isStudent=true;
// isStudent is boolean
// The typeof operator in JavaScript is used to determine the data type of a given variable or expression
typeof isStudent;


let str = "50";
let num = parseInt(str);

let isLogged = true;
let string = String(isLogged);

let number = 777;
let bool = Boolean(number);


let num1 = 4;
let num2 = 5;
let add = num1 + num2;
let sub = num1 - num2;
let mul = num1 * num2;
let div = num1 / num2;

let word = "hello" + "world";

let mod = num2 % num1;
// % operator gives the remainder after performing division.
