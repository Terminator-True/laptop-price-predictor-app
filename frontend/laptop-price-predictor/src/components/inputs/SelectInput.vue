<script>
import { Motion } from "@oku-ui/motion"

export default {
    components:{
        Motion
    },
    props:{
        name:String,
        id:String,
        options:Array,
        placeholder:String,
        modelValue:String
    },
    emits:['update:modelValue']
}
</script>

<template>
    <Motion 
        class="box"
        :initial="{ opacity: 0, scale: 0 }"
        :animate="{ opacity: 1, scale: 1 }"
        :transition="{ duration: 0.5 }"
        >
            <select 
            :name="name" 
            :id="id" 
            :placeholder="placeholder" 
            class="w-full px-2 py-2 text-sm transition-colors duration-300 bg-white border rounded text-primary-black/50 active:text-primary-black"
            :value="modelValue"
            @change="$emit('update:modelValue', $event.target.value)"
            >
                <option value="" disabled selected hidden class="">{{ placeholder }}</option>
                <option v-for="option in options" :key="option" :value="option.id">{{ option.label }}</option>
        </select>
    </Motion>
  
</template>
