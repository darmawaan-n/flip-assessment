import httpx
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from .. import database, models, schemas


async def process_pokemon(payload: schemas.PokemonProcessRequest, db: Session):
    # 1. Parse Input JSON
    ability_id = payload.pokemon_ability_id
    raw_id = payload.raw_id
    user_id = payload.user_id

    if not ability_id:
        raise HTTPException(status_code=400, detail="pokemon_ability_id is required")

    # 2. Hit PokeAPI
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://pokeapi.co/api/v2/ability/{ability_id}")
        if response.status_code != 200:
            raise HTTPException(status_code=404, detail="Ability not found")

        data = response.json()

    # 3. Normalize & Store effect_entries
    effect_entries = data.get("effect_entries", [])
    stored_entries = []

    for entry in effect_entries:
        new_effect = models.PokemonEffect(
            raw_id=raw_id,
            user_id=user_id,
            pokemon_ability_id=int(ability_id),
            effect=entry.get("effect"),
            language=entry.get("language"),
            short_effect=entry.get("short_effect"),
        )
        db.add(new_effect)
        stored_entries.append(
            {"effect": entry.get("effect"), "language": entry.get("language"), "short_effect": entry.get("short_effect")}
        )

    db.commit()

    # 4. Extract Pokemon Names
    pokemon_names = [p["pokemon"]["name"] for p in data.get("pokemon", [])]

    # 5. Return expected JSON
    return {"raw_id": raw_id, "user_id": user_id, "returned_entries": stored_entries, "pokemon_list": pokemon_names}
