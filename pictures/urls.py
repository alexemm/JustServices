from django.urls import path
from .views import IndexView


from . import views

app_name = 'pictures'
urlpatterns = [
    path('index/', IndexView.as_view(), name='picture_index'),
]