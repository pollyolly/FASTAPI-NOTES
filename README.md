### FASTAPI-NOTES

### Setup Environment
```
$ pip install pipenv
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

# Importing other python files
import consumers.py

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```
### Run
```vim
$ uvicorn main:app --reload
```
### References
[Event Driven System FastAPI](https://www.youtube.com/watch?v=VkPUBx_WtK8&t=10s)

[FastAPI](https://fastapi.tiangolo.com/)
