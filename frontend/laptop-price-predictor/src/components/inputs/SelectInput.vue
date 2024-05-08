<script>
export default {
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

    <select 
    :name="name" 
    :id="id" 
    :placeholder="placeholder" 
    class="w-full px-4 py-2 text-sm transition-colors duration-300 bg-white border rounded focus:border-primary-red text-primary-black/50 active:text-primary-black"
    :value="modelValue"
    @change="$emit('update:modelValue', $event.target.value)"
    >
        <option value="" disabled selected hidden class="">{{ placeholder }}</option>
        <option v-for="option in options" :key="option" :value="option.id">{{ option.label }}</option>
    </select>
</template>
