from pydantic import BaseModel
from typing import List, Dict, Optional

class MultilingualStr(BaseModel):
    ko: str
    en: str

class Location(BaseModel):
    name: MultilingualStr
    coordinates: Dict[str, float]

class HistoricalFigure(BaseModel):
    name: MultilingualStr
    role: MultilingualStr
    anecdote: Optional[MultilingualStr] = None

class DetailedRecord(BaseModel):
    title: MultilingualStr
    content: MultilingualStr
    source: Optional[str] = None

class GameStats(BaseModel):
    strategy: int
    difficulty: int
    recommended_items: List[MultilingualStr]

class HistoricalOccultData(BaseModel):
    id: str
    event_name: MultilingualStr
    location: Location
    significance: MultilingualStr
    occult_factor: MultilingualStr
    figures: List[HistoricalFigure] = []
    detailed_records: List[DetailedRecord] = []
    game_stats: GameStats
    verified: bool = True
    is_fiction: bool = False

class ArtifactItem(BaseModel):
    id: str
    item_name: MultilingualStr
    history: MultilingualStr
    lore: MultilingualStr
    attributes: Dict[str, str]
    power_level: str
    verified: bool = True
    is_fiction: bool = False

class PersonaData(BaseModel):
    id: str
    name: MultilingualStr
    role: MultilingualStr
    stats: Dict[str, int]
    occult_attribute: MultilingualStr
    lore: MultilingualStr
    relationships: List[Dict[str, str]]
    verified: bool = True
