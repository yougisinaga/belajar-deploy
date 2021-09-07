from sqlalchemy.orm import Session, session
from blog import models, schemas
from fastapi import HTTPException,status

def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create(request:schemas.Blog ,db: Session):
    new_blog = models.Blog(title=request.title,body=request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def show(id:int, db: Session):
    blogs = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blogs:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail=f"Blog dengan id {id} tidak tersedia")
     # response.status_code = status.HTTP_404_NOT_FOUND
       #return {'detail': f"Blog dengan id {id} tidak tersedia"}    
    return blogs

def delete(id:int,db: Session):
     blogs = db.query(models.Blog).filter(models.Blog.id ==  id)
     if not blogs:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail=f"Blog dengan id {id} tidak tersedia")                               
     blogs.delete(synchronize_session=False)
     db.commit()
     return 'done'

def update(id:int, request:schemas.Blog, db: Session):
     blogs = db.query(models.Blog).filter_by(models.Blog.id == id) 
     if not blogs.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog dengan id {id} tidak tersedia")    
     blogs.update(request.dict())  
     db.commit()
     db.refresh(blogs)
     return 'updated'


