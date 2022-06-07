from django.urls import path
from .views import registration, mylogin, mylogout, registration1
from . import views

urlpatterns = [
    path('register/',registration,name="register"),
    # path('register1/',registration1,name="register1"),
    path('register1/', views.registration1, name="register1"),
    path('login/',mylogin,name="login"),
    path('logout/',mylogout,name='logout'),
]
