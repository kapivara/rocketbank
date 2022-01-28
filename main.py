from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/health")
async def root():
    return {"message": "success"}


uvicorn.run(app, host="0.0.0.0", port=8080)
