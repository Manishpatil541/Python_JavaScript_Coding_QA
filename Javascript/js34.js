// write a program count occurance of each character in a string?

function countCharacter(inputString) {
  const returnObject = {};

  for (const character of inputString) {
    if (returnObject.hasOwnProperty(character)) {
      returnObject[character] += 1;
    } else {
      returnObject[character] = 1;
    }
  }
  return returnObject;
}
console.log(countCharacter("ILikeNewIndia"));



function countCharacter (str) {
  let count = {}
  for (let char of str){
    if(count.hasOwnProperty(char)){
      count[char] += 1
    } else {
      count[char] = 1
    }
  }
  return count
}
console.log(countCharacter("ILikeNewIndia"));