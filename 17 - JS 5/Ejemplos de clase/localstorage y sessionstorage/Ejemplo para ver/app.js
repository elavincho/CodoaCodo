/*
Fuente: https://youtu.be/DRs6zlwKZ34

localStorage: Almacenamiento local. La información dura hasta que se limpia el caché de nuestro navegador.
sessionStorage: Almacenamiento de sesión. La información dura mientras el navegador o pestaña está abierta.

Ambos permiten agregar, consultar, modificar o eliminar los elementos almacenados.
*/

//sessionStorage
function crear_ss(){
    sessionStorage.setItem("usuario", "Pedro") 
    sessionStorage.setItem("mail", "pedro@mail.com") 
}
function mostrar_ss(){
    alert("Usuario: " + sessionStorage.getItem("usuario") + "\nMail: " + sessionStorage.getItem("mail")) 
}
function modificar_ss(){
    sessionStorage.setItem("usuario", "Pedro123") 
    sessionStorage.setItem("mail", "pedro123@mail.com") 
}
function eliminar_ss(){
    sessionStorage.removeItem("usuario") 
    sessionStorage.removeItem("mail") 
}

//localStorage
function crear_ls(){
    localStorage.setItem("usuario", "Ana") 
    localStorage.setItem("mail", "ana@mail.com") 
}
function mostrar_ls(){
    alert("Usuario: " + localStorage.getItem("usuario") + "\nMail: " + localStorage.getItem("mail")) 
}
function modificar_ls(){
    localStorage.setItem("usuario", "Ana123") 
    localStorage.setItem("mail", "ana123@mail.com") 
}
function eliminar_ls(){
    localStorage.removeItem("usuario") 
    localStorage.removeItem("mail") 
}