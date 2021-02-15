<template>
    <nb-content padder>
        <nb-form>
            <nb-item :error="(!$v.emailValue.required || !$v.emailValue.email ) && $v.emailValue.$dirty">
                <nb-input placeholder="Email" v-model="emailValue" auto-capitalize="none" :on-blur="() => $v.emailValue.$touch()"/>
            </nb-item>
            <nb-item last :error="!$v.password.required && $v.password.$dirty">
                <nb-input placeholder="Password" v-model="password" auto-capitalize="none" secure-text-entry :on-blur="() => $v.password.$touch()" />
            </nb-item>
        </nb-form>
        <view :style="{marginTop:10}">
            <nb-button block :on-press="login">
                <nb-spinner v-if="logging_in" size="small" />
                <nb-text>Login </nb-text>
            </nb-button>
        </view>
    </nb-content>
</template>

<script>
    import { Dimensions, Platform, AsyncStorage } from "react-native";
    import store from '../../../store';
    import { required, email } from 'vuelidate/lib/validators'
    import { Toast } from 'native-base';
    import { NavigationActions } from 'vue-native-router';

    export default {
        name: "Login",
        props: {
            navigation: {
                type: Object
            }
        },
        data: function() {
            return {
                emailValue: '',
                password: '',
                loaded: false
            };
        },
        computed: {
            logging_in () {
                return store.state.logging_in;
            }
        },
        validations: {
            emailValue: {
                required,
                email
            },
            password: {
                required
            }
        },
        created() {
            AsyncStorage.getItem('email').then((val) => {
                if (val) {
                    this.loaded = true
                    this.navigation.navigate('Home')
                    store.dispatch('SET_USER', {userObj: {email: val}})
                } else {
                    this.loaded = true
                }
            })
        },
        methods: {
            login() {
                if (this.emailValue && this.password && !this.$v.emailValue.$invalid) {
                    store.dispatch('LOGIN', {
                        userObj: {email: this.emailValue},
                        navigate: this.navigation.navigate
                    });
                } else {
                    Toast.show({
                        text: 'Invalid Email or Password',
                        buttonText: 'Okay'
                    })
                }
            }
        }
    }
</script>

<style scoped>

</style>