from django.urls import path, include
from snippets import views
from rest_framework.routers import DefaultRouter

#create a router and register our viewsets with it
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet, basename='snippet')
router.register(r'users', views.UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]
