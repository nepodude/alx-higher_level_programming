#!/usr/bin/python3
"""
Prints the State object with the given name from the database hbtn_0e_6_usa.
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
    state_name = sys.argv[4]

    # Create the database engine
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}",
        pool_pre_ping=True
    )

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the state using a parameterized filter (SQL injection safe)
    state = session.query(State).filter(State.name == state_name).first()

    # Print result or "Not found" if no match
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()
