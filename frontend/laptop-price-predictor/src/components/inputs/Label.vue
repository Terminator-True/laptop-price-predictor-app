<script>
export default {
    props: {
        id: String,
        text: String
    }
}
</script>

<template>
    <label class="block mb-2 text-sm w-fit" :for="id">{{ text }}</label>
</template>