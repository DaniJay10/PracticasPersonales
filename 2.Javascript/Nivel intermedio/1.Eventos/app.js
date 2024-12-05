const button = document.querySelector("button");

button.addEventListener("click", saludar);

function saludar() {
  const nombre = prompt("Ingrese su nombre:");
  alert(`��Hola ${nombre}! Bienvenido a nuestra página web.`);
  button.removeEventListener("click", saludar);
}

