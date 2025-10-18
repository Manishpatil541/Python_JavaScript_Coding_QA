// write a program to extract number from the string?

let str = "you 8954 24 can ent5er max1@%imum $5500 choices of 124buying";
str = str.replace(/[^0-9]/g, "");
console.log(str); 