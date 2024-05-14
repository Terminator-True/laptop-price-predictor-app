<script>
export default {
    props: {
        id: String,
        text: String
    }
}
</script>

<template>
    <label class="block text-sm w-fit" :for="id">{{ text }}</label>
</template>