// 4. Palíndromo
// Crea una función que determine si una palabra se lee igual de izquierda a derecha y de derecha a izquierda.
// "reconocer" → true
// "programacion" → false
// Para empezar, puedes asumir que todas las palabras vienen en minúsculas y sin espacios.

function Palindromo(palabra) {
  let nuevaPalabra = "";

  let palabraMaxima = palabra.length;

  for (let i = palabraMaxima - 1; i >= 0; i--) {
    nuevaPalabra += palabra[i];
  }

  if (palabra == nuevaPalabra) {
    console.log("Es palindromo");
  } else {
    console.log("No es palindromo");
  }
}

Palindromo("reconocer");
Palindromo("programacion");
