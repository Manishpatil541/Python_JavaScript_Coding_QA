// write a program  to find the sum of all items in a object?

let coordinates = {
    x:25,
    y:35,
    z:10,
    h:500,
    w:10
}

// var summed = 0;

// for (var key in coordinates) {
//     summed += coordinates[key];
// };

// console.log(summed)

let sum = 0;
for (let i of Object.values(coordinates)) {
  sum += i;
}

console.log(sum)