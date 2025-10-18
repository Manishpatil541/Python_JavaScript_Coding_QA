// Write a program to calculate power without using predefined functions
function pow(base, power) {
  var p = 1;
  for (var i = 0; i < power; i++) {
    p *= base;
  }
  return p;
}
console.log(pow(5,5))
