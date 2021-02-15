<template>
  <nb-container>
    <nb-header>
      <nb-left>
        <nb-button transparent>
          <nb-icon name="menu" />
        </nb-button>
      </nb-left>
      <nb-body>
        <nb-title>Matetain</nb-title>
      </nb-body>
      <nb-right />
    </nb-header>
    <app-navigator></app-navigator>
  </nb-container>

</template>

<script>
  import Vue from "vue-native-core";
  import { VueNativeBase } from "native-base";
  import Main from "./src/components/layout/Main";
  import LoginScreen from "./src/components/screens/Login.vue";
  import HomeScreen from "./src/components/screens/Home.vue";
  import {
    createAppContainer,
    createStackNavigator,
  } from "vue-native-router";


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
  Vue.use(VueNativeBase);

  export default {
    components: {AppNavigator, Main }
  }

</script>

<style>
.container {
  background-color: white;
  align-items: center;
  justify-content: center;
  flex: 1;
}
.text-color-primary {
  color: blue;
}
</style>
