<template>
    <app-navigator></app-navigator>
</template>

<script>
    import {
        createAppContainer,
        createStackNavigator,
    } from "vue-native-router";

    import LoginScreen from "../components/screens/Login.vue";
    import HomeScreen from "../components/screens/Home.vue";

    const StackNavigator = createStackNavigator(
        {
            Login: LoginScreen,
            Home: HomeScreen,
        },
        {
            initialRouteName: 'Login',
        }
    );

    const AppNavigator = createAppContainer(StackNavigator);

    export default {
        components: { AppNavigator },
    }
</script>