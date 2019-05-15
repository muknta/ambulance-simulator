import os


basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    database = 'ambulance'
    host = 'localhost'
    user = 'postgres'
