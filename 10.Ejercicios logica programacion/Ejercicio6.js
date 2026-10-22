// 6. Número faltante
// Tienes un array con números desde 1 hasta n, pero falta uno.
// Encuentra cuál falta.

let numeros = [1, 2, 3, 5, 6];
let numeros2 = [1, 2, 4, 5, 6, 7];

function NumeroFaltante(numeros) {
  for (let i = 0; i < numeros.length; i++) {
    numeroFaltante = numeros[i] + 1;
    if (numeroFaltante == numeros[i + 1] && i === numeros.length - 1) {
      continue;
    } else {
      console.log("Numero faltante:" + numeroFaltante);
    }
  }
}

NumeroFaltante(numeros);
// NumeroFaltante(numeros2);
