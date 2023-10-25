/************ FUNCIONES DE TIPO FLECHA ***************/

// // Función tradicional 
// function cuadrado(x){ 
//     return x**x
// }
// //Ejecución
// console.log(cuadrado(5))

// // Función Arrow: un parámetro. La X es el parámetro
// var aCuadrado = x => x**x //Declaración
// console.log(aCuadrado(5)) //Ejecución

/*---------------------------------------------------------*/
//Función tradicional 
// function multiplicar (num1,num2) {
//     producto= num1*num2
//     return producto
// } 
// console.log(multiplicar(2,3))

// // Función Arrow: más de una línea y con 2 parámetros (num1,num2)
// var aMultiplicar = (num1,num2) => 
// {   
//     producto= num1*num2
//     return producto
// }  //Declaración

// console.log(aMultiplicar(6,7))  //Ejecución

/* ¿CÓMO CONVERTIMOS UNA FUNCIÓN TRADICIONAL EN UNA FUNCIÓN FLECHA? */
// function cubo(a){
//     return a*a*a
// }

// //Paso 1: Eliminar la palabra "function" y coloco un = a la derecha del nombre. Colocar la flecha entre el argumento y las llaves de apertura.
// cubo = (a) => {
//     return a*a*a
// }

// //Paso 2: Quitar los llaves{} del cuerpo y la palabra "return" (el return está implícito).
// cubo = (a) => a*a*a

// //Paso 3: Suprimir los paréntesis de los argumentos
// var cubo = a => a*a*a

// // console.log(cubo(3)) //27