// write a program to check if a number is an armstrong number

function armstrong(n) {
  let no = n.toString().split("");
  let realno = n;
  let a = 0;

  for (let i = 0; i < no.length; i++) {
    no[i] = Math.pow(no[i], no.length);
    a += no[i];
  }

  if (a == realno) {
    console.log("Number is armstrong");
  } else if (a != realno) {
    console.log("Number is not armstrong");
  }
}

armstrong(8208);
