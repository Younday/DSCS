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
  import React from "react";
  import Vue from "vue-native-core";
  import Vuex from 'vuex'
  import { VueNativeBase } from "native-base";
  import Vuelidate from 'vuelidate';
  import Main from "./src/components/layout/Main";
  import LoginScreen from "./src/components/screens/Login.vue";
  import HomeScreen from "./src/components/screens/Home.vue";
  import Sidebar from "./src/components/layout/Sidebar.vue";
  import {
    createAppContainer,
    createStackNavigator,
    createDrawerNavigator
  } from "vue-native-router";

  const Drawer = createDrawerNavigator(
          {
           Home: {
             screen: HomeScreen
           }
          }, {
            initialRouteName: "Home",
            contentComponent: props => <Sidebar {...props} />
          }
  );

  const StackNavigator = createStackNavigator(
          {
            Login: LoginScreen,
            Drawer: { screen: Drawer }
          },
          {
            initialRouteName: 'Login',
            headerMode: "none"
          }
  );

  const AppNavigator = createAppContainer(StackNavigator);
  Vue.use(VueNativeBase);
  Vue.use(Vuex);
  Vue.use(Vuelidate);

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
