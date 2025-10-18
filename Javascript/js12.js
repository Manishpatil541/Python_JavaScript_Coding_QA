// write a program for repating first character in a string?

function repeatChar(str) {
    for (let i = 0; i < str.length; i++) {
        // console.log(str.charAt(i))
        // console.log(str.indexOf(str.charAt(i)))
        // console.log(str.lastIndexOf(str.charAt(i)))
      if (str.indexOf(str.charAt(i)) !== str.lastIndexOf(str.charAt(i))) {
        return str.charAt(i)
      }
    }
    return '-1'
  }
console.log(repeatChar('abcdabcd'))