const ejemploVif = Vue.createApp({
    data() {
        return {
            info: {}
        }
    },
    created() {
        this.fetchData('https://breakingbadapi.com/api/characters')
    },
    methods: {
        fetchData(url) {
            fetch(url)
                .then(response => response.json())
                .then(data => {
                    this.info = data
                })
                .catch(err => {
                    console.error(err);
                })
            
        }
    }
}).mount("#app")


// const app = new Vue({
//     el: "#app",
//     data: {
//         info: {},
//     },
//     created() {
//         this.fetchData('https://breakingbadapi.com/api/characters')
//     },
//     methods: {
//         fetchData(url) {
//             fetch(url)
//                 .then(response => response.json())
//                 .then(data => {
//                     this.info = data
//                 })
//                 .catch(err => {
//                     console.error(err);
//                 })
            
//         }
//     }
// })