<template>
    <nb-container>
        <nb-header>
            <nb-left>
                <nb-button transparent>
                    <nb-icon :name="menu" />
                </nb-button>
            </nb-left>
            <nb-body>
                <nb-title>Matetain</nb-title>
            </nb-body>
            <nb-right />
        </nb-header>
        <nb-content padder>
            <slot></slot>
        </nb-content>
        <nb-footer>
            <nb-footer-tab>
                <nb-button active full>
                    <nb-text>Footer</nb-text>
                </nb-button>
            </nb-footer-tab>
        </nb-footer>
    </nb-container>
</template>

<script>
    export default {
        name: "Main"
    }
</script>

<style scoped>

</style>