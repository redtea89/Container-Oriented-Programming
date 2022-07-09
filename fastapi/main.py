from fastapi import FastAPI

app = FastAPI()


@app.get("/fastapi/")
async def root():
    return {"message": "FastAPI World"}
