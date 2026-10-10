
from fastapi import FastAPI

app = FastAPI(title="DocQuery Pipeline")


@app.get("/health")
def health_check():
    return {"status": "ok"}
