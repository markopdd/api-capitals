from typing import Optional, List
from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter()

countries = [
    {
        "country_name" : "Ukraine",
        "capital_name" : "Kyiv",
        "population" : "40 millions",
        "language" : "Ukrainian",
        "big_cities" : [
            "Kyiv", "Kharkiv", "Odesa", "Dnipro", "Donetsk", "Lviv", "Sevastopol"],
        "national_holidays" : 16,
        "interesting_facts" : "The most beautiful country in the world!",            
    }
]

class Country(BaseModel):
    country_name: str
    capital_name: str
    population: str
    language: str
    big_cities: Optional[list]
    national_holidays: Optional[int]
    interesting_facts: Optional[str]


@router.get("/countries", response_model=List[Country])
async def get_all_countries():
    return countries

@router.post("/countries/")
async def add_country(country: Country):
    return countries.append(country)

@router.get("/countries/country_names")
async def get_all_country_names():
    return [country.get("country_name") for country in countries]

@router.get("/countries/{country_id}")
async def get_country_id(country_id: int):
    return countries[country_id]

