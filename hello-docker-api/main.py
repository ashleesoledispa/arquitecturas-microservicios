from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/hello")
def hello(name: str = Query(..., example="Ana")):
    return {
        "message": f"Hola {name} desde Docker"
    }
