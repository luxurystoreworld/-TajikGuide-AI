from fastapi import APIRouter

router = APIRouter()

places = [
    {
        "id": 1,
        "name": "Iskanderkul",
        "city": "Sughd",
        "description": "Beautiful mountain lake in Tajikistan."
    },
    {
        "id": 2,
        "name": "Dushanbe",
        "city": "Dushanbe",
        "description": "Capital city of Tajikistan."
    },
    {
        "id": 3,
        "name": "Khujand",
        "city": "Sughd",
        "description": "Historic city in northern Tajikistan."
    }
]

@router.get("/places")
def get_places():
    return places
