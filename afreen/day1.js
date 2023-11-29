
//Variabes
let name ='John';
console.log(name);
let age=25;
console.log(age);

/*In JavaScript, let, var, and const are used to declare variables, but they have some key differences in terms of scoping, hoisting, and mutability.
var:
Scope: Function-scoped (or globally-scoped if declared outside any function).
Hoisting: Variables declared with var are hoisted to the top of their scope. This means you can use a variable before it's declared, but it will be initialized with undefined.
Reassignment: Can be redeclared and reassigned.
let:
Scope: Block-scoped. Variables declared with let are only accessible within the block (or statement) where they are defined.
Hoisting: Variables declared with let are hoisted to the top of their block but are not initialized. Accessing the variable before the declaration results in a ReferenceError.
Reassignment: Can be reassigned but not redeclared.
const:
Scope: Block-scoped.
Hoisting: Like let, variables declared with const are hoisted to the top of their block but are not initialized.
Reassignment: Cannot be reassigned after declaration. It is a constant value.*/


//Datatypes

/*Datatypes
The primitive data type in JS
In JavaScript, primitive data types are basic data types that are not objects and do not have methods. There are six primitive data types:
Number: Represents numeric values. It includes integers and floating-point numbers.
String: Represents sequences of characters enclosed in single (' ') or double (" ") quotes.
Boolean: Represents a logical value, either true or false.
Undefined: Represents a variable that has been declared but has not been assigned a value.
Null: Represents the intentional absence of any object value.
Symbol: Introduced in ECMAScript 6 (ES6), symbols are unique and immutable data types. They are often used as keys for object properties.
*/


let isStudent=true;
// isStudent is boolean
console.log(isStudent);

/*The typeof operator is used to determine the data type of a variable or an expression. It is a unary operator that takes an operand (a variable or an expression) and returns a string indicating the data type of that operand.*/

//test conservation
let str = "50";
let num = Number(str);
console.log(str)

let isLogged = true;
let string = String(isLogged);
console.log(isLogged)

let number = 5;
let bool = Boolean(number);
console.log(number)

// Basic operation
let num1 = 2;
let num2 = 5;
let add = num1 + num2;
let sub = num1 - num2;
let mul = num1 * num2;
let div = num1 / num2;

let sen = "hello" + "world";
console.log(sen);

let mod = num2 % num1;
// % operator defines the division.


