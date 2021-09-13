from typing import Optional

from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def get_tags():
    return "Dude"