from fastapi import FastAPI, Depends
from . import database, models, schemas
from .src.pokemon_service import process_pokemon
from sqlalchemy.orm import Session

app = FastAPI(title="Flip DE Assessment")

# Create requuired tables
models.Base.metadata.create_all(bind=database.engine)


@app.post("/process-pokemon/", response_model=schemas.PokemonProcessResponse)
async def process_pokemon_route(payload: schemas.PokemonProcessRequest, db: Session = Depends(database.get_db)):
    return await process_pokemon(payload, db)
