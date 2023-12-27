from django.urls import path
from pages.views import home, create_reservation

app_name = 'pages'
urlpatterns = [
    path('', home , name='home'),
    path('reservation/', create_reservation , name='reservation'),
]