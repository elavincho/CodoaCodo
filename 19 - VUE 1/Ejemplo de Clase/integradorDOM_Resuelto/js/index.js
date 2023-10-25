//Creo la variable miInicio

let miInicio=`
<!-- Agrego el botón para mostrar mi personaje favorito -->
<button onclick="mostrarPersonajeFavorito()">Mostrar Personaje Favorito</button>

<div class="contenedor">
`

//For para traer la información de data y mostrarla como tarjetas
for(let elemento of data){

    //Voy iterando y agregando las tarjetas

    miInicio = miInicio +`
    <!-- Pego lo que tengo dentro de la tarjeta 1 del index.html -->
    
    <div class="tarjeta">
        <img src= ${elemento.image} alt="producto">
        <div class="textocard">
            <h2> ${elemento.name} </h2>
            <p> ${elemento.species} </p>
            <p> ${elemento.created} </p>


            <!-- Agrego el botón para usar LocalStorage -->
            <button onclick="guardarLocalStorage('${elemento.name}')">Agregar Personaje Favorito</button>
            
        </div>
    </div>

    
    `
}

miInicio = miInicio + `</div>`

document.querySelector("main").innerHTML=miInicio

//Agrego la función para Guardar de manera local mi personaje Favorito SET
function guardarLocalStorage(personaje){
    localStorage.setItem("personajeFavorito", personaje)
}


//Agrego la función para Mostrar mi personaje Favorito guardado de manera local GET
function mostrarPersonajeFavorito(){
    console.log(localStorage.getItem("personajeFavorito"))
    alert(localStorage.getItem("personajeFavorito"))
}