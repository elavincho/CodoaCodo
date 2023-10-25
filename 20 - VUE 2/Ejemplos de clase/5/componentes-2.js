//********************************** Ejemplo 1
const ejemplo1 = Vue.createApp({
    data(){
        return{
            vista: 'componente',
            vista2: 'componente-dos'
        }
    },
    components: {
        'componente': {
            template: `<div>
                            <span style = "font-size:2rem;color:green;">
                                Componente dinámico
                            </span>
                        </div>`
                    },
        'componente-dos': {
            template: `<br>
                <a href="https://www.google.com" 
                style="text-decoration:none;color:red;">Ir a Google</a>`
        }
    }
}).mount("#ejemplo1")