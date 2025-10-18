// write a program to remove duplicate values from the array?

// let arr = [1, 2, 4, 5, 6, 7, 3, 2, 3, 4]
let arr = ["apple","mango","apple","orange","mango","mango"]

let newarr = []

// for (i = 0; i < arr.length; i++) {
//     if (!newarr.includes(arr[i])) {
//         newarr.push(arr[i]);
//     }
// }

// console.log(newarr)


// let removearr = () => {
//     return unique = arr.filter(function (item, index) {
//         return arr.indexOf(item) == index;
//     });
// }
// console.log(removearr()) 




for(i = 0; i<=arr.length;i++){
    if(!newarr.includes(arr[i])){
    newarr.push(arr[i])
    }
}
console.log(newarr)
