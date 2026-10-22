// 5. Eliminar duplicados
// Dado un array, crea otro array que contenga los mismos elementos pero sin elementos repetidos.
let numeros = [1, 2, 2, 3, 4, 4, 5];

let numerosSinDup = [];

for (let i = 0; i < numeros.length; i++) {
  if (!numerosSinDup.includes(numeros[i])) {
    numerosSinDup.push(numeros[i]);
  }
}

console.log(numerosSinDup);
