from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router .register('', views.UserViewSet)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls'))
]
urlpatterns += router.urls