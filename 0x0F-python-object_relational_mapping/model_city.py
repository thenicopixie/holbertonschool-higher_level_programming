#!/usr/bin/python3
"""Contains the calss definition of a City
"""
if __name__ == "__main__":
    from sqlalchemy import Column, Integer, String
    from model_state import Base, State

    class City(Base):
        """A state class inheriting from base
        """
        __tablename__ = 'cities'
        id = Column(Integer, primary_key=True, autoincrement=True,
                    nullable=False)
        name = Column(String(50), nullable=False)
        state_id = Column(Integer, foreign_key(states.id), nullable=False)
