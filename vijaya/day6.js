//Explore all in build methods that can be used.

// Examples of String methods

let message = 'Hello, World!';
console.log(message.toUpperCase());
console.log(message.toLowerCase()); 

let text = 'Vijaya is learning about HTML and CSS pages';
console.log(text.indexOf('HTML')); 
console.log(text.lastIndexOf('CSS')); 

let sentence = 'This is a practice of JavaScript.';
console.log(sentence.slice(15, 18)); 
console.log(sentence.substring(22, 26)); 

let str1 = 'JavaScript';
let str2 = 'Practice classes';
console.log(str1.concat(' ',str2)); 


let phrase = 'Anand Sir Birthday party was so fun!';
let words = phrase.split(' '); 
console.log(words); 
console.log(words.join('-')); 


let paddedText = '   Trim this text.     ';
console.log(paddedText.trim()); 


let sentence1 = 'JavaScript is awesome!';
console.log(sentence1.replace('awesome', 'amazing')); 

// Examples of Array Methods

let arr = [1, 2, 3];
arr.push(4); 
console.log(arr);

let popped = arr.pop();
console.log(popped); 
console.log(arr); 

let numbers = [1, 2, 3];
numbers.unshift(0); 
console.log(numbers); 

let shifted = numbers.shift(); 
console.log(shifted); 
console.log(numbers);


let fruits = ['apple', 'banana', 'cherry', 'date'];
fruits.splice(2, 1, 'grape'); 
console.log(fruits); 

let removed = fruits.splice(1, 2); 
console.log(removed); 
console.log(fruits); 

let colors = ['red', 'green', 'blue', 'yellow', 'orange'];
let sliced = colors.slice(1, 4); 
console.log(sliced); 
console.log(colors); 

let numbers1 = [1, 2, 3];
numbers1.forEach(function(item, index) {
  console.log(`Item at index ${index}: ${item}`);
});

let nums = [1, 2, 3];
let doubled = nums.map(function(num) {
  return num * 2;
});
console.log(doubled); 



//Object Methods Examples

let car = {
    brand: 'Toyota',
    model: 'Camry',
    year: 2020,
    //color:'White'
  };
  
  let keys = Object.keys(car);
  console.log(keys); 

  let values = Object.values(car);
  console.log(values); 


  let entries = Object.entries(car);
  console.log(entries); 

console.log(car.hasOwnProperty('model')); 
console.log(car.hasOwnProperty('color')); 

let carDetails = { color: 'blue', price: '$25,000' };
Object.assign(car, carDetails); 
console.log(car); 

let frozenObj = Object.freeze(car); 
car.model = 'Corolla'; 
console.log(car); 

let newCar = Object.create(car); 
console.log(newCar.brand); 



// Math Methods examples

let max = Math.max(5, 10, 2, 8); 
console.log(max); 

let min = Math.min(5, 10, 2, 8); 
console.log(min); 

let round = Math.round(5.3); 
console.log(round);

let floor = Math.floor(5.8); 
console.log(floor); 

let ceil = Math.ceil(5.1); 
console.log(ceil); 

let absolute = Math.abs(-10); 
console.log(absolute); 

let squareRoot = Math.sqrt(25); 
console.log(squareRoot); 

let power = Math.pow(2, 3);
console.log(power); 


let random = Math.random();
console.log(random); 

//examples of Date Methods 

let currentDate = new Date(); 
console.log(currentDate);

let specificDate = new Date('2023-12-25'); 
console.log(specificDate);

let timestamp = new Date(1638451200000); 
console.log(timestamp);

let date = new Date();
console.log(date.getFullYear()); 
console.log(date.getMonth()); 
console.log(date.getDate()); 
console.log(date.getDay()); 
console.log(date.getHours()); 
console.log(date.getMinutes()); 
console.log(date.getSeconds()); 
console.log(date.getMilliseconds()); 

let date1 = new Date();
date.setFullYear(2023);
date.setMonth(11); 
date.setDate(31);
console.log(date1);

let date2 = new Date();
console.log(date2.toDateString()); 
console.log(date2.toTimeString());
console.log(date2.toLocaleDateString()); 
console.log(date2.toLocaleTimeString()); 

let startTime = new Date();
let endTime = new Date();
let timeDifference = endTime - startTime; 
console.log(`Time taken: ${timeDifference} milliseconds`);

//examples of Other Global Methods 

console.log(isNaN('Hello'));
console.log(isFinite(10 / 0)); 

console.log(parseInt('123')); 
console.log(parseFloat('3.14')); 

let encoded = encodeURI('https://www.example.com/?name=John Doe&age=30');
console.log(encoded); 

let decoded = decodeURI(encoded);
console.log(decoded); 

let person = { name: 'John', age: 30, city: 'New York' };
let jsonString = JSON.stringify(person); 
console.log(jsonString);

let parsedObject = JSON.parse(jsonString); 
console.log(parsedObject);


// setTimeout() executes a function once after a specified delay (in milliseconds)
setTimeout(function() {
    console.log('Delayed execution after 2 seconds');
  }, 2000);
  
  // setInterval() executes a function repeatedly at specified intervals (in milliseconds)
  let counter = 0;
  let interval = setInterval(function() {
    console.log(`Interval ${counter}`);
    counter++;
    if (counter === 5) {
      clearInterval(interval); // Stops the interval after 5 iterations
    }
  }, 1000);
  