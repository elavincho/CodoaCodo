//Para mostrar info
// console.log("Un texto")
// console.log(3*2)
// console.log("Mañana es", 21+1  ,"de septiembre")
// console.log("Mañana es"+ 21+1  +"de septiembre")
// console.info(3)
// console.warn("Texto de alerta")
// console.error("Texto de error")

//Pop-up
// alert("Hola mundo")
document.write("Hola desde JS")

//Otras alternativas
console.log("Este es el número tres:",3)
console.log("Este es el resultado de 3-4:",3-4)
console.log("Este es el resultado de 3+4:",3+4)

//VARIABLES
let alumno = "Damian"
let nota = 9


//CONSTANTES
const entidad = "Buenos Aires Ciudad"
// entidad = "Nación"

console.log(entidad)
console.log("El nombre del alumno es " + alumno + " y su nota es " + nota)

//Identificando los tipos de datos
var dato = 36
console.log(typeof dato)
dato = "Pepe"
console.log(typeof dato)
dato = true
console.log(typeof dato)
dato = (36+4)*2
console.log(typeof dato)
dato = 3.14
console.log(typeof dato)

//Buenas practicas para crear variables
let nombreApellido = "Juan Carlos" //Camelcase 
let User = "Juan Carlos" //Mayuscula
let _usuario
let $usuario
let nombre_apellido = "Snake case"
let NombreApellido = "Pascal case"

//Las variables que NO pueden usarse
// let 1ernombre
// let nombre-apellido
// let var 
// let super 
// let break 
// let this

//Tipos de String
let str1 = "String entre comillas dobles"
let str2 = 'String entre comillas simples'
let str3 = `bactiks`

console.log(str1 + " y " + str2)
let str4 = str1 + " y " + str2
console.log(str4)

//Operaciones básicas
let num1 = parseFloat(prompt("Ingrese el primer número"))
let num2 = parseFloat(prompt("Ingrese el segundo número"))

// console.log(num1 + num2)
let suma = num1 + num2
console.log(suma)

let resta = num1 - num2
console.log(resta)

let multi = num1 * num2
console.log(multi)

let division = num1 / num2
console.log(division)


