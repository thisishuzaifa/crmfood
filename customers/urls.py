from django.urls import path, include
from .views import customer_list, customer_detail, customer_create, customer_update, customer_delete 
app_name = "customers"


urlpatterns = [
     path('',customer_list),
     path('<int:pk>/', customer_detail), 
     path('<int:pk>/update/', customer_update), 
     path('<int:pk>/delete/', customer_delete), 
     path('create/', customer_create)
] 