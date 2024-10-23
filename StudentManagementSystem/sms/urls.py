from django.urls import path
from . import views 

urlpatterns = [
    path('dis',views.display),
    path('add',views)
    
    
]