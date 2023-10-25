//Ejemplo 1: contador simple
const ejemplovon1 = Vue.createApp({
    data() {
        return {
            contador: 0
        }
    }
}).mount('#von1')





//Ejemplo 2: uso de métodos
const ejemplovon2 = Vue.createApp({
    data() {
        return {
            frutas: [
                { nombre: "naranja", cantidad: 10 },
                { nombre: "banana", cantidad: 0 },
                { nombre: "durazno", cantidad: 3 }
            ],
            nuevaFruta: ''
        }
    },
    methods: {
        agregarFruta() {
            this.frutas.push({ nombre: this.nuevaFruta, cantidad: 0 })
        }
    }
}).mount('#von2')










//Ejemplo 3: mejorado (temática supermercado) con modificadores de teclas
const ejemplovon3 = Vue.createApp({
    data() {
        return {
            titulo: "Supermercado Noche",
            subtitulo: "Agregando productos",
            productos: [
                { nombre: "Leche", cantidad: 10 },
                { nombre: "Café", cantidad: 3 },
                { nombre: "Azúcar", cantidad: 11 },
                { nombre: "Té", cantidad: 4 },
                { nombre: "Arroz", cantidad: 5 }
            ],
            nuevoProducto: '',
            aviso: false
        }
    },
    methods: {
        agregarProducto(){
            this.productos.push({nombre: this.nuevoProducto, cantidad: 0})
            this.nuevoProducto = ''
        },
        agregarProductoConIf(){
            if (this.nuevoProducto != "") {
                this.productos.push({ nombre: this.nuevoProducto, cantidad: 0})
                this.nuevoProducto = '',
                this.aviso = false
            }
            else {
                this.aviso = true
                alert("Caja de texto vacía")
            }
        }
    }
}).mount('#von3')