import json
import os
from fastapi import FastAPI, HTTPException, Query
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
from models import HistoricalOccultData, ArtifactSpec, PersonaData

app = FastAPI(
    title="K-History Occult Nexus API",
    description="A premium historical fantasy data engine providing structured Korean occult lore.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load data helper
def load_data(filename: str):
    path = os.path.join("data", filename)
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

# Endpoints
@app.get("/historical-shrine", response_model=List[HistoricalOccultData])
async def get_shrines(category: Optional[str] = None):
    data = load_data("battlefields.json")
    if category:
        data = [d for d in data if d["category"].lower() == category.lower()]
    return data

@app.get("/artifact-specs", response_model=List[ArtifactSpec])
async def get_artifacts(min_power: int = 0):
    data = load_data("artifacts.json")
    return [d for d in data if d["power_level"] >= min_power]

@app.get("/persona-api", response_model=List[PersonaData])
async def get_personas():
    return load_data("personas.json")

@app.get("/chronicle-horror")
async def get_chronicles():
    return load_data("chronicles.json")

@app.get("/history-data")
async def get_history_data():
    return load_data("history_data.json")

@app.get("/comprehensive-wars")
async def get_comprehensive_wars():
    return load_data("comprehensive_wars.json")

# Serve UI
@app.get("/")
async def root():
    from fastapi.responses import FileResponse
    return FileResponse("static/index.html")

# Mount static files
os.makedirs("static", exist_ok=True)
app.mount("/static", StaticFiles(directory="static"), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
