from django.urls import path
from .views import login_page, registerHandller, logoutN


urlpatterns = [
    path('login', login_page, name="login"),
    path('registerHandller', registerHandller, name="registerHandller"),
    path('logout', logoutN, name="logout"),
]
