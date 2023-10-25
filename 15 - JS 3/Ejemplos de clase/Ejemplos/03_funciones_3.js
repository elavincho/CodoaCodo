/************ FUNCIONES DE MÁS DE 1 PARAMETRO (MÚLTIPLES) ***************/

// Ejemplo 1: función para calcular la tabla de multiplicar

// // Declaración
// function tablaMultiplicar(numero, hasta) {//¿qué pasa si doy vuelta los parámetros?
//     for (let i = 1; i <= hasta; i++)
//         console.log(numero + " x " + i + " =", numero * i)
// }

// //Ejecución
// tablaMultiplicar(10, 5) // Tabla del 1 (desde el 1 hasta el 10)
// tablaMultiplicar(5, 10) // Tabla del 5 (desde el 1 hasta el 10)

// // ----------------------------------------------------------
// Ejemplo 2: función para saber si una persona es mayor de edad

//Declaración
// function mayoriaEdad(miApellido, miNombre, miEdad){
//     console.log("Apellido y nombre: " + miApellido + ", " + miNombre)
//     if (miEdad >= 18) {
//         console.log(miNombre, "es mayor de edad " + "(" + miEdad + ")")
//     }
//     else {
//         console.log(miNombre, "no es mayor de edad " + "(" + miEdad + ")")
//     }
// }

// //Ejecución
// mayoriaEdad("Argento","Fatiga",5)
// var ape= prompt("Ingrese su apellido")
// var nom= prompt("Ingrese su nombre")
// var edad= parseInt(prompt("Ingrese su edad"))
// mayoriaEdad(ape, nom, edad)


//Parámetros predeterminados
// function multiplicar(a, b = 20) {
//     return a * b
// }
// console.log(multiplicar(5, 2)) // salida: 10
// console.log(multiplicar(5)) // salida: 5