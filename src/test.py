
from sqlalchemy.orm import Session
from sqlalchemy import inspect

from mypackage.database import crud, models, schemas
from mypackage.database.database import SessionLocal, engine

from mypackage.classes.LoadData import LoadData

models.Base.metadata.drop_all(bind=engine)
models.Base.metadata.create_all(bind=engine)
load_all_files = LoadData()
load_all_files()
