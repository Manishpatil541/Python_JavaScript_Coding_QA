// find unique elements from an array
let arr = [2,3,4,2,4,3,4,4,34,3,3]

function unique(ar) {
  let items = {}
  ar.forEach((item) => {
    if(!items[item]){
      items[item] = item;
    }
  })
  return Object.values(items)
}
console.log(unique(arr))


// get the list of books in a array
// let bookslist = [
//     {
//       "id":1,
//       "name":"vaibhav",
//       "books":["hdfs","sdfsdf","dfsf"]
//     },
//     {
//       "id":2,
//       "name":"ikbal",
//       "books":["hscdfs","ssddfsdf","ddfsf"]
//     },
//     {
//       "id":3,
//       "name":"john",
//       "books":["hsddfs","sddsfsdf","dfdssf"]
//     },{
//       "id":4,
//       "name":"vibha",
//       "books":["hdsdfs","ssdsdfsdf","dfsdsf"]
//     }
//   ]
  
//   let result = bookslist.reduce((pre,curr) => {
//     return [...pre, ...curr.books]
//   },[])
//   console.log(result)

// #sum of two different size arrays print reqired output
// let a = [2,4,5,6,7]
// let b = [1,3,4]
// let res = [3,7,9,6,7]

// const result = a.map((element,index) => {
//   if(b[index]<a.length){
//     return b[index]+element
//   }else{
//     return element
//   }
// })
// console.log(result)

// duplicate an array
// function duplicate(arr) {
//   return arr.concat(arr);
// }

// duplicate([1, 2, 3, 4, 5]);


// "^[0-9A-Za-z_-]+$"
// /^[ A-Za-z0-9_-.\s]*$/i
// /^[a-zA-Z0-9_]+$/
// /^(?=.*?[A-Za-z0-9-_])?$/g
// /^[a-zA-Z0-9-_]+$/;
// "[A-Za-z0-9_-]+"

// for alphnaumeric with underscore and hypen
// ^[a-zA-Z\d-_]+$
// ^[\w-_]+$
// @"^[\w\-\s]+$"

// /^[ A-Za-z0-9_@./#&+-]*$/

// var regexp = /^[a-zA-Z\d-_]+$/;
// // var regexp = /^[a-zA-Z0-9-_]+$/
// var check = "cadsca47_-";
// if (check.search(regexp) === -1){
//     console.log('invalid'); }
// else
//     {console.log('valid'); }


