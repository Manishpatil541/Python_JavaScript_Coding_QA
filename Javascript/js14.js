// write a program to find the factorial of a given number?

// var number = -1;
// if (number < 0) {
//   console.log('cannot find negative number');
// } else if (number === 0) {
//   console.log(`The factorial of ${number} is 1.`);
// } else {
//   let fact = 1;
//   for (i = 1; i <= number; i++) {
//     fact *= i;
//   }
//   console.log(fact);
// }

// function factorial(num) {
//   var result = num;
//   if (num === 0 || num === 1) return 1;
//   while (num > 1) {
//     num--;
//     result *= num;
//   }
//   return result;
// }
// console.log(factorial(10))

function factorial(n){
  let result = n;
  if(n === 0 || n === 1) return 1;
  while(n>1){
    n--;
    result =  result*n
  }
  return result
}
console.log(factorial(10))