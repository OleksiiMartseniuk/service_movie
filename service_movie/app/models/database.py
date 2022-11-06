import databases
from config.settings import SQLALCHEMY_DATABASE_URL


database = databases.Database(SQLALCHEMY_DATABASE_URL)
