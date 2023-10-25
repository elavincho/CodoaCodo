//Creamos una función Constructora (Clase)
function Auto(marca, modelo, anioFabricacion, aireAcondicionado) {
    this.marca = marca
    this.modelo = modelo
    this.anioFabricacion = anioFabricacion
    this.aireAcondicionado = aireAcondicionado
    }
 
//Creamos el objeto miAuto del tipo Auto
var miAuto = new Auto('Ford','Focus', 2019, true)

//Creamos el objeto miFurgon del tipo Auto
var miFurgon = new Auto('Renault','Traffic', 2008, false)


//MAIN : Muestro alguna de sus propiedades y métodos
console.log(miAuto.marca,"fue fabricado en el año",miAuto.anioFabricacion)
console.log(miFurgon.marca,"fue fabricado en el año",miFurgon.anioFabricacion)