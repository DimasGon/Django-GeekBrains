from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:pk>', views.CartAdd.as_view()),
    path('delete/<int:pk>', views.CartDelete.as_view()),
    path('order', views.OrderView.as_view()),
    path('', views.CartView.as_view()),
]
