// 1. Fibonacci
// Crea una función que reciba un número n y muestre los primeros n números de la secuencia de Fibonacci.

let previousNumber = 0;
let nextNumber = 0;
let newNumber = 0;

function Fibonnaci(number) {
  for (let i = 0; i < number; i++) {
    if (i == 0) {
      console.log(i);
      previousNumber = i;
    } else if (i == 1) {
      console.log(i);
      nextNumber = i;
    } else {
      newNumber = previousNumber + nextNumber;
      //   if (i == number - 1) {
      //     console.log("Estoy sumando = " + previousNumber + "y" + nextNumber);
      //   }
      console.log(newNumber);
      previousNumber = nextNumber;
      nextNumber = newNumber;
    }
  }
}

// Fibonnaci(5);
Fibonnaci(8);

//vuelta 1 => 0 + 0 = 0, previous numvber = 0
//vuelta 2 => 1 + 0 = 1, previous number = 1

//? aca no tengo que sumar el siguiente valor de 1 sino que solo los dos anteriores

//vuelta 3=> 2+1 = 3, prevopus number = 2
//vuelta 4 => 3+2 = 5, prevous number = 3
//vuelta 5 => 4+3 = 7, prevous number = 4
