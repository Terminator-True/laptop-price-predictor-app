
# Laptop Price Predictor

Una aplicación que dados unos parámetros de un portátil. Te generará un precio predecido por Machine Learning

## API Reference
### POST /api/prediction

El endpoint te permite realizar una predicción en base a los datos enviados.

#### Request Body

- raw (application/json)
    

| Parameter | Type | Description |
| --- | --- | --- |
| cpu | number | The CPU id |
| marca | number | The brand id |
| gpu | number | The GPU id |
| so | number | The operating system id |
| ram | number | The RAM value |
| inches | number | The screen size value |
| ssd | number | The SSD value |



## Datos

### CPU

| id  | name                      |  
| --- | ------------------------- |  
| 0   | low gamma intel processor  |  
| 1   | low gamma amd processor    |  
| 2   | intel core i5              |  
| 3   | intel core i7              |  
| 4   | intel core i9              |  
| 5   | amd ryzen 5                |  
| 6   | amd ryzen 7                |  
| 7   | amd ryzen 9                |  
| 8   | Mac Processor              |  


### GPU
Aquí tienes la tabla con los datos adicionales que proporcionaste, con `id` numérico comenzando desde 0 y `name` en lugar de `type`:

| id  | name                          |  
| --- | ----------------------------- |  
| 0   | Nvidia High gamma             |  
| 1   | Nivida medium gamma           |  
| 2   | Nvidia low gamma              |  
| 3   | Other nvidia grafic card      |  
| 4   | integrated graphics           |  
| 5   | Apple integrated graphics     |  
| 6   | Amd low Gamma                 |  
| 7   | Amd High gamma                |  

### Marca

Aquí tienes la tabla con los nuevos datos que proporcionaste, con `id` numérico comenzando desde 0 y `name` en lugar de `type`:

| id  | name                |  
| --- | ------------------- |  
| 0   | Lenovo              |  
| 1   | Asus                |  
| 2   | HP                  |  
| 3   | MSI                 |  
| 4   | Acer                |  
| 5   | Apple               |  
| 6   | Alurin              |  
| 7   | Dell                |  
| 8   | Microsoft           |  
| 9   | PcCom               |  
| 10  | Gigabyte            |  
| 11  | Medion              |  
| 12  | Razer               |  
| 13  | LG                  |  
| 14  | Samsung             |  
| 15  | Vant                |  
| 16  | Vanwin              |  
| 17  | Denver              |  
| 18  | Primux              |  
| 19  | Deep Gaming         |  
| 20  | Dynabook Toshiba    |  
| 21  | Prixton             |  
| 22  | Innjoo              |  
| 23  | Realme              |  
| 24  | Huawei              |  
| 25  | Thomson             |  
| 26  | Jetwing             |  
| 27  | Toshiba             |  

### Sistema Operativo



| id  | name         |  
| --- | ------------ |  
| 0   | No OS/Linux  |  
| 1   | Windows      |  
| 2   | Apple        |  


## Response

La petición devuelve el precio del portátil entrado con anterioridad

#### JSON Schema for Response

``` json
{
  "price":10000
}

 ```
