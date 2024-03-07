from sqlalchemy import Column, Integer, String

from database.database import Base


class Peak(Base):
    __tablename__ = 'peaks.peaks'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    elevation_meters = Column(Integer)
    # latitude = Column(Integer)
    # longitude = Column(Integer)
