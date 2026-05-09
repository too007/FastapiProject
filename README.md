main.py
app.include_router(api_router)                                                                         
       ↓
       
router.py
api_router = APIRouter()
api_router.include_router(router)                                                                                                                                          
       ↓                                                                                            
       
apiUser.py
router = APIRouter()
       
↓

@router.post("/users")
def add_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user) 


