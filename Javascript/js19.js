// Program for convert given string Input to output string
// Input - I_Am_A_Coder
// Output - i.aM.a.cODER

s = "I_Am_A_Coder";
function modify_string(s) {
  let l = [];
  temp = s.split("_");
  for (let i in temp);
    
  l.push(i[0].toUpperCase()+i[1].toLowerCase())
  console.log(l)
}

console.log(modify_string(s))
