from persistence.models import Product
from infrastructure.dependencies import main_context

class ProductService:
    
    def get_all(self, context: main_context):    
        return context.query(Product).all()        
    
    def get_by(self, id: str):
        try:
            return Product.get(id)
        except:
            return False
        
    def create(self, product):
        product = Product(**product.model_dump())
        return product.save()
        
    def delete_by(self, id:str):
        try:
            Product.delete(id)
            return True
        except:
            return False
    
    def decrease_stock(self, id: str, count: int):
        product = self.get_by(id)
        
        if product:
            if (product.quantity - count) > 0:
                product.quantity -= count
                return product.save()

        return False
        
product_service = ProductService()