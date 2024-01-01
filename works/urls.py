from django.urls import path
from .views import landing , home , detail

app_name = 'works'

urlpatterns = [
    #path('', home, name='home'),
    path('', landing , name='jobs'),
    path('details/' , detail , name='details'),

    
]