/************ FUNCIONES QUE DEVUELVEN VALORES ***************/

// Ejemplo 1: función que devuelve un valor

// Declaración
// function sumar(a, b) {
//     return a + b // Devolvemos la suma de a y b al exterior de la función
// }

// // Ejecución
// var num1 = 4, num2 = 6
// var resultado = sumar(num1, num2) // Se guarda 10 en la variable resultado
// console.log("La suma entre "+ num1 +" y "+ num2 +" es: "+ resultado)

// ----------------------------------------------------------
// Ejemplo 2: diferencia entre una función que devuelve un valor y otra que no

// Declaración de f que NO retorna el valor
// function sumarDos(num1, num2){
//     let suma = num1 + num2
//     console.log("La suma es: " + suma)
// }
// // Ejecución
// sumarDos(20,5)

// // Declaración de f que SI retorna el valor
// function sumarTres(num1, num2){
//     let suma = num1 + num2
//     return suma
// }

// // Ejecución
// var n1 = 8, n2 = 6
// // var resultado = sumarTres(n1, n2)
// // console.log("El resultado es: " + resultado)

// console.log("El resultado es: " + sumarTres(n1, n2)) //En la muestra de datos, llamo a la función


// ----------------------------------------------------------
// Ejemplo 3: uso de variable en sustitución del nombre de la función

// Declaración
// var suma = function sumarCuatro(numero1, numero2) {
//     return numero1 + numero2
// }
// // Ejecución
// console.log("Resultado de la suma:", suma(40, 15))

// ----------------------------------------------------------
// Ejemplo 4: función para obtener el valor máximo

// Declaración
// var numeroMaximo = function (valor1, valor2) {
//     if (valor1 > valor2) {
//         return valor1
//     }
//     return valor2
// }

// // Ejecución
// var v1 = parseInt(prompt("Ingrese un número entero"))
// var v2 = parseInt(prompt("Ingrese otro número entero"))
// console.log("El numero máximo es:", numeroMaximo(v1,v2))