//Realice un algoritmo que permita calcular el precio que tiene transportar un paquete de un lugar a otro,  dependiendo de su peso y su lugar de destino, cumpliendo las siguientes condiciones: 
//1. La empresa no transporta paquetes con un peso superior a los 5kg. 
//2. Los precios por kilogramo varía dependiendo del lugar al que se diriga el paquete, los precios son los siguientes: 
//América del Norte 24$ por cada 1kg -- 
//América Central 20$ por cada 1kg --
//América del Sur 21$ por cada 1kg -- 
//Europa 10$ por cada 1kg
//Asia 18$ por cada 1kg

//El mensaje que debe recibir el usuario es el precio del transporte del paquete o dado el caso, que se ha rechazado por exceso de peso.

let peso=Number(prompt("Ingrese peso del cargamento (kg)"));
let lugar=prompt("Ingrese lugar de destino continente");
if (peso>5){
    alert("La empresa no transporta paquetes pesados")
}else if(lugar=="America del Norte"){
    let precio=24*peso
    alert("el precio de envio es"+precio)
}else if(lugar=="America Central"){
    let precio=20*peso
    alert("el precio de envio es"+precio)
}else if(lugar=="America del sur"){
    let precio=21*peso
    alert("el precio de envio es"+precio)
}else if(lugar=="Europa"){
    let precio=10*1
    alert("el precio de envio es"+precio)
}else if(lugar=="Asia"){
    let precio=18*1
    alert("el precio de envio es"+precio)
}