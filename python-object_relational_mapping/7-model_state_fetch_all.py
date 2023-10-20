#!/usr/bin/python3

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password>"
              " <database_name>".format(
                  sys.argv[0]))
        sys.exit(1)

    mysql_uname = sys.argv[1]
    mysql_pwd = sys.argv[2]
    db_name = sys.argv[3]

    # Create a database connection
    engine = create_engine(
        f'mysql+mysqldb://{mysql_uname}:{mysql_pwd}@localhost:3306/{db_name}',
        pool_pre_ping=True
    )

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and print all State objects, sorted by states.id
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()