from django.urls import path
from .views import show_event, show_profile


urlpatterns = [
    path('event/', show_event, name='show_event'),
    path('profile/', show_profile, name='show_profile')
]


