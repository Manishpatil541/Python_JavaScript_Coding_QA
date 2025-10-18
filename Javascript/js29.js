// given a string as your Input, delete any reoccuring character and return new string

// function reoccuringChar(x) {
//   var a = x.split(",");
//   console.log(a)
//   var x2 = [];
//   for (var i in a) if (x2.indexOf(a[i]) == -1) x2.push(a[i]);
//   return x2.join(",");
// }

function reoccuringChar(s) {
  let charArray = s.split("");
  for (let i = 0; i < charArray.length; i++) {
    for (let j = i + 1; j < charArray.length; j++)
      if (charArray[i] == charArray[j]) {
        charArray.splice(j, 1);
        j--;
      }
  }
  return charArray.join("");
}
console.log(reoccuringChar("missed"));
