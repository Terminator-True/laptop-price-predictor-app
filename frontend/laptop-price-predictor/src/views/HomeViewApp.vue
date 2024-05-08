<script>
import TextInput from '@/components/inputs/TextInput.vue';
import Label from '@/components/inputs/Label.vue';
import SelectInput from '@/components/inputs/SelectInput.vue';
export default {
    components:{
		TextInput, Label, SelectInput
	},
	data(){
		return {
			form:{}
		}
	}
}
</script>

<template>
<div class="flex flex-col justify-center min-h-screen py-6 bg-gray-100 sm:py-12">
	<TextInput id="text" placeholder="Texto de prueba" v-model="form.text"/>
	
</div>
</template>