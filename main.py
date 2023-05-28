from fastapi import FastAPI
from endpoints.countries import router

app = FastAPI(
    title= "Capitals API",
    description= "The Capitals API project",
    version= "0.1.0",
    contact={"name":"Gwen","email":"Gwen@com"},
    license_info={"name":"MIT",},
)

app.include_router(router)
