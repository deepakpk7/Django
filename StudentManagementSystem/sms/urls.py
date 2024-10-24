from django.urls import path
from . import views 

urlpatterns = [
    path('dis',views.display),
    path('add',views.add),
    path('edit_std/<id>',views.edit_std),
]