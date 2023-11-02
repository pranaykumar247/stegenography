from django.urls import path
from . import views

app_name = 'steganoApp'  # Add this line

urlpatterns = [
    path('encode_text/', views.encode_text, name='encode_text'),
    path('decode_text/', views.decode_text, name='decode_text'),
]
