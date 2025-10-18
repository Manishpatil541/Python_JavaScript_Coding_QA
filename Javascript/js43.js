// find the pair with a given number in a array?

// function sumOfTwo(array, sumNumber) {
//     for (i of array) {
//       for (j of array) {
//           if (i + j === sumNumber) {
//               console.log([i, j])
//           }
//       }
//     }
//   }
//   sumOfTwo([1, 2, 3], 4)

function arraypair(array,sum){
    for (i = 0;i < array.length;i++) {
        var first = array[i];
        for (j = i + 1;j < array.length;j++) {
            var second = array[j];

            if ((first + second) == sum) {
        // alert('First: ' + first + ' Second ' + second + ' SUM ' + sum);
        console.log('First: ' + first + ' Second ' + second);
            }
        }

    }
}

var a = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9];

arraypair(a,7);