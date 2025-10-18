// Print the required output:
// Input string- 'abcdef'
// Fibonacci series - [1,1,2,3,5,8]
// Output - 20a1b1c2d3e5f8

let s1 = 'abcdef'
let fibo = [1,1,2,3,5,8]
let sum = 0


let new_s = fibo.reduce((a,b) => a+b,0)

for(let i = 0; i< s1.length; i++){
    new_s = new_s + s1[i]+fibo[i]
}
console.log(new_s)












// let new_s = fibo.reduce((a, b) => a + b, 0);

// for (let i=0;i<=s1.length;i++){
//     new_s = new_s+s1[i]+fibo[i]
// }
// console.log(new_s)