from .views import TractionView
from django.urls import path
 
urlpatterns = [
    path('traction-view', TractionView.as_view() , name='Traction -list')
]