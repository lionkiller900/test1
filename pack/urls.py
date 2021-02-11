from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_pack, name='view_pack'),
    path('add/<item_id>/', views.put_to_bag, name='put_to_bag')
]
