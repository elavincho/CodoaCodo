//Creamos un objeto utilizando una clase
class Animal {
    constructor(nombre, edad, mamifero, color) {
        this.nombre = nombre
        this.edad = edad
        this.mamifero = mamifero
        this.color = color
    }
    //Agrego 2 métodos
    caminar(){return this.nombre+ " camina."}
    volar(){return this.nombre+ " vuela."}
}

// Instanciamos dos objetos clase Animal:
var perro = new Animal("Mora", 4, true, "Marron")
var paloma = new Animal("Greta", 6, false, "Blanco")


//MAIN : Muestro alguna de sus propiedades y métodos
console.log(perro.nombre)
console.log(paloma.edad)
console.log(perro.caminar())
console.log(paloma.volar())

//Modificamos propiedades
perro.nombre= "Stimpy"
paloma.edad = 8
console.log(perro) //Mostramos el objeto
console.log(paloma) //Mostramos el objeto

