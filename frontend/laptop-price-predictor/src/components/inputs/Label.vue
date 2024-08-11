<script>
import { Motion } from "@oku-ui/motion"

export default {
    components:{
        Motion
    },
    props: {
        id: String,
        text: String
    }
}
</script>

<template>
    <Motion 
        class="box"
        :initial="{ opacity: 0, scale: 0 }"
        :animate="{ opacity: 1, scale: 1 }"
        :transition="{ duration: 0.5 }"
    >
        <label class="block text-sm w-fit" :for="id">{{ text }}</label>
    </Motion>
</template>