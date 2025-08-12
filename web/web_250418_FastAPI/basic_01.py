from fastapi import FastAPI


app = FastAPI()

@app.get("/te.st")
def test():
    d = {"name" : "마이쮸", "price" : 1000}
    return d