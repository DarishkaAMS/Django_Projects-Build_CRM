from django.urls import path
from .views import (AssignAgentView,
                    lead_create,
                    LeadCreateView,
                    lead_delete,
                    LeadDeleteView,
                    lead_detail,
                    LeadDetailView,
                    lead_list,
                    LeadListView,
                    lead_update,
                    LeadUpdateView)

app_name = "leads"

urlpatterns = [
    path('', LeadListView.as_view(), name="lead-list"),
    path('create/', LeadCreateView.as_view(), name="lead-create"),
    path('<int:pk>/', LeadDetailView.as_view(), name="lead-detail"),
    path('<int:pk>/assign-agent/', AssignAgentView.as_view(), name="assign-agent"),
    path('<int:pk>/delete/', LeadDeleteView.as_view(), name="lead-delete"),
    path('<int:pk>/update/', LeadUpdateView.as_view(), name="lead-update"),

]
