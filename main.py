from email.message import EmailMessage
import json
from src.model.client import Client
from fastapi import FastAPI, Body
import re
import uvicorn

app = FastAPI()

client_list = []

@app.get("/health")
async def root():
    return {"message": "success"}

@app.post("/clients")
def create_client(request_body = Body(...)):
    
    name = request_body["name"]
    email = request_body["email"]
    id = request_body ["id"]
    client = Client(name, email, id) 
    client_list.append(client)
    print(client_list)
    
    #if check_email(email):
    #    return client
    #else:
    #    return {"message":"invalid email"}
   
def check_email(email):
    pattern = r'^[a-z 0-9]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$'

    return bool(re.match(pattern, email))
   
    #if re.search(pattern, email):
    #    return True
    #else:
    #    return False
   
#uvicorn.run(app, host="0.0.0.0", port=8080)