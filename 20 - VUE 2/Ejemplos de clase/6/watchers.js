const ejemplo1 = Vue.createApp({
    data(){
        return{
            kilometros: 0,
            metros: 0
        }
    },
    watch: {
        kilometros(val) {
            this.kilometros = val
            this.metros = val * 1000
        },
        metros(val) {
            this.kilometros = val / 1000
            this.metros = val
        }
    }
}).mount("#ejemplo1")

