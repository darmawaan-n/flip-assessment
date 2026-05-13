from pydantic import BaseModel, Field, field_validator
from typing import List


class PokemonProcessRequest(BaseModel):
    """Validates the incoming JSON request."""

    raw_id: str = Field(default=None, min_length=13, max_length=13, example="7dsa8d7sa9dsa")
    user_id: str = Field(default=None, min_length=7, max_length=7, example="5199434")
    pokemon_ability_id: str = Field(example="150")

    @field_validator("user_id")
    @classmethod
    def check_user_id_numeric(cls, value: str):
        if not value.isdigit():
            raise ValueError("user_id must contain digit-only characters")
        return value

    @field_validator("raw_id")
    @classmethod
    def check_raw_id_alnum(cls, value: str):
        if not value.isalnum():
            raise ValueError("raw_id must contain alpha-numeric-only characters")
        return value


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
