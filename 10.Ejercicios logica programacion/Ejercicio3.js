let array = ["a", "b", "a", "c", "b", "a"];

let elementos = [];

let NumElementos = [];

let cont = 0;

for (let i = 0; i < array.length; i++) {
  if (!elementos.includes(array[i])) {
    elementos.push(array[i]);
    NumElementos[cont] = 1;
    cont++;
  } else {
    let posicion = elementos.indexOf(array[i]);
    NumElementos[posicion]++;
  }
}

console.log(elementos);
console.log(NumElementos);
