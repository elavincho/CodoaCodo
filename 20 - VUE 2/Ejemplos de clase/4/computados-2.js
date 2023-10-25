const ejemplocomputados2 = Vue.createApp({
    data() {
        return {
            productos: [
                // { nombre: "Leche", cantidad: 10 },
                // { nombre: "Café", cantidad: 3 },
                // { nombre: "Azúcar", cantidad: 11 },
                // { nombre: "Té", cantidad: 4 },
                // { nombre: "Arroz", cantidad: 5 }
            ],
            nuevoProducto: '',
            aviso: false,
            total: 0
        }
    },
    methods: {
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
    },
    computed: {
        sumarProductos() {//Muestra sumatoria total de cantidades de frutas.
          this.total = 0;
          for (producto of this.productos) {
            this.total += producto.cantidad; //acumulador
            //this.total = this.total + producto.cantidad; //acumulador
          }
          return this.total;
        }
      }
}).mount('#computados2')