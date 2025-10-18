// Write a program to check whether a number is palindrome or not ?

// var string = prompt("enrtr a input:")
// const isPalindrome = (string) => {
//     if (string == string.split('').reverse().join('')){
//         console.log("Palindrome")
//     }
//     else{
//         console.log("Not Palindrome")
//     }
// }

// isPalindrome(string)


function isPal(str){
    if (str == str.split().reverse().join()){
        console.log('its palindrome')
    } else {
        console.log('its not palindrome')
    }
}
isPal('vaibhav')
