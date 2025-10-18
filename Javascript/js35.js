// write a program to find out common letters between two strings?

commonletters = (str1, str2) => {
  let uniqueletter = "";
  for (let i = 0; i < str1.length; i ++) {
    if (uniqueletter.indexOf(str1[i]) === -1) {
      if (str2.indexOf(str1[i]) !== -1) {
        uniqueletter += str1[i];
      }
    }
  }
  return [...uniqueletter];
};

console.log(commonletters('naina','neena'));













// const commonLettres = () => {
//   let x = "vaibhav";
//   let y = "shruthi";
//   let s1 = new Set(x);
//   let s2 = new Set(y);
//   let z = s1 & s2;
//   console.log(z);
// };
// commonLettres();
