from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

# Autoriser les appels depuis ton app web (http://127.0.0.1:5500)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tu peux mettre ["http://127.0.0.1:5500"] pour restreindre
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/add")
def add(a: float, b: float):
    return {"result": a + b}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
