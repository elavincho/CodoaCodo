let header = `
<h1>La cocina de Pepe</h1>
<nav class="navbar navbar-expand-md bg-dark navbar-dark">
  <a class="navbar-brand" href="index.html">Home</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#collapsibleNavbar">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="collapsibleNavbar">
    <ul class="navbar-nav">

      <li class="nav-item">
        <a class="nav-link" href="about.html">Acerca de</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="contact.html">Contacto</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="location.html">Sucursal</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="form.html">Registrarse</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="NuestrosClientes.html">Nuestros Clientes</a>
      </li>
    </ul>
</nav>
`
document.getElementById("idheader").innerHTML = header

let footer = `
    <a class="redsoc" href="https://www.twitter.com" target="_blank"><i class="fa fa-twitter"
        aria-hidden="true"></i></a>
    <a class="redsoc" href="https://www.facebook.com/marcela.cerda.9" target="_blank"><i class="fa fa-facebook"
        aria-hidden="true"></i></a>
    <a class="redsoc" href="https://www.pinterest" target="_blank"><i class="fa fa-pinterest"
        aria-hidden="true "></i></a>
    <a class="redsoc" href="https://www.instagram.com/marcela.ines.cerda/" target="_blank"><i class="fa fa-instagram"
        aria-hidden="true"></i></a>
    <a class="redsoc" href="https://www.linkedin.com/in/marcela-cerd%C3%A1-678b05196/" target="_blank"><i
        class="fa fa-linkedin" aria-hidden="true"></i></a>
    <p>Derechos reservados @2020 </p>
`
document.getElementById("idfooter").innerHTML = footer

const ejemploVif = Vue.createApp({
  data() {
    return {
      recetas: [
        {
          codigo: "1",
          imagen: "imagenes/focaccia.jpg",
          nombre: "Focaccia",
          descripcion: "Es la predecesora de la pizza"
        },
        {
          codigo: "2",
          imagen: "imagenes/goulash.jpg",
          nombre: "Goulash",
          descripcion: "Clasico de la cocina húngara"
        },
        {
          codigo: "3",
          imagen: "imagenes/salmorejo.jpg",
          nombre: "Salmorejo",
          descripcion: "El salmorejo es una crema ácida"
        },
        {
          codigo: "4",
          imagen: "imagenes/seafood.jpg",
          nombre: "Seafood",
          descripcion: "Los mariscos criaturas marinas que puedes comer"
        },
        {
          codigo: "5",
          imagen: "imagenes/seafood.jpg",
          nombre: "Seafood",
          descripcion: "Los mariscos criaturas marinas que puedes comer"
        },
        {
          codigo: "6",
          imagen: "imagenes/seafood.jpg",
          nombre: "Seafood",
          descripcion: "Los mariscos criaturas marinas que puedes comer"
        },
        {
          codigo: "4",
          imagen: "imagenes/seafood.jpg",
          nombre: "Seafood",
          descripcion: "Los mariscos criaturas marinas que puedes comer"
        }
      ],
      clientes: [
        { foto: "imagenes/cl1.jpg" },
        { foto: "imagenes/cl2.jpg" },
        { foto: "imagenes/cl3.jpg" },
        { foto: "imagenes/cl4.jpg" },
        { foto: "imagenes/cl5.jpg" },
        { foto: "imagenes/cl6.jpg" },
      ]
    }
  }
}).mount("#app")