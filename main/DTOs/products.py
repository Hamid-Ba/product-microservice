from pydantic import BaseModel, Field


class ProductDTO(BaseModel):
    id: int
    title: str = Field(min_length=2, max_length=125)
    image: str = Field(min_length=2, max_length=225)

class ProductUserDTO(BaseModel):
    id: int
    user_id: int
    product_id: int