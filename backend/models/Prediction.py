class Prediction:
    
    marca:int
    inches:float
    cpu:int
    ram:int
    graphic_card:int
    so:str
    ssd:int
    
    def __init__(self) -> None:
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
        self.graphic_cards = [
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
    def get_cpu(self,cpu_num):
        return self.cpus[cpu_num]
    
    def get_cpu(self,graphic_card_num):
        return self.graphic_cards[graphic_card_num]
    
    def do_prediction(self):
        #TODO Call to prediction model
        pass