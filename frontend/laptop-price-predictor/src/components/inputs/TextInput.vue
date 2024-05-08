<script>
export default {
    props:{
        placeholder:String,
        id:String
    },
    emits: ['update:modelValue']
}
</script>

<template>
    <input
        :id="id"
        class="w-full px-4 py-2 text-sm transition-colors duration-300 border border-transparent rounded outline-none bg-primary-black/5 focus:border-primary-red placeholder:text-primary-black/50"
        :placeholder="placeholder"
        :value="modelValue"
        @input="$emit('update:modelValue', $event.target.value)"
    />

</template>