
from sklearn.preprocessing import StandardScaler
import pickle
import pandas as pd
from fastapi import HTTPException


def loadModel():
    pickled_model= pickle.load(open('pkl_modelo_SVC.pkl', 'rb'))
    return pickled_model

def preprocess(df):
    modelo=loadModel()
    columns_name=list(modelo.feature_names_in_)
    df.columns=columns_name
    scalerSVC_test=StandardScaler()
    data_test_scaled=scalerSVC_test.fit_transform(df)
    pd_data_test_scaled=pd.DataFrame(data_test_scaled, columns=columns_name)
    return pd_data_test_scaled, modelo
    
def makePrediction(df):
    try:
        df_prediction,model=preprocess(df)
        value_predict=model.predict_proba(df_prediction)
        return value_predict.tolist()
    except:
        raise HTTPException(400, detail="The files is incorrect: The file must have the same number of columns, please see the sample data file")