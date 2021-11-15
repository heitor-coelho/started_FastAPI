from fastapi import FastAPI
from pydantic import BaseModel
from random import randint
from typing import List, Optional
from uuid import uuid4

app = FastAPI()

class Animal(BaseModel):
    nome: str
    sexo: str
    id: Optional[str]
    idade:int
    cor: str 

banco: List[Animal] = []

@app.post("/animal")
def cadastrar_animal(animal: Animal):
    animal.id = str(uuid4())
    banco.append(animal)
    return None



@app.get("/animal") 
def get_all_animal():   
    return banco

@app.get("/animal/{animal_id}")
def get_id_animal(animal_id:str):
    for animal in banco:
        if animal.id == animal_id:
            return animal
    return ("Animal não encontrado")

@app.delete("/animal/{animal_id}")
def remover_animal(animal_id:str):
    posicao = -1
    for index, animal in enumerate(banco):
        if animal.id == animal_id:
            posicao = index
            break      

    if posicao != -1:
        banco.pop(posicao)  
        return "Animal removido com sucesso."
    else:
        return "Algo deu errado."
