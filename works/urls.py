from django.urls import path
from .views import landing , detail , province_view

app_name = 'works'

urlpatterns = [
    path('', landing , name='jobs'),
    path('#/', province_view , name='province'),
    path("<str:id>" , detail , name='details'),
    path("home/" , landing , name='home'),
    
]