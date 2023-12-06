//1
// a.
let user = {};

// b.
user.name = "John";

// c.
user.surname = "Smith";

// d.
user.name = "Pete";

// e.
delete user.name;

//2

let salaries = {
    John: 100,
    Ann: 160,
    Pete: 130
  };
  let sum = 0;
  for (let employee in salaries) {
    sum += salaries[employee];
  }
  console.log(sum);

 
//3

function multiplyNumeric(obj) {
    for (let key in obj) {
      if (typeof obj[key] === 'number') {
        obj[key] *= 2;
      }
    }
  }
  let menu = {
    width: 200,
    height: 300,
    title: "My menu"
  };
  
  multiplyNumeric(menu);
  console.log('My menu')
  
  
  
