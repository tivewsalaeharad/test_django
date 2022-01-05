from django.contrib import admin
from django.urls import path
from moscowregionsite import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.showlist, name="showlist"),
    path('api/localities/', views.LocalitiesView.as_view()),
]
