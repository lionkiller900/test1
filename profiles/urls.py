from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('product_history/<product_number>', views.product_history, name='product_history'),
]