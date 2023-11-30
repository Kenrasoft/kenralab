//1

let x = 5;

let result = x>0 ? "positive" : x<0 ? "negative" : "zero";
console.log(result)

let age = 18;

let result1 = age >= 18 ? "eligible to vote" : "not eligible to vote";
console.log(result1)

//2

let a = null;

if (a === null || a === undefined) {
    console.log("variable is null or undefined");
} else {
    console.log("variable has a value")
}

let count = undefined;
count = count || 10;
console.log(count);

let userInputEmail = "abc@email";
let validEmail = "qwerty@email";
let email = validEmail == userInputEmail ? userInputEmail : "default@email";
console.log(email);

let number = 15;
if (number > 10 && number < 20) {
    console.log("Number is greater than 10 and less than 20");
} else {
    console.log("Number is not in range");
}

let username = "trisquare";
let password = "kenrasoft";
if (username === "trisquare" && password === "kenrasoft") {
    console.log("Login successful");
} else {
    console.log("Invalid username or password");
}

let voterAge = 24;
let isCitizen = true;
if (voterAge >= 18 && isCitizen) {
    console.log("Person is eligible to vote");
} else {
    console.log("Person is not eligible to vote");
}
let guestname = null;
guestname = guestname ?? "Guest";
console.log(guestname);

let value = null;
let resvalue = value ?? 0;
console.log(resvalue);

let price = null;
price = price ?? 100;
console.log(price);

// 3

console.log("Pattern 1 using for loop:");
for (let i = 0; i < 5; i++) {
    let row = "";
    for (let j = 0; j < 5; j++) {
        row += "*";
    }
    console.log(row);
}

console.log("\nPattern 2 using for loop:");
for (let i = 5; i > 0; i--) {
    let row = "";
    for (let j = 0; j < i; j++) {
        row += "*";
    }
    console.log(row);
}

console.log("Pattern 1 using while:");
let i = 0;
while (i < 5) {
    let j = 0;
    let row = "";
    while (j < 5) {
        row += "*";
        j++;
    }
    console.log(row);
    i++;
}

console.log("\nPattern 2 using while:");
let k = 5;
while (k > 0) {
    let l = 0;
    let row = "";
    while (l < k) {
        row += "*";
        l++;
    }
    console.log(row);
    k--;
}
//4
for (let i = 1; i <= 20; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
        continue;
    } else if (i % 3 === 0) {
        console.log("Fizz");
    } else if (i % 5 === 0) {
        console.log("Buzz");
    } else {
        console.log(i);
    }
}