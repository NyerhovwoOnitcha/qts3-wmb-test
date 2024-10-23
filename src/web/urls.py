from django.urls import path

from .views import batch
from .views import home
from .views import new_batch
from .views import user_login
from .views import user_view
from .views import logout_view



urlpatterns = [
    path("", home, name="home"),
    path("batch/<int:pk>/", batch, name="batch"),
    path("batch/new/", new_batch, name="new_batch"),
    path("login/", user_login, name="login"),
    path("user/", user_view, name="user" ),
    path('logout/', logout_view, name='logout'),
]
