// # write a program to convert given input string to output string?
// # input = 'a2b3c4';
// # output = aabbbcccc

// let d;
// let str = "a2b3c4";
// let output = "";
// for (i in str) {
//   if (i.match(/[a-z]/)) {
//     x = i;
//   } else {
//     d = parseInt(i);
//   }
//   output += x.repeat(d);
// }
// console.log(output);

























str = "a2b3cCfg4";
function stingCompression(str) {
  var result = [];

  for (var i = 0; i < str.length; ++i) {
    var curChar = str.charAt(i);

    if (i + 1 < str.length) {
      var nextChar = str.charAt(i + 1);

      var charNum = parseInt(nextChar, 10);

      if (!isNaN(charNum)) {
        curChar = new Array(charNum + 1).join(curChar);

        ++i;
      }
    }

    result.push(curChar);
  }

  return result.join("");
}
console.log(stingCompression(str));
