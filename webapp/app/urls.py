from django.urls import path, include

from app.views import HomeView

app_name="app"
urlpatterns = [
    path('home/', HomeView.as_view()),
]
