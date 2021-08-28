
# core/routers.py
from rest_framework.routers import SimpleRouter

from core.products.viewsets import ProductViewSet
from core.viewsets import UserViewSet
from core.auth.viewsets import LoginViewSet, RegistrationViewSet, RefreshViewSet


routes = SimpleRouter()

# AUTHENTICATION
routes.register(r'auth/login', LoginViewSet, basename='auth-login')
routes.register(r'auth/register', RegistrationViewSet, basename='auth-register')
routes.register(r'auth/logout', RefreshViewSet, basename='auth-logout')

# USER
routes.register(r'user', UserViewSet, basename='user')

#product
routes.register(r'product/create', ProductViewSet, basename='product-create')

urlpatterns = [
    *routes.urls
]
