from django.urls import path
from .views import login_page, registerHandller


urlpatterns = [
    path('login', login_page, name="login"),
    path('registerHandller', registerHandller, name="registerHandller"),
]
