from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('product', views.ProductView)
router.register('user',views.UserView)
router.register('notication', views.NoticationView)

urlpatterns = [
    path('', include(router.urls)),
]