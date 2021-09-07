from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import user
from blog import models, schemas
from fastapi import HTTPException,status
from blog.hashing import Hash

def create_user(request:schemas.User, db: Session):
    add_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(add_user)
    db.commit()
    db.refresh(add_user)
    return add_user

def show_user(id: int, db:Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail=f"User dengan id {id} tidak tersedia")
    return user

def delete(id:int,db: Session):
     user = db.query(models.User).filter(models.User.id ==  id)
     if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail=f"Blog dengan id {id} tidak tersedia")                               
     user.delete(synchronize_session=False)
     db.commit()
     return 'done'