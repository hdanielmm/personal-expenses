from fastapi import FastAPI
from core.models import models
from core.settings import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Welcome to personal expenses application"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", log_level="info", reload=True)
