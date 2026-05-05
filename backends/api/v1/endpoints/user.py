from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from backends.api.deps import get_db
from backends.db.session import engine 
from backends.schemas.user_schema import UserCreate
from sqlalchemy import text

from backends.crud.user import create_user, get_users



router = APIRouter()

@router.post("/users")
def add_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)    

@router.get("/users")
def list_users(db: Session = Depends(get_db)):
    return get_users(db)

@router.get("/db-check")
def db_check():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            return {"status": "connected", "result": result.scalar()}
    except Exception as e:
        return {"status": "error", "message": str(e)}