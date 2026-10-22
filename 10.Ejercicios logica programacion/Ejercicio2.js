// 2. Segundo número más grande
// Dado un array de números, encuentra el segundo número más grande, sin ordenar el array.

let array = [10, 5, 8, 20, 15];

let mayor = array[0];
let mediano = 0;
let posicionActual = 0;

for (let i = 0; i < array.length; i++) {
  if (mayor < array[i + 1]) {
    mayor = array[i + 1];
  }
}

console.log("El numero mayor es:" + mayor);

//?primero sacare el mayor y luego veo como saco el mediano

//la verdad no se como sacar el mediano en un solo ciclo for. el mayor es facil porque comparo un numero con el siguiente pero en el mediano tengo que comparar con el siguiente y con todos los anteriores
for (let i = 0; i < array.length; i++) {
  console.log(array[i]);
  if (array[i] < mayor && array[i] > mediano) {
    mediano = array[i];
  }
}

console.log("El numero mediano es:" + mediano);

//?Tiempo en obtener la solucion: aprox 25 minutos
