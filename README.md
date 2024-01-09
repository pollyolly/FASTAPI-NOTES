### FASTAPI-NOTES

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
```

```
