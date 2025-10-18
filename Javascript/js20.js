// write a program to interchange first and last elements in a array?

arr = [4, 5, 6, 7, 8, 9, 9, 4, 5, 6, 7]
function swap_array(arr) {
  // let size = arr.length;
  temp = arr[0];
  arr[0] = arr[arr.length - 1];
  arr[arr.length - 1] = temp;
  return arr;
}

console.log(swap_array(arr));

// function swap_array(arr) {
//   arr[0], arr[arr.length-1] = arr[arr.length-1],arr[0];
//   return arr;
// }

// console.log(swap_array(arr));
