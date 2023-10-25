const ejemplo1 = Vue.createApp({
    methods: {
        addText() {
            const text          = this.$refs.text.value
            const textField     = this.$refs.textField
            textField.innerHTML = `${textField.innerHTML}<br>${text}`
        },
        deleteText() {
            const textField     = this.$refs.textField
            textField.innerHTML = ""
        }
    }
}).mount("#ejemplo1")


