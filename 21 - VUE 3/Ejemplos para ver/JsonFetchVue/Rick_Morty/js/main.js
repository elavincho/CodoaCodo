const app = Vue.createApp({
    data() {
        return {
            personajes: []
        }
    },
    //created():
    // Este método se suele usar para realizar las llamadas API REST, por ejemplo si queremos pintar un array con información que provenga del backend lo que se suele hacer es dentro del created hacer la llamada y almacenar el valor de retorno de una de las variables del data. Como Vue es reactivo, cuando la vista esté cargada se pintará el array.
    created() {
        this.fetchData()
    },


    methods: {
        fetchData() {
            fetch('https://rickandmortyapi.com/api/character/')
                .then(response => response.json())
                .then(data => {
                    this.personajes = data.results
                } )
                .catch( err => {
                    console.error(err)
                })
        }
    }
}).mount("#app")