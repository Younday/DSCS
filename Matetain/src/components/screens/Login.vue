<template>
    <nb-form>
        <nb-item>
            <nb-input placeholder="Username" />
        </nb-item>
        <nb-item last>
            <nb-input placeholder="Password" />
        </nb-item>
        <nb-button
          :on-press="loginAction"
        >
            <nb-text>Submit</nb-text>
        </nb-button>
    </nb-form>
</template>

<script>
    export default {
        name: "Login",
        props: {
            navigation: {
                type: Object
            }
        },
        methods: {
            loginAction() {
                console.log('test 12');
                this.navigation.navigate('Home')
            }
        }
    }
</script>

<style scoped>

</style>