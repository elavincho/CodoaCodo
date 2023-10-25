const { createApp } = Vue
createApp({
    data() {
        return {
            nombre: '',
            apellido: '',
            edad: '',
            cursos: [
                { nro: 1, nombre: 'HTML' },
                { nro: 2, nombre: 'CSS' },
                { nro: 3, nombre: 'VUE' },
                { nro: 4, nombre: 'JS' }
            ],
            modulo: 'Front-end'
        }
    }
}).mount('#ejemplo')

