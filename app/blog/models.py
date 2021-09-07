from sqlalchemy import  Column, Integer, String, ForeignKey
from blog.database import Base, get_db
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20))
    email = Column(String(20))
    password = Column(String(100))

    blogs = relationship("Blog", back_populates='creator')

class Blog(Base):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(20))
    body = Column(String(20)) 
    user_id = Column(Integer, ForeignKey("User.id"))

    creator = relationship("User", back_populates="blogs")