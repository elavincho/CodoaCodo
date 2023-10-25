//Me creo la variable miHeader y pegamos el código que tenemos en el HTML
let miHeader=`
    <h1>Rick and Morty</h1>
    <nav>
        <a class="aheader" href="index.html">Inicio</a>
        <a class="aheader" href="nosotros.html">Nosotros</a>
        <a class="aheader" href="sucursales.html">Sucursales</a>
        <a class="aheader" href="#contacto">Contacto</a>
    </nav>
`

document.querySelector("header").innerHTML=miHeader;

