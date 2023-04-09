from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.store, name="store"),
    path('sponsors/', views.sponsors, name="sponsors"),

]
