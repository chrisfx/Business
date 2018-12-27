from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('customerform', views.customerform, name='customerform'),
    path('list/', views.CustomerListView.as_view(), name='list'),
]
