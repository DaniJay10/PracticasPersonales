const button = document.querySelector(".button");

button.addEventListener("click", saludar);
function saludar() {
  const nombre = prompt("Ingrese su nombre:");
  alert(`��Hola ${nombre}! Bienvenido a nuestra página web.`);
  button.removeEventListener("click", saludar);
}

//orden de eventos
const button2 = document.querySelector(".button2");
const contenedor = document.querySelector(".contenedor");

contenedor.addEventListener("click",(e)=>{
  alert("Click en el contenedor");
  e.stopPropagation();
},true); //El que tenga el TRUE SE EJECUTARA PRIMERO

button2.addEventListener("click",(e)=>{
  alert("Click en el boton2");
});