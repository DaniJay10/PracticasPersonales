class Mascota {
    constructor(nombre, tipo, edad) {
        this.nombre = nombre;
        this.tipo = tipo;
        this.edad = edad;
    }


    describir() {
        console.log(`Esta es ${this.nombre}, un ${this.tipo} de ${this.edad} años.`);
    }


    cumplirAnios() {
        this.edad++;
        console.log(`${this.nombre} ha cumplido años y ahora tiene ${this.edad} años.`);
    }
}


const mascota1 = new Mascota("Luna", "perro", 3);
const mascota2 = new Mascota("Miau", "gato", 2);
const mascota3 = new Mascota("Pipo", "conejo", 1);


mascota1.describir();
mascota1.cumplirAnios();

mascota2.describir();
mascota2.cumplirAnios();

mascota3.describir();
mascota3.cumplirAnios();
