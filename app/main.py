from fastapi import FastAPI
from pydantic import BaseModel
import json
import requests
import socket
from fastapi.responses import FileResponse

app = FastAPI(
    title= socket.gethostname(),
    description="Demo FCEFyN-UNC",
    version="0.0.1"
)

image = "/app/images/_proyecto_.png"

dbs = []
class Country(BaseModel):
    name: str

@app.get("/")
async def main():
    return FileResponse(image)

@app.post('/loadcountry')
def cargar_paises(country: Country):
    dbs.append(country.dict())
    return dbs[-1]

@app.get('/heroku')
def mostrar_informacion_por_pais():
    results = []
    if len(dbs) == 0:
        return{
            "message" : "Ingresar paises, la lista esta vacia"
        }
    else:
        for country in dbs:
            r = requests.get('http://coronavirus-19-api.herokuapp.com/countries/' + country["name"])
            data = r.json()
            results.append({'country' : data['country'],
                            'cases': data['cases'],
                            'todayCases': data['todayCases'],
                            'deaths': data['deaths'],
                            'todayDeaths': data['todayDeaths'],
                            'recovered': data['recovered']
                            })
        return results

@app.get('/listcountry')
def mostrar_todos_los_paises():
    return dbs

@app.delete('/country/{country_id}')
def eliminar_pais(country_id: int):
    dbs.pop(country_id)
    return {
        "message" : "País eliminado con éxito"
    }