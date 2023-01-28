
from sklearn.preprocessing import StandardScaler
import pickle
import pandas as pd

def cargaModelo():
    pickled_model= pickle.load(open('pkl_modelo_SVC.pkl', 'rb'))
    return pickled_model

def procesamiento(df):
    modelo=cargaModelo()
    columns_name=list(modelo.feature_names_in_)
    df.columns=columns_name
    scalerSVC_test=StandardScaler()
    data_test_scaled=scalerSVC_test.fit_transform(df)
    pd_data_test_scaled=pd.DataFrame(data_test_scaled, columns=columns_name)
    return pd_data_test_scaled, modelo

def realizarPrediccion(df):
    df_prediccion,modelo=procesamiento(df)
    value_predict=modelo.predict_proba(df_prediccion)
    return value_predict.tolist()
