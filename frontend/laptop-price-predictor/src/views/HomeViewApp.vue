<script>
import TextInput from '@/components/inputs/TextInput.vue';
import Label from '@/components/inputs/Label.vue';
import SelectInput from '@/components/inputs/SelectInput.vue';
import AppLayout from '@/components/Layouts/AppLayout.vue'
import PrimaryButton from '@/components/buttons/PrimaryButton.vue';
import instance from '@/mod/axiosInstance';

export default {
    components:{
		TextInput, Label, SelectInput, AppLayout, PrimaryButton
	},
	data(){
		return {
			cargando:false,
			result:false,
			predicted_price:0,
			formulario:{},
			form_data:{
				options:[{
					id:0,
					label:'test'
				}],
			},
			form:{},
			paso:0,
			optionsMarcas:[
    {
      "id": 0,
      "label": "Lenovo"
    },
    {
      "id": 1,
      "label": "Asus"
    },
    {
      "id": 2,
      "label": "HP"
    },
    {
      "id": 3,
      "label": "MSI"
    },
    {
      "id": 4,
      "label": "Acer"
    },
    {
      "id": 5,
      "label": "Apple"
    },
    {
      "id": 6,
      "label": "Alurin"
    },
    {
      "id": 7,
      "label": "Dell"
    },
    {
      "id": 8,
      "label": "Microsoft"
    },
    {
      "id": 9,
      "label": "PcCom"
    },
    {
      "id": 10,
      "label": "Gigabyte"
    },
    {
      "id": 11,
      "label": "Medion"
    },
    {
      "id": 12,
      "label": "Razer"
    },
    {
      "id": 13,
      "label": "LG"
    },
    {
      "id": 14,
      "label": "Samsung"
    },
    {
      "id": 15,
      "label": "Vant"
    },
    {
      "id": 16,
      "label": "Vanwin"
    },
    {
      "id": 17,
      "label": "Denver"
    },
    {
      "id": 18,
      "label": "Primux"
    },
    {
      "id": 19,
      "label": "Deep Gaming"
    },
    {
      "id": 20,
      "label": "Dynabook Toshiba"
    },
    {
      "id": 21,
      "label": "Prixton"
    },
    {
      "id": 22,
      "label": "Innjoo"
    },
    {
      "id": 23,
      "label": "Realme"
    },
    {
      "id": 24,
      "label": "Huawei"
    },
    {
      "id": 25,
      "label": "Thomson"
    },
    {
      "id": 26,
      "label": "Jetwing"
    },
    {
      "id": 27,
      "label": "Toshiba"
    }
  			],
			optionsGPUs:[
    {
      "id": 0,
      "label": "Nvidia High gamma"
    },
    {
      "id": 1,
      "label": "Nivida medium gamma"
    },
    {
      "id": 2,
      "label": "Nvidia low gamma"
    },
    {
      "id": 3,
      "label": "Other nvidia grafic card"
    },
    {
      "id": 4,
      "label": "integrated graphics"
    },
    {
      "id": 5,
      "label": "Apple integrated graphics"
    },
    {
      "id": 6,
      "label": "Amd low Gamma"
    },
    {
      "id": 7,
      "label": "Amd High gamma"
    }
  			],
			optionsCPUs: [
    {
      "id": 0,
      "label": "low gamma intel processor"
    },
    {
      "id": 1,
      "label": "low gamma amd processor"
    },
    {
      "id": 2,
      "label": "intel core i5"
    },
    {
      "id": 3,
      "label": "intel core i7"
    },
    {
      "id": 4,
      "label": "intel core i9"
    },
    {
      "id": 5,
      "label": "amd ryzen 5"
    },
    {
      "id": 6,
      "label": "amd ryzen 7"
    },
    {
      "id": 7,
      "label": "amd ryzen 9"
    },
    {
      "id": 8,
      "label": "Mac Processor"
    }
  			],
			optionsSO:[
			{
			"id": 0,
			"label": "No Os/ Linux"
			},
			{
			"id": 1,
			"label": "Windows"
			},
			{
			"id": 2,
			"label": "Apple"
			}
		]

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
	},
	methods:{
		getLabelsFromOptions(data) {
			const getLabelById = (options, id) => {
				const option = options.find(o => o.id === id);
				return option ? option.label : null;
			};

			return {
				cpu: getLabelById(this.optionsCPUs, parseInt(data.cpu)),
				marca: getLabelById(this.optionsMarcas, parseInt(data.marca)),
				gpu: getLabelById(this.optionsGPUs, parseInt(data.gpu)),
				so: getLabelById(this.optionsSO, parseInt(data.so)),
				ram: data.ram,
				inches: data.inches,
				ssd: data.ssd
			};
		},
		async submit(){
			this.cargando = true;
			let config = {
				method:"POST",
				data:this.form
			}
			
			await instance.request('/prediction',config).then((res)=>{
				this.predicted_price = res.data.value
			})
			this.formulario = this.getLabelsFromOptions(this.form);
			console.log(this.formulario);
			setTimeout(() => {
				this.cargando = false;
				this.result = true;
			}, 1500);
		}
	}
}
</script>

<template>
	<div class="flex justify-center align-middle min-h-[70vh] mt-5">


		<div class="content-center col-span-6 bg-white rounded-xl">
			
			<div class="rounded-md type-js headline text-slate-50/20 w-fit">
				<h1 class=" text-slate-600 text-js"> Laptop price predictor 💻</h1>
			</div>
		
		<template v-if="cargando">
			
			<div class="flex items-center justify-center m-4">
				<div class="flex flex-row gap-2">
					<div class="w-4 h-4 bg-blue-700 rounded-full animate-bounce"></div>
					<div class="w-4 h-4 rounded-full bg-blue-700 animate-bounce [animation-delay:-.3s]"></div>
					<div class="w-4 h-4 rounded-full bg-blue-700 animate-bounce [animation-delay:-.5s]"></div>
				</div>
			</div>
		
				
		</template>
		
		<template v-else-if="!cargando && result">
			<div class="flex items-center justify-center m-4">
				<div class="flex flex-col gap-2">
					<table class="m-4 table-auto">
					<thead class="border-b dark:border-white/10 ">
						<tr>
						<th colspan="2">Características escogidas</th>
						</tr>
					</thead>
					<tbody class="border-b dark:border-white/10 ">
						<tr v-for="(value, key) in formulario" :key="key">
							<td>{{ key }}</td>
							<td>{{ value }}</td>
						</tr>
					</tbody>
					</table>

					<p> El precio del portátil configurado sería: {{ predicted_price }} €</p>
				</div>
			</div>
			
		</template>
		
		<template v-else-if="!cargando && !result">
			<template v-if="paso == 0">
				<div class="p-10 rounded-md w-fit md:w-full">

					<div class="w-full">
						<h2 class="text-slate-600 "> Introduce las características del portátil que buscas</h2>
					</div>

					<div class="bg-white/20">

							<!-- <SelectInput id="text" placeholder="Texto de prueba" v-model="form.text" class="m-4 text-black" :options="form_data.options"/> -->
							<div class="flex flex-col mt-2">
								
								<Label id="text" text="Ram GigaBytes" class="m-4 text-xl text-slate-600"/>
								
								<TextInput id="text" placeholder="GB de ram del portátil" v-model="form.ram" class="m-4"/>
							
							</div>
							
							<div class="flex flex-col mt-2">
								
								<Label id="text" text="Pulgadas" class="m-4 text-xl text-slate-600"/>
								
								<TextInput id="text" placeholder="Pulgadas de la pantalla" v-model="form.inches" class="m-4"/>
							
							</div>
							
							<div class="flex flex-col mt-2">
								
								<Label id="text" text="Disco duro" class="m-4 text-xl text-slate-600"/>
								
								<TextInput id="text" placeholder="Almacenamiento del GB del SSD" v-model="form.ssd" class="m-4"/>
							
							</div>
						</div>
					</div>
					
				
			</template>
			<template v-if="paso == 1">
				<div class="p-10 mx-auto rounded-md w-fit">

					<h2 class="text-slate-600 "> Introduce las características del portátil que buscas</h2>
					<!-- <SelectInput id="text" placeholder="Texto de prueba" v-model="form.text" class="m-4 text-black" :options="form_data.options"/> -->
						<div class="flex flex-col mt-2">
							
							<Label id="text" text="Marca" class="m-4 text-xl text-grey"/>
							
							<SelectInput id="text" placeholder="Marca del portatil" v-model="form.marca" class="m-4" :options="optionsMarcas"/>
						
						</div>
						
						<div class="flex flex-col mt-2">
							
							<Label id="text" text="Procesador" class="m-4 text-xl text-slate-600"/>
							
							<SelectInput id="text" placeholder="CPU" v-model="form.cpu" class="m-4" :options="optionsCPUs"/>
						
						</div>
						
						<div class="flex flex-col mt-2">
							
							<Label id="text" text="Targeta gráfica" class="m-4 text-xl text-slate-600"/>
							
							<SelectInput id="text" placeholder="GPU" v-model="form.gpu" class="m-4" :options="optionsGPUs"/>
						
						</div>
					</div>
			</template>
			<template v-if="paso == 2">
				<div class="p-10 mx-auto rounded-md w-fit">

					<h2 class="text-slate-600 "> Introduce las características del portátil que buscas</h2>
						<!-- <SelectInput id="text" placeholder="Texto de prueba" v-model="form.text" class="m-4 text-black" :options="form_data.options"/> -->
						<div class="flex flex-col mt-2">
							
							<Label id="text" text="SO" class="m-4 text-xl text-slate-600"/>
							
							<SelectInput id="text" placeholder="Sistema Operativo" v-model="form.so" class="m-4" :options="optionsSO"/>
						
						</div>
						
						<!-- <div class="flex flex-col mt-2">
							
							<Label id="text" text="Pulgadas" class="m-4 text-xl text-slate-600"/>
							
							<TextInput id="text" placeholder="Inches" v-model="form.inches" class="m-4"/>
						
						</div> -->
						
						
					</div>
			</template>
			<div class="flex w-full">
					<PrimaryButton class="mx-auto" @click="paso>0 ? paso--:paso">
						Atrás
					</PrimaryButton>
					
					<PrimaryButton v-show="paso<=1" class="mx-auto"  @click="paso<=2 ? paso++:paso">
						Siguente
					</PrimaryButton>

					<PrimaryButton v-show="paso>=2" class="mx-auto"  @click="submit">
						Enviar datos
					</PrimaryButton>
					
					
				</div>
		</template>
	</div>
</div>
	
</template>
