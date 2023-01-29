# Data Set Information

These data are the results of a chemical analysis of wines grown in the same region in Italy but derived from three different cultivars. The analysis determined the quantities of 13 constituents found in each of the three types of wines.

The attributes are (dontated by Riccardo Leardi, riclea '@' anchem.unige.it ) 1) Alcohol 2) Malic acid 3) Ash 4) Alcalinity of ash 5) Magnesium 6) Total phenols 7) Flavanoids 8) Nonflavanoid phenols 9) Proanthocyanins 10) Color intensity 11) Hue 12) OD280/OD315 of diluted wines 13) Proline.
https://archive.ics.uci.edu/ml/datasets/Wine

# Execution in Google Colab

All the process of descriptive analysis, preprocessing, and modeling is done in Google Colab. Open the file Colab_wines.ipynb and then click in the button "Open in Colab" for see all the analyses.

# Deploy the model with FastAPI

this project was execute with version 3.8.10 of python 

1. Clone the repository follow the command: 

```sh
git clone https://github.com/EdFlo15/FastAPI_Wines.git
```

2. Go to the directory "despliegue_FastAPI"
```sh
cd despliegue_FastAPI
```
3. Create inside of despliegue_FastAPI the virtual enviroment with the version 3.8.10 of python and then activate the environment following the command:

On Windows create the virtual enviroment and then activate the environment:
```sh
python -m virtualenv -p="path\Python\Python3.8.10\python.exe" venv
.\venv\Scripts\activate

```
On Linux, create and activate the environment:
```sh
python3 -m venv venv
source venv/bin/activate
```
4. Install the libraries with teh command:
```sh
pip install -r requirements.txt
```
5. Launch the aplication locally with the command:
```sh
uvicorn main:app --reload
```

6. Test the aplication locally on the port 8000
```sh
http://localhost:8000/docs

```
7. Download the test file. You cand find the file in FastAPI_Wines/despliegue_FastAPI/uploads/ and then load in the aplication.

If the file not have the same number of columns the aplication will launch the exeption.


