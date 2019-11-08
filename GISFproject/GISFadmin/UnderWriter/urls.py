from django.urls import path
from .views import (InsuredcreateView,PolicyCreateView,PolicyUpdateView)
app_name = 'UnderWriter'

urlpatterns = [
    path('CreateInsured/', InsuredcreateView, name='CreateInsured'),
    path('PolicyCreate/', PolicyCreateView, name='PolicyCreate'),
    path('PolicyUpdate/',PolicyUpdateView, name='PolicyUpdate')
    ]
