#!/usr/bin/python3
"""
Lists all State objects and their corresponding City objects
from the database hbtn_0e_101_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # Retrieve command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create the database engine
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}",
        pool_pre_ping=True
    )

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all states with their corresponding cities in one query
    states = session.query(State).order_by(State.id).all()

    # Print states and their cities
    for state in states:
        print(f"{state.id}: {state.name}")
        for city in sorted(state.cities, key=lambda city: city.id):
            print(f"\t{city.id}: {city.name}")

    # Close the session
    session.close()
