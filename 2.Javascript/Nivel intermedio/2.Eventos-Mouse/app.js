const button = document.querySelector("button");
const contenedor = document.querySelector(".contenedor");


//EVENTO CLICK
contenedor.addEventListener("click",(e)=>{
  alert("Click en el contenedor");
}); 

//EVENTO DOUBLECLICK
button.addEventListener("dblclick",(e)=>{
  alert("doble click en el boton en el boton");
});

//EVENTO MOUSEOVER
const contenedor2 = document.querySelector(".contenedor2");
contenedor2.addEventListener("mouseover",(e)=>{
  alert("Mouse over en el contenedor2");
});