from django.urls import path
from .views import registration, mylogin, mylogout

urlpatterns = [
    path('register/',registration,name="register"),
    path('login/',mylogin,name="login"),
    path('logout/',mylogout,name='logout'),
]
