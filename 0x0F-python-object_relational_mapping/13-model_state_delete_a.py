#!/usr/bin/python3
"""
Deletes all State objects with a name containing 'a' from hbtn_0e_6_usa.
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

    # Query states containing the letter 'a'
    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()

    # Delete each state found
    for state in states_to_delete:
        session.delete(state)

    # Commit changes
    session.commit()

    # Close the session
    session.close()
