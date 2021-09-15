from typing import Optional
from fastapi import FastAPI

from pydantic import BaseModel, BaseSettings
import boto3
import base64

class Settings(BaseSettings):
    rekognition_id =""
    rekognition_secret=""
    rekognition_region="us-east-1"
    class Config:
            env_file = ".env"
class Body(BaseModel):
    image: str

    

app = FastAPI()
settings= Settings()

@app.post("/tarea3-200819117")
def get_tags(body: Body):

    options = dict(aws_access_key_id =settings.rekognition_id,aws_secret_access_key =settings.rekognition_secret,region_name=settings.rekognition_region, )

    client = boto3.client("rekognition", **options )
    image = base64.b64decode(body.image.partition(",")[2])
    response = client.detect_labels(Image=dict(Bytes=image))
    return response