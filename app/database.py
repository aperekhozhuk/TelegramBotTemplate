from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app import settings, models


engine = create_engine(settings.DATABASE_URL)
session_maker = sessionmaker(bind=engine)


if __name__ == "__main__":
    models.Base.metadata.create_all(bind=engine)
