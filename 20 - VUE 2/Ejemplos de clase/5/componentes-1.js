//********************************** Ejemplo 1
const CustomComponent1 = {
    template:   `<div>
                    <h1 class="rojo">Otro titulo</h1>
                    <h1 class="rojo">Primer componente personalizado</h1>
                </div>`
}


const ej1 = Vue.createApp({
    components: {
        'componente-personalizado-1': CustomComponent1
    }
}).mount("#ejemplo1")



//********************************** Ejemplo 2
const CustomComponent2 = {
    template:   `<div>
                    <h2>{{buttonText}}</h2>
                    <p> Mi nombre es {{ nombre }} y mi edad es {{ edad }} años </p>
                </div>`,
    data() {
        return {
            'buttonText': "Componente Personalizado en Vue.JS 3",
            'nombre': "Moni Argento",
            'edad': 48
        }
    }
}









const ej2 = Vue.createApp({
    components: {
        'componente-personalizado-2': CustomComponent2
    }
}).mount("#ejemplo2")



//********************************** Ejemplo 3
const CustomComponent3 = {
    template: `<div v-on:mouseover = "cambiarNombre();" v-on:mouseout = "reestablecerNombre();">
                    <h1>Componente creado por {{nombre}}</span></h1>
                </div>`,
    data(){
        return{
            nombre: "Pepe"
        }
    },
    methods: {
        cambiarNombre() {
            this.nombre = "Maria Elena"
        },
        reestablecerNombre() {
            this.nombre = "Paola"
        }
    }
}

const ej3 = Vue.createApp({
    components: {
        'componente-personalizado-3': CustomComponent3
    }
}).mount("#ejemplo3")

