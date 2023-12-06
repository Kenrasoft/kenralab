// Write the code, one line for each action:
// a. Create an empty object user.
let user={};

// b. Add the property name with the value John.
user.name="John";

// c. Add the property surname with the value Smith.
user.surname="Smith";

// d. Change the value of the name to Pete.
user.name="Pete";

// e. Remove the property name from the object.
delete user.name;
console.log(user);
//2.
// We have an object storing salaries of our team:

let salaries = {
  John: 100,
  Ann: 160,
  Pete: 130
}


// Write the code to sum all salaries and store in the variable sum. Should be 390 in the example above.

let sum = salaries.John+salaries.Ann+salaries.Pete;
console.log(sum);
// If salaries is empty, then the result must be 0.
salaries={};
sum = salaries.John+salaries.Ann+salaries.Pete;
console.log(sum);

//3.
// Create a function multiplyNumeric(obj) that multiplies all numeric property values of obj by 2.
// For instance:
// // before the call
let menu = {
  width: 200,
  height: 300,
  title: "My menu"
};

function multiplyNumeric(menu){
    for (let key in menu){     
        if (typeof menu[key] == 'number'){
            menu[key] = 2 * menu[key];
        }        
    }    
}

multiplyNumeric(menu);
console.log(menu);

// // after the call
// menu = {
//   width: 400,
//   height: 600,
//   title: "My menu"
// };
// Please note that multiplyNumeric does not need to return anything. It should modify the object in-place.
// P.S. Use typeof to check for a number here.