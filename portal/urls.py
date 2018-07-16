from django.urls import path, include
from .views import IndexView, AboutView


from . import views

app_name = 'portal'
urlpatterns = [
    path('index/', IndexView.as_view(), name='index'),
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about')]

