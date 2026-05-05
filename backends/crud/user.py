from backends.model.user import User



def create_user(db, user):
    # create object
    db_user = User(
        name=user.name,
        email=user.email
    )

    # save to DB
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

def get_users(db):
    return db.query(User).all()