/************ FUNCIONES DE 1 PARAMETRO ***************/

// Ejemplo 1: función para saludar al usuario

// Declaración
// function saludarUsuario(miNombre){
//     console.log("Hola " + miNombre) //Contenido de la función
// }

// // Ejecución
// // saludarUsuario("Pepe Argento") //Argumento fijo
// var nombre= prompt("Ingrese su nombre") //Pedimos valores
// saludarUsuario(nombre) //Argumento variable

// ----------------------------------------------------------
// Ejemplo 2: tabla de multiplicar hasta cierto número

// // Declaración
// function tablaMultiplicar(final) {
//     for (let i = 1; i <= final; i++)
//         console.log("1 x", i, "=", 1 * i)
// }

// //Ejecución
// tablaMultiplicar(15)

// -------------------------------------------------------
// Ejemplo 3: tabla de multiplicar de cierto número

// // Declaración
// function tablaMultiplicarDos(numero) {
//     console.log("Tabla del:", numero)
//     for (let i = 1; i <= 10; i++) {
//         console.log(numero + " x " + i + " = " + numero * i)
//     }
// }

// //Ejecución
// // tablaMultiplicarDos(8)
// var t = parseInt(prompt("Ingrese un valor:")) // Pedimos un valor
// tablaMultiplicarDos(t)