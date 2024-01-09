### FASTAPI-NOTES

### Setup Environment
```
$ pip3 install pipenv
$ mkdir app-project-folder
$ cd app-project-folder
$ pipenv shell
```
[More Details](https://github.com/pollyolly/DJANGO-NOTE)
### Installation
```vim
$ pip install uvicorn
$ pip install fastapi
```
main.py
```vim
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
