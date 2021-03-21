from django.contrib import admin
from django.urls import path
from customers.views import landing_page


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('',landing_page)
]
