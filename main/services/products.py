from persistence.models import Product
from infrastructure.dependencies import main_context

class ProductService:
    
    def get_all(self, context: main_context):    
        return context.query(Product).all()        
        
product_service = ProductService()