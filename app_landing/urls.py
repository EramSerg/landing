from django.urls import path
from .views import app_landing_view, TemplView

urlpatterns = [
    path('template/', TemplView.as_view()),
    path('welcome/', app_landing_view),
]
