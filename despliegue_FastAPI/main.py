from fastapi import FastAPI,HTTPException,UploadFile,File
from fastapi.responses import FileResponse

import pandas as pd

from functions.functions import makePrediction
app = FastAPI()

@app.post(
    "/prediction",
    tags=['Model for predict variety of wines'])

async def clasification(
    file:UploadFile=File(...)
):

    """
    Upload a file .xlsx for use the model SVC to prediction. Click on "Try it out" option and then upload the file and finally click on the button "Execute"
    Parameters: None
    Request Body: A file .xlsx with new observations
        
    Return: A file .xlsx with the probability of new observations.
  
    """
    # Restrict the load of files. This aplication omly accept .xlsx
    if file.content_type not in ["application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"]:
        raise HTTPException(400, detail="Invalid document type, the format correct is xlsx")
    file_location = f"uploads/{file.filename}"

    # Save files
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())
    print(f"File {file.filename} saved in path: {file_location}")

    # Read File to process and make prediction with class makePrediction()
    df_load=pd.read_excel(file_location)
    prediccion=makePrediction(df_load)
    pd_prob=pd.DataFrame(prediccion,columns=['prob_variety1','prob_variety2','prob_variety2'])

    df_postload=pd.read_excel(file_location)
    pd_result=pd.concat([df_postload,pd_prob],axis=1)
    pd_result.to_excel("predictions/predictions.xlsx")
    return FileResponse(path="predictions/predictions.xlsx", filename="predictictions.xlsx", 
                        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
