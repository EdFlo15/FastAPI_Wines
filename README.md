# Informacion de los datos

Data Set Information:

The attributes are (dontated by Riccardo Leardi, riclea '@' anchem.unige.it ) 1) Alcohol 2) Malic acid 3) Ash 4) Alcalinity of ash 5) Magnesium 6) Total phenols 7) Flavanoids 8) Nonflavanoid phenols 9) Proanthocyanins 10) Color intensity 11) Hue 12) OD280/OD315 of diluted wines 13) Proline.
https://archive.ics.uci.edu/ml/datasets/Wine

# Ejecución del proyecto en Google Colab

Todo el proceso de análisis descriptivo, procesamiento y modelado se puede realizar en Google Colab abriendo el archvio Colab_wines.ipynb >> open in colab, en donde se genera el modelo para despliegue.

# Despliegue de modelo en FastAPI

1. Clonar el repositorio: 

```sh
git clone https://github.com/EdFlo15/FastAPI_Wines.git
```

2. Situarse en la carpeta despliegue_FastAPI
```sh
cd despliegue_FastAPI
```
3. Crear dentro de la carpeta despliegue_FastAPI el ambiente virtual con la version 3.8.10 de python y activarlo.

En Windows ejecutar y activar:
```sh
python -m virtualenv -p="path\Python\Python3.8.10\python.exe" venv
.\venv\Scripts\activate

```
En linux ejecutar y activar:
```sh
python3 -m venv venv
source bin/activate
```
4. Instalar las librerias necesarias
```sh
pip install -r requirements.txt
```
5. Lanzar la aplicación: 
```sh
uvicorn main:app --reload
```

6. Probar la aplicación en local por el puerto 8000
```sh
http://localhost:8000/docs

```
7. Descargar el archivo de pruebas de la carpeta  FastAPI_Wines/despliegue_FastAPI/uploads/ y cargar a la API.

