from fastapi import FastAPI,HTTPException,UploadFile,File
from fastapi.responses import FileResponse


import pandas as pd

from funciones.funciones import realizarPrediccion
app = FastAPI()

@app.post(
    "/predicciones",
    tags=['Modelo de predicción de variedad de vinos'])


async def clasification(
    file:UploadFile=File(...)
):
    # Restringir la carga de archivos
    if file.content_type not in ["application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"]:
        raise HTTPException(400, detail="Invalid document type, the format correct is xlsx")
    file_location = f"uploads/{file.filename}"

    # Guardado del archivo
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())
    print(f"Archivo {file.filename} guardado en {file_location}")

    # Lectura de archivo para procesar
    df_load=pd.read_excel(file_location)
    prediccion=realizarPrediccion(df_load)
    pd_prob=pd.DataFrame(prediccion,columns=['prob_variety1','prob_variety2','prob_variety2'])

    df_postload=pd.read_excel(file_location)
    pd_result=pd.concat([df_postload,pd_prob],axis=1)
    pd_result.to_excel("predicciones/predicciones.xlsx")
    return FileResponse(path="predicciones/predicciones.xlsx", filename="predicciones.xlsx", 
                        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
