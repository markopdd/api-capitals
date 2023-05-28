from typing import Optional, List
from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter()

cities = [{
        "country_name" : "Ukraine",
        "city_name" : "Kyiv",
        "population" : "4 millions",
        "is_capital" : True,
        "area" : "839 sq2",
        "timezone" : "UTC",
        "major_landmarks" : ["Sobor Svjatogo Volodimyra", "Pecherska Lavra", "Majdan Nezalegnosti"],
        "museums" : ["Nacionalnij Hudozhnij Muzej", "History Museum of Kyiv"],
        "universities": [
            "Kyivskij nacionalnij universitet imeni Tarasa Sevcenka", 
            "Nacionalnij tehnichnij universitet Ukraїni - Kiїvskij politehnicnij institut"],

    }
]

class Cities(BaseModel):
    city_name: str
    population: str
    is_capital: bool
    area: str
    timezone: str
    major_landmarks: Optional[list]
    museums: Optional[list]
    universities: Optional[list]



@router.get("/cities", response_model=List[Cities])
async def get_all_cities():
    return cities

@router.post("/cities/")
async def add_city(city: Cities):
    return cities.append(city)

@router.get("/cities/city_names")
async def get_all_city_names():
    return [city_names.get("country_name") for city_names in cities]

@router.get("/countries/{city_id}")
async def get_country_id(city_id: int):
    return cities[city_id]

