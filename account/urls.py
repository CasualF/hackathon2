from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.UserDetailView)

urlpatterns = [
    path('register/', views.RegistrationView.as_view()),
    path('activate/', views.ActivationView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('logout/', views.LogoutView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('', include(router.urls)),
]

