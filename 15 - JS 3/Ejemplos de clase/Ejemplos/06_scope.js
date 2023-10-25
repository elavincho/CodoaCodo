/***********************SCOPE*********************/

// let carName = "BMW"
// console.log(carName, "Esto es fuera de la f") // aca no puedo usar la variable carName pq no fue declarada

// function myFunction() {
//     var carName = "Volvo"
//     // aca si puedo usar la variable carName
//     console.log(carName, "Esto es dentro de la f")
// }
// myFunction()


// console.log(carName, "Esto es fuera de la f") // aca no puedo usar la variable carName pq no fue declarada

//--------------------------------------------------//
// //Segundo ejemplo, pero con una variable a nivel global

// var carName2 = "Fiat" //La declaro y la convierto en global
// console.log(carName2) //Aqui si puedo usar carName2

// function myFunction2() {
//     //aqui tambien puedo usar la variable carName2
//     console.log(carName2, "desde la función")
//     //También puedo cambiar su contenido
//     carName2 = "Renault"
//     console.log(carName2, "con un nuevo nombre!")
// }
// myFunction2()

// console.log(carName2,"fuera de la función") // uso la variable fuera de la función

//--------------------------------------------------//
//Tercer ejemplo: variable automáticamente global

// function myFunction3() {
//    carName3 = "Chevrolet"  // variable automáticamente global por no ser declarada como "var" o "let"
//    console.log(carName3, "desde adentro de la función")
// }

// myFunction3() // aquí llamo a la variable carName3

// console.log(carName3, "desde fuera de la función")



// let vs var

var a = 5
var b = 10

if (a === 5) {
    let a = 4 // El alcance es dentro del bloque if
    var b = 15 // El alcance es global, sobreescribe a 10 ¿qué pasa si es let?

    console.log("a:", a)  // 4, por alcance a nivel de bloque
    console.log("b:", b)  // 15, por alcance global
}

console.log("a:", a) // 5, por alcance global
console.log("b:", b) // 15, por alcance global
