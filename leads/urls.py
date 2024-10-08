from django.urls import path
from . import views

app_name = 'leads'

urlpatterns = [
    path('', views.LeadListView.as_view(), name='list'),
    path('create/', views.LeadCreateView.as_view(), name='create'),
    path('<pk>/', views.LeadDetailView.as_view(), name='detail'),
    path('<pk>/update', views.LeadUpdateView.as_view(), name='update'),
    path('<pk>/delete', views.LeadDeleteView.as_view(), name='delete'),
]
