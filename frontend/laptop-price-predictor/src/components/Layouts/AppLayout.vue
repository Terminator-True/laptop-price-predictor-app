<script>
import Header from '@/components/headers/Header.vue';
import Footer from '@/components/footers/Footer.vue'
export default {
    components: {
        Header, Footer
    }
}
</script>

<template>
    <div class="z-10 flex flex-col min-h-screen">
        <!-- <Header /> -->
            <!-- <div class="z-10"></div> -->
            <slot>
            </slot>
        <Footer class="mt-auto" />
    </div>

</template>
