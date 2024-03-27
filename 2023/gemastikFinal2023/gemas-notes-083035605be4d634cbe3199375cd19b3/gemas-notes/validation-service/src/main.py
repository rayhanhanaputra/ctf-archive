from fastapi import Request, FastAPI, HTTPException, Depends
import requests
import json
import re
from validation import validation_schema
from jsonschema import Draft7Validator,validate
from jsonschema.exceptions import ValidationError

@Draft7Validator.FORMAT_CHECKER.checks("security-validation",ValueError)
def validate_payload(data):
    pattern = r'[!#$"\'`{}()]'
    return not re.search(pattern, data)

app = FastAPI()
note_service = "http://gemas-notes:3000"

@app.api_route("/{path_name:path}", methods=["GET","DELETE"])
def no_body_request(request: Request):
    client_host = request.client.host
    headers = {"X-Real-IP": client_host}
    if request.headers.get("authorization"):
        headers["Authorization"] = request.headers.get("authorization")

    if request.method == "DELETE":
        status_code = requests.delete(note_service + request.url.path, headers=headers).status_code
        if status_code == 204:
            return {}
        raise HTTPException(status_code=500)
    
    try:
        return requests.get(note_service + request.url.path, headers=headers).json()
    except:
        return []

@app.api_route("/{path_name:path}", methods=["POST", "PUT","PATCH"])
async def with_body_request(request: Request):
    url_path = request.url.path
    body = await request.body()
    client_host = request.client.host

    if request.headers.get("content-type") != "application/json":
        raise HTTPException(status_code=400, detail="Please specify JSON data")
    
    try:
        headers = dict(request.headers)
        headers["X-Real-IP"] = client_host
        validate(json.loads(body), validation_schema.get(url_path), format_checker=Draft7Validator.FORMAT_CHECKER)

        if request.method == "PUT":
            res = requests.put(note_service + url_path, data=body, headers=headers)
        elif request.method == "PATCH":
            res = requests.patch(note_service + url_path, data=body, headers=headers)
        else:
            res = requests.post(note_service + url_path, data=body, headers=headers)
        
        
        if res.status_code == 401:
            raise HTTPException(status_code=401, detail="Please Login")
        
        if res.status_code == 200:
            return res.json()

        return {}
    
    except ValidationError as e:
        raise HTTPException(status_code=400, detail="Invalid JSON data")

