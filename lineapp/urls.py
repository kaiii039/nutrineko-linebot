from django.urls import path
from .views import webhook_callback

urlpatterns = [
    path('callback/', webhook_callback, name='line-callback'),
]