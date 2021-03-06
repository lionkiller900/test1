from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path(
        '<int:product_id>/',
        views.product_description,
        name='product_description'
        ),
    path(
        'put/', views.put_product,
        name='put_product'
        ),
    path(
        'update/<int:product_id>/',
        views.update_product,
        name='update_product'
        ),
    path(
        'delete/<int:product_id>/',
        views.delete_product,
        name='delete_product'
        ),
]
