from django.conf import settings
from django.urls import path
from neighbourhood import views 
from rest_framework.authtoken.views import obtain_auth_token
from django.views.generic.base import TemplateView


urlpatterns = [
    path('api/v1/hoods', views.NeighbourhoodList.as_view()),
    path('.*', TemplateView.as_view(template_name="home.html"), name="home")
]
