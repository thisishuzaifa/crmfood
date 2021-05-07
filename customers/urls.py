from django.urls import path, include
from .views import customer_list, customer_detail
app_name = "customers"


urlpatterns = [
     path('',customer_list),
     path('<pk>/', customer_detail)
     
]