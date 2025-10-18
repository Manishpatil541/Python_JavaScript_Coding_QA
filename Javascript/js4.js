//  Write a program to count no of occurances in a array and convert it to objects?

let lst = [2, 3, 5, 6, 4, 3, 4, 5, 5, 6, 6, 4];

let lst2 = ["a", "b", "ab", "a", "b", "ab", "c"];

// let k = {};

// for (let i of lst) {
//   if (k[i]) {
//     k[i] = ++k[i];
//   } else {
//     k[i] = 1;
//   }
// }

// console.log(k)

let k = {}

for (let i of lst) {
  if (k[i]) {
    k[i] = k[i] + 1
  } else {
    k[i] = 1
  }
}

console.log(k)