// # print the required output?
let arry = [1,2,3,4,5]
let cubarray = [1,8,27,64,125]

// let arra=[];
// for(o in arry){
//    arra.push(arry[o]*arry[o]*arry[o])
  

// }
// console.log(arry=arra)

var numbers = [1,2,3,4,5,6,7,8];
numbers.forEach(function(element, index, array){
    array[index] = element* element*element;
});
console.log(numbers);
