// write a program to reverse a object?

function reverseObjectIntoArray(obj) {

  var array = [];

  for (var i in obj) {
    array.extend(obj[i]);
  }

  array.reverse();

  return array;

}

console.log(reverseObjectIntoArray({ 1: 'A', 2: 'B', 3: 'C' }))