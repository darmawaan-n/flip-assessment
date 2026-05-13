from pydantic import BaseModel, Field
from typing import List


class PokemonProcessRequest(BaseModel):
    """Validates the incoming JSON request."""

    raw_id: str = Field(..., min_length=13, max_length=13, example="7dsa8d7sa9dsa")
    user_id: str = Field(..., min_length=7, max_length=7, example="5199434")
    pokemon_ability_id: str = Field(..., example="150")


class LanguageSchema(BaseModel):
    """Schema for the language dictionary object."""

    name: str
    url: str


class EffectEntrySchema(BaseModel):
    """Normalized effect entry as stored in the DB."""

    effect: str
    language: LanguageSchema
    short_effect: str


class PokemonProcessResponse(BaseModel):
    """The final expected JSON output structure."""

    raw_id: str
    user_id: str
    returned_entries: List[EffectEntrySchema]
    pokemon_list: List[str]  # List of names
