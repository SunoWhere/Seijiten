from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import yaml


with open("db/config.yml", "r") as file:
    db_config = yaml.safe_load(file)

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://" \
                          + db_config["username"] + ":" \
                          + db_config["password"] + "@" \
                          + db_config["host"] +"/" \
                          + db_config["database"] + "?charset=utf8mb4"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()