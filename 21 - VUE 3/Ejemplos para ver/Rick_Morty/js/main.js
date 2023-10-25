const app = new Vue({
    el: "#app",
    data: {
        personajes: []
    },
    created() {
        this.fetchData()
    },
    methods: {
        fetchData() {
            fetch('https://rickandmortyapi.com/api/character/')
                .then(response => response.json())
                .then(data => {
                    this.personajes = data.results;
                } )
                .catch( err => {
                    console.error(err);
                })
        }
    }
});