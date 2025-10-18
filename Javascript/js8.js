// how many ways we can convert array to objects in js?

// Using Object.assign method
const array = ['fiz', 'buz', 'fizbuz'];
const obj = Object.assign({}, array);
console.log(obj)

// using spread operator
// const arr = ["foo", "boo", "zoo"];
// const obj = {...arr};
// console.log(obj);


// using Object.fromEntries()
// const arr2 = [
//     ['name', 'vibha'],
//     ['age', 25],
//   ];
  
//   const obj1 = Object.fromEntries(arr2);
  
//   console.log(obj1);


// using foreach 
// const arr = ['zero', 'one', 'two'];

// const obj2 = {};

// arr.forEach((element, index) => {
//   obj2['key' + index] = element;
// });

// console.log(obj2);

  