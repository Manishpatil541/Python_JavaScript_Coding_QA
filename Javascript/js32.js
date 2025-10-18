// find the missing number in a list?

const findMissing = num => {
    const max = Math.max(...num); 
    const min = Math.min(...num); 
    const missing = []
  
    for(let i=min; i<= max; i++) {
      if(!num.includes(i)) { 
        missing.push(i); 
      }
    }
    return missing;
  }
  

function missingNumber (num)  {
  let max = Math.max(...num);
  let min = Math.min(...num);
  let m = []
  for(let i = min; i <= max; i++){
    if(!num.includes(i)){
      m.push(i)
    }
  }
  return m;
}
console.log(missingNumber([0,9,10,3,4,5,6,7,8,1]));