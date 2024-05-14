<script>
import TextInput from '@/components/inputs/TextInput.vue';
import Label from '@/components/inputs/Label.vue';
import SelectInput from '@/components/inputs/SelectInput.vue';
import AppLayout from '@/components/Layouts/AppLayout.vue'
import PrimaryButton from '@/components/buttons/PrimaryButton.vue';

export default {
    components:{
		TextInput, Label, SelectInput, AppLayout, PrimaryButton
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

		<template v-if="paso == 0">
			<div class="p-10 mx-auto rounded-md w-fit">

				<h2 class="text-slate-50"> Introduce las características del portátil que buscas</h2>
					<!-- <SelectInput id="text" placeholder="Texto de prueba" v-model="form.text" class="m-4 text-black" :options="form_data.options"/> -->
					<div class="flex flex-col mt-2">
						
						<Label id="text" text="Ram GigaBytes" class="m-4 text-xl text-white"/>
						
						<TextInput id="text" placeholder="GB de ram del portátil" v-model="form.inches" class="m-4"/>
					
					</div>
					
					<div class="flex flex-col mt-2">
						
						<Label id="text" text="Pulgadas" class="m-4 text-xl text-white"/>
						
						<TextInput id="text" placeholder="Pulgadas de la pantalla" v-model="form.ram" class="m-4"/>
					
					</div>
					
					<div class="flex flex-col mt-2">
						
						<Label id="text" text="Disco duro" class="m-4 text-xl text-white"/>
						
						<TextInput id="text" placeholder="Almacenamiento del GB del SSD" v-model="form.ssd" class="m-4"/>
					
					</div>
				</div>
				
			
		</template>
		<template v-if="paso == 1">
			<div class="p-10 mx-auto rounded-md w-fit">

				<h2 class="text-slate-50"> Introduce las características del portátil que buscas</h2>
					<!-- <SelectInput id="text" placeholder="Texto de prueba" v-model="form.text" class="m-4 text-black" :options="form_data.options"/> -->
					<div class="flex flex-col mt-2">
						
						<Label id="text" text="Marca" class="m-4 text-xl text-white"/>
						
						<SelectInput id="text" placeholder="Marca del portatil" v-model="form.marca" class="m-4"/>
					
					</div>
					
					<div class="flex flex-col mt-2">
						
						<Label id="text" text="Pulgadas" class="m-4 text-xl text-white"/>
						
						<SelectInput id="text" placeholder="Pulgadas de la pantalla" v-model="form.gpu" class="m-4"/>
					
					</div>
					
					<div class="flex flex-col mt-2">
						
						<Label id="text" text="Disco duro" class="m-4 text-xl text-white"/>
						
						<SelectInput id="text" placeholder="Almacenamiento del GB del SSD" v-model="form.so" class="m-4"/>
					
					</div>
				</div>
		</template>
		<div class="flex w-full">
				<PrimaryButton class="mx-auto" @click="paso>0 ? paso--:paso">
					Atrás
				</PrimaryButton>
				
				<PrimaryButton class="mx-auto"  @click="paso<2 ? paso++:paso">
					Siguente
				</PrimaryButton>
				
				
			</div>
	</div>
</template>
