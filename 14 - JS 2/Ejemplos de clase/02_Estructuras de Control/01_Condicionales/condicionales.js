/*************** CONDICIONALES: IF ****************/
// var nota = 4
// console.log("Nota:", nota)
// // Condición (si nota es mayor o igual a 5)
// if (nota >= 5) {
//     console.log("¡Estoy aprobado!")
// }
// console.log("Sigue programa...")

/*************** CONDICIONALES: IF/ELSE ****************/
// let nota = 7
// console.log("He realizado mi examen. Mi resultado es el siguiente:")
// // Condición
// if (nota < 5) {
//   // Acción A (True): (nota es menor que 5)
//   calificacion = "desaprobado."
// } else {
//   // Acción B (False): Cualquier otro caso a A (nota es mayor o igual que 5)
//   calificacion = "aprobado."
// }
// console.log("Estoy", calificacion)

// /*Otro ejemplo*/
// let num = parseInt(prompt("Ingrese un número: ", "")) //Pedimos un valor
// if (num > 0) {
//   alert("El número es positivo.")
// } else {
//   alert("El número es cero o negativo.")
// }

// /*************** OPERADOR TERNARIO ****************/
// let nota = 10
// console.log("He realizado mi examen. Mi resultado es el siguiente:")
// // Operador ternario: (condición ? verdadero : falso)
// let calificacion = nota < 5 ? "desaprobado." : "aprobado."
// console.log("Estoy", calificacion)

/*************** IF MULTIPLE ****************/
// let nota = 6
// console.log("He realizado mi examen.")
// nota = parseInt(prompt("Ingrese su nota: ", "")) //Pedimos un valor

// // Condición
// if (nota < 5) {
//   calificacion = "Insuficiente."
// } else if (nota < 6) {
//   calificacion = "Suficiente."
// } else if (nota < 8) {
//   calificacion = "Bien."
// } else if (nota <= 9) {
//   calificacion = "Notable."
// } else {
//   calificacion = "Sobresaliente."
// }
// console.log("He obtenido un", calificacion)

// /*Otro ejemplo*/
// let menu = prompt("Ingrese una opción: \n 1: Abrir programa \n 2: Salir del programa \n 3: Otra opción \n ...etc.: ")
// if (menu == "1") {
//   alert("Bienvenido!")
// }
// else if (menu == "2") {
//   alert("Adiós!")
// }
// else if (menu == "3") {
//   alert("Opción 3")
// }
// else {
//   alert("Ha ingresado una opción inválida!")
// }

/*************** SWITCH ****************/
// let nota = 6
// console.log("He realizado mi examen. Mi resultado es el siguiente:")
// switch (nota) {
//   case 10:
//     calificacion = "Sobresaliente."
//     break
//   case 9:
//   case 8:
//     calificacion = "Notable."
//     break
//   case 7:
//   case 6:
//     calificacion = "Bien."
//     break
//   case 5:
//     calificacion = "Suficiente."
//     break
//   case 4:
//   case 3:
//   case 2:
//   case 1:
//   case 0:
//     calificacion = "Insuficiente."
//     break
//   default:
//     Cualquier otro caso
//     calificacion = "Nota errónea."
//     break
// }
// console.log("Nota:", calificacion)