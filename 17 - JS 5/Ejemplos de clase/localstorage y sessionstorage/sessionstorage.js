// sessionStorage
// Los datos almacenados en sessionStorage son eliminados cuando finaliza la sesion de navegación (cuando se cierra la página).

//El navegador soporta esta función?
if (typeof(Storage) !== "undefined") {
    // setItem guarda datos en el dispositivo
    sessionStorage.setItem("curso", "Full Stack Python") 

    // getItem recupera datos del dispositivo
    curso = sessionStorage.getItem("curso")
    console.log("recuperado: " + curso)
} else {
    console.log("Web Storage no soportado.")
}