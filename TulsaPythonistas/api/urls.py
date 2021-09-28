from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('event-list/', views.eventList, name="event-list"),
    path('event-detail/<str:pk>/', views.eventDetail, name="event-list"),
]