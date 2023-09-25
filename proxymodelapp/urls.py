from django.urls import path
from . import views as proxy_views
from django.contrib.auth.views import LoginView

app_name = "proxymodelapp"

urlpatterns = [
    path("",proxy_views.homePage,name='homepage'),
    path("login/",LoginView.as_view(template_name="proxymodelapp/loginpage.html"),name='proxylogin')
   
]
