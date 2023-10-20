from rest_framework.routers import DefaultRouter
from django.urls import path, include

from products import views

router = DefaultRouter()

router.register("products", views.ProductViewSet)

app_name = "products"

urlpatterns = [
    path("", include(router.urls)),
    path("user/", views.UserAPIView.as_view(), name="rand_user"),
]
