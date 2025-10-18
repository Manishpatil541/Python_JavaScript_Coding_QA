// # Write a program for string compression?
// # For example given string = nnnnrrrrtttt
// # output should be  = 4n4r4t

const compressString = (str = '') => {
    let res = '';
    let count = 1;
    for(let i = 0; i < str.length; i++){
       let cur = str[i];
       let next = str[i + 1];
       if(cur === next){
          count++;
       }else{
          res += cur + String(count);
          count = 1;
       };
    }
    return res.length < str.length ? res : str;
 };
 const str1 = 'wwwaabbbb';
 console.log(compressString(str1));