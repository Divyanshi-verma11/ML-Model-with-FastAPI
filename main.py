from fastapi import FastAPI
from schema import UserInput
import pandas as pd
from models import model
from fastapi.responses import JSONResponse
app = FastAPI()


@app.get("/")
def home():
    return {"message" : "This is the Premium Category prediction category website"}

@app.get("/health")
def health():
    return{
        "Port" : "The Port is 8000 for the fastapi and 8501 for the streamlit",
          "Version" : "1.0.0"
          }
    
@app.post("/predict")
def predict_premium(user: UserInput):
    input_df = pd.DataFrame([{
        "bmi" : user.bmi,
        "age_group" : user.age_group,
        "lifestyle_risk" : user.lifestyle_risk,
        "city_tier" : user.city_tier,
        "income_lpa" : user.income_lpa,
        "occupation" : user.occupation
    }])

    print("INPUT DATA:")
    print(input_df)

    print("DATA TYPES:")
    print(input_df.dtypes)
    prediction = model.predict(input_df)[0]

    return JSONResponse(status_code = 200, content = {"response" : prediction})
    