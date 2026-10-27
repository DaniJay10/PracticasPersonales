let numeros = [12, 5, 8, 20, 15, 20];

function segundoMayor(numeros) {
  let mayor = -Infinity;
  let segundo = -Infinity;

  for (let i = 0; i < numeros.length; i++) {
    if (numeros[i] > mayor) {
      segundo = mayor;
      mayor = numeros[i];
    } else if (numeros[i] > segundo && numeros[i] < mayor) {
      segundo = numeros[i];
    }
  }

  if (segundo === -Infinity) {
    return "No existe un segundo número distinto";
  }

  return segundo;
}

console.log(segundoMayor(numeros));
