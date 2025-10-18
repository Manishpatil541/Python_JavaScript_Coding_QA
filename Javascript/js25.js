// Write a program to count the number of vowels in a string?
let str = "This is a not a binomial distribution Guess the count from this string";

const vowels = 'aeiou';

const countVowel = (str) => {
  let count = 0;
  for (let letter of str.toLowerCase()) {
    if (vowels.includes(letter)) {
      count++;
    }
  }
  return count;
};
console.log(countVowel(str));
