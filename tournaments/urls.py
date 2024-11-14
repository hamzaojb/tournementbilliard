# tournaments/urls.py
from django.urls import path
from . import views
app_name = 'tournaments'


urlpatterns = [
    path('', views.home, name='home'),
        path('register/<int:tournament_id>/', views.register_for_tournament, name='register'),
            path('publications/', views.publication_list, name='publication_list'),


]
