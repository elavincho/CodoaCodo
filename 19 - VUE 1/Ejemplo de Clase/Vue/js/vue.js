//Objeto de tipo Vue
const { createApp } = Vue

createApp({ //Acá le voy a asignar las propiedades

    data(){
        return{
            mensaje: "Hola mundo con VUE",
            comision: 23523,
            dia: "martes",

            //V-text
            desarrollador: "Evan You",
            anio: 2014,

            //v-html
            subtitulo: '<h2 class="naranja">Este es un subtitulo agregado con v-html</h2>',

            //v-bind
            foto: 'img/logo_vue.png',
            url: 'https://vuejs.org',

            //v-show
            mostrar: true, //False lo oculto, Show lo muestra
        }
    }




}).mount('#app')

