from sqlalchemy import Column, String, Integer, UniqueConstraint
from .database import Base

class Product(Base):
    __tablename__ = "product"
    
    id = Column(Integer, primary_key=True, autoincrement=False)
    title = Column(String)
    image = Column(String)
    
class ProductUser(Base):
    __tablename__ = "product_user"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    product_id = Column(Integer)
    
    UniqueConstraint("user_id", "product_id", name="user_product_unique")