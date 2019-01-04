#!/usr/bin/python3
"""Lists all City obejcts from te database
"""
if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from relationship_state import Base, State
    from relationship_city import City
    import sys

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).all():
        for city in state.cities:
            print("{}: {} -> {}".format(city.id, city.name, state.name))
    session.commit()
    session.close()
