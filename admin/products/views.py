import random
from rest_framework import views, viewsets, response, status

from .models import Product, User
from .serializers import ProductSerializer
from .producer import publish, publish_admin

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # publish_admin()
        publish("create_product", serializer.data)
        return response.Response(data=serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk, *args, **kwargs):
        try:
            product = Product.objects.get(id=pk)
            
            serializer = self.serializer_class(instance=product, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            
            publish("update_product", serializer.data)
            return response.Response(data=serializer.data, status=status.HTTP_200_OK)
    
        except:
            return response.Response(data={"detail" : "Not Found!"}, status=status.HTTP_404_NOT_FOUND)
    
    def partial_update(self, request, pk, *args, **kwargs):
        try:
            product = Product.objects.get(id=pk)
            
            serializer = self.serializer_class(instance=product, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            
            publish("patch_product", serializer.data)
            return response.Response(data=serializer.data, status=status.HTTP_200_OK)
        except:
            return response.Response(data={"detail" : "Not Found!"}, status=status.HTTP_404_NOT_FOUND)
    
    def destroy(self, request, pk, *args, **kwargs):
        try:
            product = Product.objects.get(id=pk)
            product.delete()
            
            publish("delete_product", pk)
            return response.Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return response.Response(data={"detail" : "Not Found!"}, status=status.HTTP_404_NOT_FOUND)
    
class UserAPIView(views.APIView):
    def get(self, request):
        users = User.objects.all()
        user = random.choice(users)
        return response.Response({"user" : user.id}, status=200)
    
class LikeProductAPIView(views.APIView):
    def post(self, request, id):
        try:
            product = Product.objects.get(id=id)
            product.likes += 1
            product.save()
            
            return response.Response(data={"detail":"product liked!"}, status=status.HTTP_200_OK)
        except:
            return response.Response(data={"detail" : "Not Found!"}, status=status.HTTP_404_NOT_FOUND)