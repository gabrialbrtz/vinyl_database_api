import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

file = "../data.sqlite"
dir = os.path.dirname(os.path.realpath(__file__))

# Full path dir + file
path = f"sqlite:///{os.path.join(dir, file)}"

# Creation of the engine using the path
engine = create_engine(path, echo=True)

# Creation of the session passing by parameter the engine
session = sessionmaker(bind=engine)

# Creation of base to manipulate the tables of the database
base = declarative_base()
