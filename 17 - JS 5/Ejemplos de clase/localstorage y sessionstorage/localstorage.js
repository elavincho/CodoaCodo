// LocalStorage
// El objeto localStorage almacena datos sin fecha de vencimiento.

//El navegador soporta esta función?
if (typeof(Storage) !== "undefined") {
    // setItem guarda datos en el dispositivo
    localStorage.setItem("apellido", "Perez") // No existe, lo agrega. 
    localStorage.setItem("apellido", "Pérez") // Existe, lo reemplaza
    localStorage.setItem("nombre", "Juan")
    console.log("Datos guardados.")

    // getItem recupera datos del dispositivo
    ape = localStorage.getItem("apellido")
    nom = localStorage.getItem("nombre")
    console.log(ape + ", " + nom)
} else {
    console.log("Web Storage no soportado.")
}