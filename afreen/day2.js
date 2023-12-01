//1

let x=5;
let message = (x > 0) ? 'Promise' :
(x < 0)  ? 'Negative' :
'Zero' ;
console.log(message);

let age = 18;
let message2 = (age>=18) ? 'Eligible to vote' :
'Not eligible to vote';
console.log(message2);

//2

let Variable = 5-5 ;
if (Variable === null || Variable === undefined) {
}
console.log('Variable is either null or undefined');

//2b

let Number = 15;

if (Number > 10 && Number < 20) {
    console.log("The number is greater than 10 and less than 20.");
} 

let username = 'afreenkenra';
let password = 123456;
if (username==='afreenkenra' && password===123456) {
    console.log("Login successful");
} else {
    console.log("Invalid username or password");
}

let ager =23;
let Citizen = 'Indian';
if (ager >= 18 && Citizen) {
    console.log("Eligible to vote");
} else {
    console.log("Not eligible to vote");
}

//2c

let usernamee = null;
username = usernamee ?? "Guest";
console.log(username);

let value = null;
result = value ?? 0
console.log(value);

let price = 50;
price = price ?? 100;
console.log(price);

//3

console.log("Pattern 1:");
for (let i = 0; i < 5; i++) {
    let row = '';
    for (let j = 0; j < 5; j++) {
        row += '*';
    }
    console.log(row);
}

console.log("Pattern 1:");
let i = 0;
while (i < 5) {
    let j = 0;
    let row = '';
    while (j < 5) {
        row += '*';
        j++;
    }
    console.log(row);
    i++;
}

//4

for (let i = 1; i <= 20; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
        continue;
    }
    if (i % 3 === 0) {
        console.log("Fizz");
    }
    else if (i % 5 === 0) {
        console.log("Buzz");
    }
    else {
        console.log(i);
    }
}
