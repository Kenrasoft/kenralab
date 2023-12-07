//1

const user = {};
user.name = "John";
user.surname = "Smith";
user.name = "Pete";
delete user.name;

//2

let salaries = {
    John: 100,
    Ann: 160,
    Pete: 130
};

let sum = 0;
for (let i in salaries) {
sum += salaries[i];
}

console.log(sum); 

//3

function multiply(obj) {
    for (let i in obj) {
      if (typeof obj[i] === 'number') {
        obj[i] *= 2;
        }
    }
}

let menu = {
width: 200,
height: 300,
title: "My menu"
};

multiply(menu);
console.log(menu);