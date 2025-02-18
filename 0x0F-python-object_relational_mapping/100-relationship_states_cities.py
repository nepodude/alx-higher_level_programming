#!/usr/bin/python3
"""
Creates the State 'California' with the City 'San Francisco'
in the database hbtn_0e_100_usa.
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

    # Create tables in the database
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create State and City objects
    california = State(name="California")
    san_francisco = City(name="San Francisco", state=california)

    # Add to session and commit
    session.add(california)
    session.add(san_francisco)
    session.commit()

    # Close the session
    session.close()
