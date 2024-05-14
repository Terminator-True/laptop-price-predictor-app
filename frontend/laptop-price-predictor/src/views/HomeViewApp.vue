<script>
import TextInput from '@/components/inputs/TextInput.vue';
import Label from '@/components/inputs/Label.vue';
import SelectInput from '@/components/inputs/SelectInput.vue';
import AppLayout from '@/components/Layouts/AppLayout.vue'

export default {
    components:{
		TextInput, Label, SelectInput, AppLayout
	},
	data(){
		return {
			form_data:{
				'options':[{
					id:0,
					label:'test'
				}]
			},
			form:{},
			paso:0
		}
	},
	mounted(){

		function autoType(elementClass, typingSpeed){
		var content = $(elementClass);
		content.css({
			"position": "relative",
			"display": "inline-block"
		});
		content.prepend('<div class="cursor" style="right: initial; left:0;"></div>');
		content = content.find(".text-js");
		var text = content.text().trim().split('');
		var amntOfChars = text.length;
		var newString = "";
		content.text("|");
		setTimeout(function(){
			content.css("opacity",1);
			content.prev().removeAttr("style");
			content.text("");
			for(var i = 0; i < amntOfChars; i++){
			(function(i,char){
				setTimeout(function() {        
				newString += char;
				content.text(newString);
				},i*typingSpeed);
			})(i+1,text[i]);
			}
		},1500);
		}

		$(document).ready(function(){
		// Now to start autoTyping just call the autoType function with the 
		// class of outer div
		// The second paramter is the speed between each letter is typed.   
		autoType(".type-js",200);
		});
	}
}
</script>

<template>
	<div class="flex flex-col mx-auto content-center justify-center max-w-5xl py-6 align-middle min-h-[90vh] sm:py-12">
		
		<div class="p-4 m-2 rounded-md type-js headline text-slate-50 w-fit">
			<h1 class="text-js">Laptop price predictor</h1>
		</div>
		
		<div class="p-10 mx-auto rounded-md w-fit">
			<h2 class="text-slate-50"> Introduce las características del portátil que buscas </h2>
				<SelectInput id="text" placeholder="Texto de prueba" v-model="form.text" class="m-4 text-black" :options="form_data.options"/>
				<TextInput id="text" placeholder="Texto de prueba" v-model="form.text" class="m-4"/>
				<TextInput id="text" placeholder="Texto de prueba" v-model="form.text" class="m-4"/>
				<TextInput id="text" placeholder="Texto de prueba" v-model="form.text" class="m-4"/>
			</div>
		
	</div>
</template>
