import random

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Serie(BaseModel):
    id: int | None
    nome: str
    ano: int
    temporadas: int
    genero: str


series: list[Serie] = []
next_id = 2

dark = Serie(id=1, nome='Dark', ano=2020, temporadas=3, genero='FICCAO')
series.append(dark)


@app.get('/hello')
def hello():
    return "Hello"


@app.get('/series')
def all_series():
    return series


@app.post('/series', status_code=201)
def create_serie(serie: Serie):
    global next_id
    serie.id = next_id
    next_id += 1
    series.append(serie)
    return serie


@app.get('/series/{id}')
def detail_serie(id: int):
    return series[id-1]
