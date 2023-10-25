//Creamos un objeto utilizando los literales { }
var perro = {
    nombre: "Milo",
    edad: 12,
    vivo: true,
    color: "Blanco",

    //Métodos
    quienSoy() {return "Soy " + this.nombre},
    ladrar() {return this.nombre + " dice guau!"}
}

//MAIN : Muestro resultados
console.log(perro.nombre,"tiene",perro.edad,"años.")
console.log(perro.quienSoy()) //Muestro el método

if (perro.vivo) {
    console.log(perro.ladrar()) //Muestro el método
}
