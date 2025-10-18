// calculate the average of numbers in a given array of numbers?

let arr = [2,4,6,8,10,1,3,5,7,9]
// let avg = arr => arr.reduce((a,b) => a+b)/arr.length
// console.log(avg(arr))

// function avg(arr){
//     var sum = 0
//     arr.forEach(function(item,id){
//         sum += item
//     })
//     return sum/arr.length
// }
// console.log(avg(arr))


let total = 0
for(let i=0;i<arr.length;i++){
    total += arr[i]
}
console.log(total/arr.length)