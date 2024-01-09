### FASTAPI-NOTES

### Setup Environment
```
$ pip3 install pipenv
$ mkdir test_project_folder
$ cd test_project_folder
$ pipenv shell
```
[More Details](https://github.com/pollyolly/DJANGO-NOTE)
### Installation
```vim
$ pip install uvicorn
$ pip install fastapi
```
test_project_folder/main.py
```vim
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```
### Run
```vim
$ uvicorn main:app --reload
```
