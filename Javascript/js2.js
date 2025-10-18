// Write a Js Program to Find the Second Largest Number in a array?

let arr = [3,4,5,6,7,2]
let arr1 = [2,3,4,5,6,5,4,3,6]

arr1.sort(function(a,b){
    return b-a
})

// console.log(arr1[1])

new_arr = [...new Set(arr)]

new_arr2 = new_arr.sort()
console.log(new_arr2[new_arr2.length-2])


// console.log(arr[arr.length-2])