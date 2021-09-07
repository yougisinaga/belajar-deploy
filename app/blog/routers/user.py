from fastapi import APIRouter, Depends,status
from blog import database, schemas
from sqlalchemy.orm import Session
from blog.repository import User

router = APIRouter(
    prefix="/user",
    tags=['Users']
)
get_db=database.get_db


@router.post('/')
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return User.create_user(request,db)

@router.get('/{id}', response_model = schemas.ShowUser)
def show_user(id, db: Session = Depends(get_db)):
    return User.show_user(id,db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def hapus(id:int, db: Session = Depends(get_db)):
    return User.delete(id,db)
