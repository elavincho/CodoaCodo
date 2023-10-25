//Creamos un objeto utilizando los literales { }
var persona = {
    nombre: "Juan", //variable del objeto
    apellido: "Paz",
    dni: 11223344,
    }

//MAIN : Muestro resultados
console.log(persona) // Imprimo el objeto
console.log(persona.nombre) // Imprimo una propiedad del objeto Juan, su nombre
console.log(persona.dni) // Imprimo una propiedad del objeto Juan, su Dni

//Puedo modificar las propiedades utilizando corchetes
persona['nombre'] = "Pepe"
console.log(persona.nombre) // Imprimo una propiedad del objeto Pepe, su nombre