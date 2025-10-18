// Write a program to print the duplicates present in array?

const arr = [1, 4, 3, 3, 1, 3, 2, 4, 2, 1, 4, 4];
const dupItems = arr => {
   const res = [];
   for(let i = 0; i < arr.length; i++){
      if(arr.indexOf(arr[i]) !== arr.lastIndexOf(arr[i])){
         if(!res.includes(arr[i])){
            res.push(arr[i]);
         };
      };
   };
   return res;
};

const duplicates  = (arr) => {
   let res = []
   for(let i = 0; i<=arr.length;i++){
      if (arr.indexOf(arr[i]) !== arr.lastIndexOf(arr[i])){
         if(!res.includes(arr[i])){
            res.push(arr[i])
         }
      }
   }
   return res
  
}
console.log(duplicates(arr));