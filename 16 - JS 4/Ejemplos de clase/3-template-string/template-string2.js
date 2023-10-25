function suma(a, b) {
    return a + b
}

//Programa principal
var a = Number(prompt("Ingrese un numero a:"))
var b = Number(prompt("Ingrese un numero b:"))

//Mostramos en forma tradicional
console.log("La suma entre " + a + " y " + b + " es: " + suma(a, b))

//Utilizando Template String
console.log(`La suma entre ${a} y ${b} es: ${suma(a, b)}`)

/* Otros ejemplos de template string*/
function fn() {
    return "este es el resultado de la función"
}
console.log(`Hola Mundo: ${fn()}`) // resultado => Hola Mundo: este es el resultado de la función

var usuario = {
    nombre: 'Juan Perez',
    mail: 'juanperez@mail.com'
 }

console.log(`Estás conectado como ${usuario.nombre.toUpperCase()}
(${usuario.mail})`)

var divisa = 'Pesos'
console.log(`Los precios se indican en ${divisa}. Utiliza nuestro conversor para convertir ${divisa} en tu moneda local.`)