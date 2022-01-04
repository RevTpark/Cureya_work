from django.urls import path, include
from .views import CustomUserCreate, BlacklistTokenView

urlpatterns = [
    path("register/", CustomUserCreate.as_view(), name="create_user"),
    path("logout/blacklists/", BlacklistTokenView.as_view(), name="blacklist"),

]
