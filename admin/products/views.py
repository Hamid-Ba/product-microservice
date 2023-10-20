import random
from rest_framework import views, viewsets, response

from .models import Product, User
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    
class UserAPIView(views.APIView):
    def get(self, request):
        users = User.objects.all()
        user = random.choice(users)
        return response.Response({"user" : user.id}, status=200)