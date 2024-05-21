from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('services/', get_services, name='services'),
    path('staffs/', get_staffes, name='staffes'),
    path('contact/', get_contact_us, name='contact'),
]