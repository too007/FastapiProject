from backends.db.session import engine, Base
from backends.model import user

def init_db():
    Base.metadata.create_all(bind=engine)