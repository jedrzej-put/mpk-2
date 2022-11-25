from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class City(Base):
    __tablename__ = "cities"

    city_id = Column(Integer, primary_key=True, index=True)
    city_name = Column(String, index=True)

    def keys_names():
        return ["city_id", "city_name"]

class Route(Base):
    __tablename__ = "routes"

    route_id = Column(String, primary_key=True, index=True)
    route_short_name = Column(String, index=True)
    route_desc = Column(String)

    def keys_names():
        return ["route_id", "route_short_name", "route_desc"]

