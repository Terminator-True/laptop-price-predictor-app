import pickle
import numpy as np

class Prediction:
    
    marca:int
    inches:float
    cpu:int
    ram:int
    gpu:int
    so:int
    ssd:int
    
    def __init__(self, marca, inches, cpu, ram, gpu, so, ssd) -> None:
        self.marca = marca
        self.inches = inches
        self.cpu = cpu
        self.ram = ram
        self.gpu = gpu
        self.so = so
        self.ssd = ssd
        self.cpus = [
            'low gamma intel processor',
            'low gamma amd processor',
            'intel core i5',
            'intel core i7',
            'intel core i9',
            'amd ryzen 5',
            'amd ryzen 7',
            'amd ryzen 9'
            'Mac Processor',
        ]
        self.gpus = [
            'Nvidia High gamma',
            'Nivida medium gamma',
            'Nvidia low gamma',
            'Other nvidia grafic card',
            'integrated graphics',
            'Other nvidia grafic card',
            'Apple integrated graphics',
            'Amd low Gamma',
            'Amd High gamma'
        ]
        self.marcas = [
            "Lenovo",
            "Asus",
            "HP",
            "MSI",
            "Acer",
            "Apple",
            "Alurin",
            "Dell",
            "Microsoft",
            "PcCom",
            "Gigabyte",
            "Medion",
            "Razer",
            "LG",
            "Samsung",
            "Vant",
            "Vanwin",
            "Denver",
            "Primux",
            "Deep Gaming",
            "Dynabook Toshiba",
            "Prixton",
            "Innjoo",
            "Realme",
            "Huawei",
            "Thomson",
            "Jetwing",
            "Toshiba"
        ]
        self.sos = [
            'No Os/ Linux',
            'Windows'
        ]
    def get_cpu(self):
        return self.cpus[self.cpu]
    
    def get_gpu(self):
        return self.gpus[self.gpu]
    
    def get_so(self):
        if self.marca == 'Apple':
            return 'MacOs'
        return self.sos[self.so]
    def get_marca(self):
        return self.marcas[self.marca]
    
    def do_prediction(self):
        #TODO Call to prediction model
        pipe = pickle.load(open('backend\ML_model\pipe_main.pkl','rb'))
        query = np.array([
            self.get_marca(),
            self.inches,
            self.get_cpu(),
            self.ram,
            self.get_gpu(),
            self.get_so(),
            self.ssd], dtype=object)
        query = query.reshape(1,7)
        return int(np.exp(pipe.predict(query)[0]))
    
if __name__ == '__main__':
    prediction = Prediction(0,15.6,0,32,0,0,2000)
    print(prediction.do_prediction())