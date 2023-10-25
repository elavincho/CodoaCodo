var persona = {
    nombre: "Juan", //variable del objeto. Par variable: valor,
    apellido: "Paz",
    dni: 11223344,
    //Método: es una propiedad más
    nombreCompleto: function () { //Esta variable guarda el resultado de una función
        return this.nombre + " " + this.apellido; //Función anónima
        //El string que devuelve tiene información del propio objeto
    }
};
console.log(persona) // Imprimo el objeto
console.log(persona.nombre) // Imprimo una propiedad del objeto: Juan
console.log(persona.nombreCompleto()) // Imprimo el resultado de una función del objeto: Juan Paz
