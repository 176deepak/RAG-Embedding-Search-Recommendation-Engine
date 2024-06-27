# ------------------ ::IMPORT MODULES, FILES, ETC.:: -----------------------
import os
import orjson
from dotenv import load_dotenv
from fastapi import (
    FastAPI, 
    Response, 
    HTTPException, 
    Depends
    )
from fastapi.security.api_key import APIKeyHeader
from src.pipeline.inference_pipeline import InferenceEpsPipeline
# ---------------------------- ::END:: --------------------------------------


# -------------------------- ::ENV VARIABLES:: ------------------------------
load_dotenv()
INFERENCE_KEY = os.getenv("INFERENCE_KEY")
# ---------------------------- ::END:: --------------------------------------


# ------------------- ::CLASSES INITIALIZATION:: ----------------------------
app = FastAPI()
inference_pls = InferenceEpsPipeline()
api_key_header = APIKeyHeader(name="Authorization", auto_error=False)
# ---------------------------- ::END:: --------------------------------------


# ------------------------------ ::FUNCTION:: -------------------------------
def get_api_key(api_key: str = Depends(api_key_header)):
    if api_key == INFERENCE_KEY:
        return api_key
    else:
        raise HTTPException(status_code=401, detail="Invalid API key")
# ---------------------------- ::END:: --------------------------------------


# ---------------------------- ::ROUTES:: -----------------------------------
@app.get("/home")
def home():
    return {"message": "Serving"}
# ---------------------------- ::END:: --------------------------------------


# ---------------------------- ::APIs:: -------------------------------------
@app.get("/api.v1/embedding/")
def get_vector_ebd(query: str, api_key: str = Depends(get_api_key)):
    ebd = inference_pls.ebd_ep(query)
    if isinstance(ebd, list):
        json_data = orjson.dumps({"embedding": ebd}).decode("utf-8")
        return Response(content=json_data, media_type="application/json")
    
    if ebd == 500:
        raise HTTPException(status_code=500, detail="Error! Server error")


@app.get("/api.v1/products/")
def get_recommendations(query: str, api_key: str = Depends(get_api_key)):
    ebd = inference_pls.ebd_ep(query)
    data = inference_pls.vs_ep(ebd)
    if isinstance(data, list):
        json_data = orjson.dumps(data).decode("utf-8")
        return Response(content=json_data, media_type="application/json")
    if ebd == 500:
        raise HTTPException(status_code=500, detail="Error! Server error")
# ---------------------------- ::END:: --------------------------------------
