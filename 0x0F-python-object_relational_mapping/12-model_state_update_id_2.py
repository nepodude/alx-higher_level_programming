#!/usr/bin/python3
"""
Updates the name of the State where id = 2 to 'New Mexico' in hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State  # Import State and Base

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

    # Retrieve the State object with id = 2
    state = session.query(State).filter_by(id=2).first()

    # Update the state name if it exists
    if state:
        state.name = "New Mexico"
        session.commit()

    # Close the session
    session.close()
