//¿Cómo llegamos a una función?
//Supongamos que tenemos que reproducir por consola la tabla de multiplicar del 5 tres veces:

/*PRIMER EJEMPLO:
  Sin ciclos de repetición y sin funciones (lo hacemos una vez y vemos que estamos escribiendo mucho código):
*/

// console.log("5 x 1 = ", 5 * 1)
// console.log("5 x 2 = ", 5 * 2)
// console.log("5 x 3 = ", 5 * 3)
// console.log("5 x 4 = ", 5 * 4)
// console.log("5 x 5 = ", 5 * 5)
// console.log("5 x 6 = ", 5 * 6)
// console.log("5 x 7 = ", 5 * 7)
// console.log("5 x 8 = ", 5 * 8)
// console.log("5 x 9 = ", 5 * 9)
// console.log("5 x 10 = ", 5 * 10)

/*SEGUNDO EJEMPLO:
  Con ciclos de repetición y sin funciones:
*/

// for (i = 1; i <= 10; i++) {
//     console.log("5 x", i, "=", 5 * i)
// }

/*TERCER EJEMPLO:
  Repetimos el ciclo de repetición tres veces, no usamos funciones:
*/

// // Primera vez
// for (i = 1; i <= 10; i++) {
//     console.log("5 x", i, "=", 5 * i)
// }
// // Segunda vez
// for (i = 1; i <= 10; i++) {
//     console.log("5 x", i, "=", 5 * i)
// }
// // Tercera vez
// for (i = 1; i <= 10; i++) {
//     console.log("5 x", i, "=", 5 * i)
// }

/*CUARTO EJEMPLO:
  Declaramos una función y la llamamos 3 veces:
*/

//Declaración de la función tablaDelCinco()
// function tablaDelCinco(){
//     for (i = 1; i <= 10; i++){
//         console.log("5 x", i, "=", 5 * i)
//     }
//   }

// //Bucle que ejecuta 3 veces la función tablaDelCinco()
// for (let i = 1; i <= 3; i++) {
//     tablaDelCinco()
// }
