from django.urls import path
from .views import IndexView


from . import views

app_name = 'pictures'
urlpatterns = [
#<<<<<<< HEAD
    path('', views.PictureView.as_view(), name='index'),
#=======
    path('index/', IndexView.as_view(), name='picture_index'),
#>>>>>>> a12aa38c2b414a10edd9c4391940eee2708e4fcc
]