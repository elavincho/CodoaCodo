/************** OTROS METODOS PARA ARRAYS *****************/

/*slice(inicio, final) retorna la copia de un arreglo desde el índice inicio hasta final, excluyendo el final. No modifica el arreglo original.*/
//https://www.w3schools.com/jsref/jsref_slice_array.asp
//https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice

// const animales = ['araña', 'buey', 'caballo', 'elefante', 'perro']

// console.log("----------------SLICE----------------")
// console.log(animales.slice(2)) // Desde 2 en adelante: ['caballo', 'elefante', 'perro']
// console.log(animales.slice(2, 4)) // Desde 2 hasta 4 (no inclusive): ['caballo', 'elefante']
// console.log(animales.slice(1, 5)) // Desde 1 hasta 5 (no inclusive): ['buey', 'caballo', 'elefante', 'perro']
// console.log(animales.slice(-2)) // Los últimos 2: ['elefante', 'perro']
// console.log(animales.slice(1, -1)) // Desde 1 hasta el último (no inclusive): ['buey', 'caballo', 'elefante']
// console.log(animales.slice()) // Todos los elementos

/*splice realiza operaciones sobre el arreglo, modificándolo. Es muy versátil, y permite tanto quitar elementos como agregarlos*/
//https://www.w3schools.com/jsref/jsref_splice.asp
//https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/splice

// const meses = ['Enero', 'Marzo', 'Abril', 'Otoño', 'Junio']
// console.log("----------------SPLICE----------------")
// meses.splice(1, 0, "Febrero") // Agrega 'Febrero' en posición 1: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Otoño', 'Junio']. El 1 hace referencia a la posición, el 0 me indica que corra los elementos y agregue "Febrero"
// console.log(meses)
// meses.splice(4, 1, "Mayo") // reemplaza 1 elemento en el índice 4: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio']. El 4 hace referencia a la posición, el 1 me indica que pise el contenido y agrega "Mayo"
// console.log(meses)
// meses.splice(2, 1, "Octubre", "Noviembre") // En la posición 2 agrega 2 elementos y elimina 1: ['Enero', 'Febrero', 'Octubre', 'Noviembre', 'Abril', 'Mayo', 'Junio']. El 2 hace referencia a la posición, el 1 me indica que pise el contenido de Marzo por "Octubre" y corre una posición para agregar "Noviembre"  
// console.log(meses)