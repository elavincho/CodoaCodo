/************** ARRAYS *****************/

/*Acceso a elementos por posición y largo del array*/

// const array = ["a", "b", "c"]
// console.log(array[0]) // 'a'
// console.log(array[2]) // 'c'
// console.log(array[5]) // undefined
// console.log(array.length) // 3


/**************   *****************/
/*Crear, acceder y mostrar elementos*/

// const vector= [1,3,5,8] //0, 1, 2, 3: cantidad de elementos - 1
// const vectorVacio= [] //Vector vacío
// const vectorDos = new Array("a", "b", "c")
// const vectorTres = new Array (1, 5, 10, 15, 20)

// console.log(vector) //Mostramos por consola
// document.write(vector) //Mostramos en el body
// console.log("Vector vacio:", vectorVacio) //Mostramos por consola
// console.log(vectorDos)
// console.log(vectorDos[1]) //Imprime "b"
// console.log(vectorTres[2]) //Imprime 10
// console.log(vectorTres[6]) //Indefinido, no existe la posición 6
// console.log("Último elemento:", vector[vector.length-1]) //Accedemos al último elemento, ya que vector[vector.length] daría indefinido porque arranca desde 0



/**************   *****************/
/*Acceder y mostrar elementos con for*/

// const nombres = ["Juan", "Lucía", "Ana", "Luis"]
// const notas = [8, 7, 10, 4]

// console.log("Nombres y notas:")
// for(i = 0; i < nombres.length; i++){
//     console.log(nombres[i], notas[i])
// }

// document.write("Nombres y notas: <br>")
// for(i = 0; i < notas.length; i++){
//     document.write(nombres[i], ": ", notas[i], "</br>")
// }