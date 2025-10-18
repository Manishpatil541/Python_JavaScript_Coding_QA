// Write a program to print even values from array?

let arr = [1,2,3,4,5,6,7,8,9,12,13,15]

let even_arr = arr.filter(num => {
    return num % 2 === 0
})
console.log(even_arr)

function even(a){
    let new_arr = []
    for(i=0;i<arr.length;i++){
        if (a[i]%2===0){
            new_arr.push(a[i])
        }
    }
    return new_arr
}
console.log(even(arr))
