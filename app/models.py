from sqlalchemy import Column, Integer, String, JSON
from .database import Base


class PokemonEffect(Base):
    __tablename__ = "pokemon_effects"

    id = Column(Integer, primary_key=True, index=True)
    raw_id = Column(String(13), index=True)
    user_id = Column(Integer, index=True)
    pokemon_ability_id = Column(Integer)
    effect = Column(String)
    language = Column(JSON)
    short_effect = Column(String)
