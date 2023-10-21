from fastapi import APIRouter, HTTPException, status

from DTOs.products import ProductDTO
from services.products import product_service

router = APIRouter(
    prefix="/products",
    tags=["products"]
)

@router.get("/")
async def all():
    return product_service.get_all()

@router.get("/{id}")
async def product(id: str):
    product = product_service.get_by(id)
    
    if product:
        return product
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found!")

@router.post("/")
async def create(product: ProductDTO):
    res = product_service.create(product)
    return res

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(id: str):
    res = product_service.delete_by(id)
    
    if not res:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found!")