// write a program to check leap year or not?

function leapYear(year) {
  return (year % 4 == 0 && year % 100 != 0) || year % 400 == 0;
}

console.log(leapYear(2000))

function Leap(yr) {
  return ((yr % 4 == 0 && yr % 100 != 0) || yr % 400 == 0)
}
console.log(Leap === true ? 'Not Lear Year' : ' Lear Year')