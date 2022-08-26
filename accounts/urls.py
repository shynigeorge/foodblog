from django.urls import path

from accounts import views

urlpatterns=[
    path('register',views.registered,name="registered"),
    path('login',views.loged,name="login"),
    path('logout', views.logout, name="logout")

]