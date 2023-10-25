
// /************** METODOS PARA ARRAYS *****************/
// /* .push(obj1, obj2...): Añade uno o varios elementos al final del array. Devuelve tamaño del array.*/

// var frutas = ["Banana", "Naranja", "Manzana", "Mango"]
// document.write("PUSH <br>")
// document.write(frutas, "<br>")
// frutas.push("Kiwi", "Pera")
// document.write(frutas, "<br>")

// // /* .pop(): Elimina y devuelve el último elemento del array.*/

// document.write("<br><br>POP <br>")
// document.write(frutas, "<br>")
// var frutaEliminada = frutas.pop() //No tiene argumentos
// document.write(frutas)
// document.write("<br> Fruta eliminada: ", frutaEliminada)

// // /*.unshift(obj1, obj2...): Añade uno o varios elementos al inicio del array. */

// var colores = ["Rojo", "Amarillo", "Verde", "Celeste"]
// document.write("<br><br> UNSHIFT <br>")
// document.write(colores, "<br>")
// colores.unshift("Azul", "Naranja")
// document.write(colores, "<br>")

// // /*.shift(): Elimina y devuelve el primer elemento del array.*/

// document.write("<br><br> SHIFT <br>")
// document.write(colores, "<br>")
// var colorEliminado = colores.shift() //No tiene argumentos
// document.write(colores)
// document.write("<br> Color eliminado: ", colorEliminado)

// /* .concat(obj1, obj2...): Concatena los elementos (o elementos de los arrays) pasados por parámetro.*/

// var ciudades = ["Roma", "Madrid"]
// var masCiudades = ["Atenas", "Valencia"]
// var todos = ciudades.concat(masCiudades, "Brasil") //Agrega al array ciudades loe elementos del array masCiudades

// document.write("<br><br> CONCAT <br>")
// document.write(ciudades, "<br>")
// document.write(masCiudades, "<br>")
// document.write(todos, "<br>") 
// todos = todos.concat("Buenos Aires", "Montevideo") //Sobreescribo el array todos con nuevos valores
// document.write(todos, "<br>")

// /*.indexOf(obj, from): Devuelve la posición de la primera aparición de obj desde from.*/

// document.write("<br> INDEX OF <br>")
// var letras = ["A", "B", "C", "D", "E", "B", "B"]
// document.write(letras, "<br>")
// var pos = letras.indexOf("E")
// document.write("E está en la posición: ", pos)

// /*.lastIndexOf(obj, from): Devuelve la posición de la última aparición de obj desde from.*/

// document.write("<br><br> LAST INDEX OF")
// var pos2 = letras.lastIndexOf("B")
// document.write("<br> B está en la posición: ", pos2)
