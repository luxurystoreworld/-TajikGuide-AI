import json
from pathlib import Path

DATABASE = Path(__file__).parent.parent / "database" / "places.json"

def get_places():
    with open(DATABASE, "r", encoding="utf-8") as file:
        return json.load(file)
