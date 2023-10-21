from pydantic import BaseModel, Field


class ProductDTO(BaseModel):
    title: str = Field(min_length=2, max_length=125)
    image: str = Field(min_length=2, max_length=225)
    