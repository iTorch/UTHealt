from django.urls import path
app_name='user'
from apps.user.views import *

urlpatterns = [
    path('registro/', SolicitudCreate.as_view(), name ='registro'),
    path('login/',LoginFormView.as_view(), name='login'),
    path('logout/' ,logout_view.as_view(), name='logout'),
    path('index/', index, name='index'),
]