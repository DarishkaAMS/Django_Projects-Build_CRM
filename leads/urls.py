from django.urls import path
from .views import lead_list, lead_detail

app_name = "leads"

urlpatterns = [
    path('', lead_list),
    path('<str:pk>/', lead_detail),
]
