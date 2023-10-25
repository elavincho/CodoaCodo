// JavaScript for/in Statement
// https://www.w3schools.com/jsref/jsref_forin.asp
// For in recorre las propiedades de un objeto

// var vec = ["a", "b", "c", "d"]
// console.log(vec)

/* For in recorre el vector entero y me lo muestra uno debajo del otro*/
// for (var i in vec) {
//     console.log(i) //Muestra posiciones
// }

// for (var i in vec) {
//     console.log(vec[i]) //Muestra contenido
// }

// console.log(" ")





// Otro ejemplo con Objetos
// var persona = {
//     nombre: "Ana",
//     apellido: "Paz",
//     edad: 25,
//     dni: 11223366
// }

// var x
// for (x in persona) {
//     console.log(x) //Muestra propiedades
// }

/* Si quiero ver el contenido, recorro las posiciones del objeto */
// for (x in persona) {
//     console.log(x + ": " + persona[x]) //Muestra propiedades y contenido
// }



// JavaScript for/of Statement
// https://www.w3schools.com/jsref/jsref_forof.asp
// Recorre los valores de un iterable.

//Ejemplo 1
// console.log(" ")
// let cad = "hola"
// for (let letra of cad) {
//     console.log(letra)
// }

//Ejemplo 2
// let nombres = ["Juan", "Ana", "Luis"]
// for (let item of nombres) {
//     console.log(item)
// }

// Ejemplo 3
// let numeros = [2, -4, 99, 987, 65]
// for (let elem of numeros) {
//     console.log(elem)
// }



/*la sentencia for in muestra el indice y la propiedad en sí, y la sentencia for of muestra los valores de una colección.*/