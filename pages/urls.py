from django.urls import path
from pages.views import home, menu

app_name = 'pages'
urlpatterns = [
    path('', home , name='home'),
    path('menu', menu, name='menu'),
]