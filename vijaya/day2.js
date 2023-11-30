/* 
1. Rewrite using Conditional operator:
a.
let x = 5;

if (x > 0) {
    console.log("Positive");
} else if (x < 0) {
    console.log("Negative");
} else {
    console.log("Zero");
}*/
 
let x = 5;

let message = (x>0)? "Positive" : (x<0)? "Negative" : "zero";
console.log(message);


/*b.
let age = 18;

if (age >= 18) {
    console.log("Eligible to vote");
} else {
    console.log("Not eligible to vote");
}*/

let age = 18;
let message1 = (age >= 18) ? "Eligible to vote" : "Not eligible to vote";
console.log(message1);

/*2. 
a. Logical OR (||):
    Question:
    Write an if statement that checks if a variable value is either null or undefined.

    Question:
    Write a condition using || that assigns a default value of 10 to a variable count if it is falsy.

    Question:
    Check if a user has provided a valid email address. If not, use a default email address.*/
 
    let a;

    if (a == null || a == undefined) {

        console.log(a);
    }

    let count;

    if (!count ) {
        count=10;
        console.log('count: ' + count);
    }

    function validateEmail(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    }
      
      let emailAddress = 'example@email.com';

      if (!validateEmail(emailAddress)) 
      { 

        emailAddress = 'default@email.com';
      }
      console.log(emailAddress);

    

/*
b. Logical AND (&&):
    Question:
    Write an if statement that checks if a number is greater than 10 and less than 20.

    Question:
    Implement a condition using && that prints "Login successful" only if both the username and password are valid.

    Question:
    Check if a person is eligible to vote based on age (18 or older) and citizenship.
*/
    let number=15;
    if (number>10 && number<20) {
        console.log("number is between 10 and 20");
    }

    let username= "Vijaya";
    let password= "Paruchuri";
    if (username=="Vijaya" && password=="Paruchuri"){
        console.log("Loging Successfully");            
    }

    let voterage= 19;
    let citizenship= true;
    if (voterage>=18 && citizenship) {
        console.log("Citizen is eligible to vote");            
    }



/*
c. Nullish Coalescing Operator (??):
    Question:
    Use the nullish coalescing operator to assign a default value of "Guest" to a variable username if it is null or undefined.

    Question:
    Implement a condition using ?? to set the value of result to 0 if value is null or undefined.

    Question:
    Check if a variable price is defined. If not, set it to the default value of 100 using the nullish coalescing operator.
*/



    let username1;
    username1=username1 ?? "Guest"
    console.log(username1);
    


    let result;
    result=result ?? 0
    console.log(result);
    


    let price;
    price=price ?? 100
    console.log(price);
    

/*
3. 
a. Use for loop to generate these patterns
b. use while loop to generate these patterns
Pattern 1
*****
*****
*****
*****
*****
*/
for(i=0; i<5;i++) {
    let pattern="";
    for (j=0; j<5; j++) {
      pattern+="*";
    }
    console.log(pattern);
}

/*
Pattern 2
*****
****
***
**
*
*/
let k=5;
while (k>0){
    let pattern2="";
    let m=k;
    while (m>0 ){
        pattern2+="*";
        m--;
    }
    console.log(pattern2);
    k--;

}



/*
4. Write a JavaScript program that iterates through the numbers from 1 to 20 (inclusive). For multiples of 3, print "Fizz"; for multiples of 5, print "Buzz." However, if a number is a multiple of both 3 and 5, skip that iteration. (hint: 15 is skipped)
Required Output:
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
16
17
Fizz
19
Buzz
*/

const numbers2=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20];
for(i=0;i<numbers2.length; i++)
{
    if (numbers2[i]%3==0 && numbers2[i]%5==0){
        continue;
    }
    else if (numbers2[i]%3==0){
        console.log("Fizz");    
    }
    else if (numbers2[i]%5==0){
        console.log("Buzz");
    }
    else {
        console.log(numbers2[i]);
    }
}

