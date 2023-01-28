# Informacion de los datos

Data Set Information:

These data are the results of a chemical analysis of wines grown in the same region in Italy but derived from three different cultivars. The analysis determined the quantities of 13 constituents found in each of the three types of wines.

I think that the initial data set had around 30 variables, but for some reason I only have the 13 dimensional version. I had a list of what the 30 or so variables were, but a.) I lost it, and b.), I would not know which 13 variables are included in the set.

The attributes are (dontated by Riccardo Leardi, riclea '@' anchem.unige.it ) 1) Alcohol 2) Malic acid 3) Ash 4) Alcalinity of ash 5) Magnesium 6) Total phenols 7) Flavanoids 8) Nonflavanoid phenols 9) Proanthocyanins 10) Color intensity 11) Hue 12) OD280/OD315 of diluted wines 13) Proline

In a classification context, this is a well posed problem with "well behaved" class structures. A good data set for first testing of a new classifier, but not very challenging.

# Ejecución del proyecto en Google Colab

Ejecuta el proyecto en google colab para realizar el analisis descriptivo, modelado y guardado de modelo.


# Despliegue de modelo en FastAPI

1. situarse en la carpeta despliegue_FastAPI
```sh
cd despliegue_FastAPI
```
2. Crear dentro de la carpeta despliegue_FastAPI el ambiente virtual con las version 3.8.10 de python y activarlo.

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
3. Instalar las librerias necesarias
```sh
pip install -r requirements.txt
```
4. Lanzar la aplicación: 
```sh
uvicorn main:app --reload
```

5. Probar la palicación en local por el puerto 8000
```sh
http://localhost:8000/docs

```

# Screenshot

![image](https://github.com/EdFlo15/Geocoding-API-Google/img/img1.png)