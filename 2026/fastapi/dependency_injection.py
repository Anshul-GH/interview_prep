from fastapi import Depends, FastAPI

app = FastAPI()

def common_dependency():
    return {"dependency_data": "Shared logic or data"}

@app.get("/use-dependency")
def use_dependency(data = Depends(common_dependency)):
    return data
