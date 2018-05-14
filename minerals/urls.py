from django.urls import path

from . import views

urlpatterns = [
    # ex: /minerals/
    path('', views.index, name='index'),
    # ex: /minerals/Abelsonite/
    path('<name>/', views.detail, name='detail'),
]