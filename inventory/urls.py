from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, ItemCreateView, ItemView, ItemListView

urlpatterns = [
    path("register/", RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('item/', ItemCreateView.as_view(), name='item-create'),
    path('items/', ItemListView.as_view(), name='item-list'),
    path('item/<int:item_id>/', ItemView.as_view(), name='item-detail'),
]
