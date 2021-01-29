from django.urls import path
from .views import *


urlpatterns = [
    path('nested_set/', nested_set, name='nested_set'),
    path('nested_set/rubric/<int:pk>', get_rubrick, name='rubric'),
]