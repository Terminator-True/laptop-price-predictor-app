<script>
import { Motion } from "@oku-ui/motion"

export default {
    components:{
        Motion
    },
    props:{
        placeholder:String,
        id:String,
        modelValue:Number
    },
    emits: ['update:modelValue']
}
</script>

<template>
    <Motion 
        class="box"
        :initial="{ opacity: 0, scale: 0 }"
        :animate="{ opacity: 1, scale: 1 }"
        :transition="{ duration: 0.5 }"
    >
        <input
            type="number"
            :id="id"
            class="w-full px-2 py-2 text-sm duration-300 border rounded outline-none text-primary-black/50 placeholder:text-primary-black/50"
            :placeholder="placeholder"
            :value="modelValue"
            @input="$emit('update:modelValue', $event.target.value)"
        />
    </Motion>

</template>