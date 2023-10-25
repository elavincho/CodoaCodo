const templates={
    home:`
        <div id="home" class="active">
            <h2>Recetas</h2> 
            <p>{{receta}}</p> 
            <p>Ingredientes: {{ingredientes}}</p> 
            <p>Preparacion: {{preparacion}}</p> 
        </div>`,
    about:`
        <div id="about" class="container active">
            <h2> Acerca de nosotros </h2>
            <img v-bind:src="imagen" alt="">
            <p>{{texto}}</p>
        </div>`,
    contact:`
        <div id="contact" class="container active">
            <h2>Contacto</h2>
            <p>Envíame tus sugerenciasde recetas a mi correo: <a :href=  ' "mailto:"+mail'   >{{mail}}</a></p>       
        </div>`,
    clientes:
        `<div id="clientes" class="container active">
            <h2>Clientes</h2>
            <ul>
                <li v-for="cliente in cli">
                   <p>{{cliente.razonSocial}}</p>
                    <p>{{cliente.descripcion}}</p> 
                    <p>{{cliente.direccion}}</p>
                    <img v-bind:src="cliente.logo" alt="logo" > 
                </li>
            </ul>       
        </div>`
}
var app=new Vue({
    el:"#app",
    data: {
        view : 'home',
    },
    components: {
        home: {
            data:function () {      
                return {receta:"Sopa de calabaza",
                        ingredientes:"Calabaza, agua y sal ",
                        preparacion:" Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
                }
            },

            props: [],  //parametros
            template: templates.home
        },
        about: {
            data: function () {return {
                imagen:"https://gourmetdemexico.com.mx/wp-content/uploads/2018/03/descarga.jpg",
                texto:"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.texto:"
            }},
            props: [],
            template: templates.about
        },
        contact: {
            data: function () {return {
                mail:"oscarramos@gmail.com",
            }},

            
            props: [],
            template: templates.contact
        } ,
        clientes: {
            data: function () {return {
                cli:[
                    {razonSocial:"Frávega S.A",
                    logo:"data:image/png;base64,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",
                    descripcion:"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                    direccion:"Corrientes 348 2º Piso ascensor"
                    },
                    {razonSocial:"Rodo S.A",
                    logo:"data:image/jpeg;base64,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",
                    descripcion:"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                    direccion:"Boedo 111 caba"
                    }
                ]
                }
            },   
            props: [],
            template: templates.clientes
        } 
    }

})