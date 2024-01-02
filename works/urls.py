from django.urls import path
from .views import landing , detail

app_name = 'works'

urlpatterns = [
    path('', landing , name='jobs'),
    path('details/' , detail , name='details'),

    
]