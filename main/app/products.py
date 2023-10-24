import json, requests

from fastapi import APIRouter, HTTPException, status

from producer import publish
from DTOs.products import ProductDTO
from services.products import product_service
from persistence.models import Product, ProductUser
from infrastructure.dependencies import main_context

router = APIRouter(
    prefix="/products",
    tags=["products"]
)

@router.get("/")
async def all(context: main_context):
    return product_service.get_all(context)

@router.post("/")
async def create(product: ProductDTO, context: main_context):
    product = Product(**product.model_dump())
    context.add(product)
    context.commit()
    return product

@router.put("/{id}")
async def create(id: int,product_dto: ProductDTO, context: main_context):
    product = context.query(Product).get(id)
    product.title = product_dto.title
    product.image = product_dto.image
    
    context.add(product)
    context.commit()
    
    return product

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(id: int, context: main_context):
    product = context.query(Product).get(id)
    context.delete(product)
    context.commit()
    
@router.post("/like/{id}", status_code=status.HTTP_201_CREATED)
async def like(id:int, context: main_context):
    res = requests.get("http://docker.for.mac.localhost:8000/api/products/user/")
    res = res.json()
    
    user_id = res.get("user", 0)
    
    like = ProductUser()
    like.user_id = user_id
    like.product_id = id
    
    context.add(like)
    context.commit()
    
    publish("like_product", id)
    
    return like