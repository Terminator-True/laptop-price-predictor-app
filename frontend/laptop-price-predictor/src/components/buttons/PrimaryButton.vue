<script>
import { Motion } from "@oku-ui/motion"

export default {
    components:{
        Motion
    },
    props:{
        placeholder:String,
        id:String,
        modelValue:String
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
    <button class="w-full px-2 py-2 text-sm duration-300 bg-white border border-white rounded outline-none cursor-pointer text-primary-black/50 placeholder:text-primary-black/50">
        <slot></slot>
    </button>
        <input
            type="button"
            :id="id"
            :placeholder="placeholder"
            :value="modelValue"
            @input="$emit('update:modelValue', $event.target.value)"
        />
    </Motion>

</template>