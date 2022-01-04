from django.urls import path, include
from .views import BotSolutions

urlpatterns = [
    path("query/", BotSolutions.as_view(), name="query_view"),

]
