// write a program to find max and min from a array without using predefined functions

function getMinMax(arr) {
  let min = arr[0];
  let max = arr[0];
  let i = arr.length;

  while (i--) {
    min = arr[i] < min ? arr[i] : min;
    max = arr[i] > max ? arr[i] : max;
  }
  return { min, max };
}
let arr = [2, 4, 7, 9, 56, 45, 445, 443, 3456, 54567, 5575545];


console.log(getMinMax(arr));
