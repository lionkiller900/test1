from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_pack, name='view_pack'),
    path('add/<item_id>/', views.put_to_bag, name='put_to_bag'),
    path('edit/<item_id>/', views.edit_pack, name='edit_pack'),
    path('delete/<item_id>/', views.delete_pack, name='delete_pack'),
]
