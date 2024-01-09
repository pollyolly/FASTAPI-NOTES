### FASTAPI-NOTES

### Setup Environment
```
$ cd app-project-folder
$ pip3 install pipenv
```
[More Details](https://github.com/pollyolly/DJANGO-NOTE)
### Installation
```vim
$ pip install uvicorn
$ pip install fastapi
```
```vim
# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```
Run
```
$ uvicorn main:app --reload
```
