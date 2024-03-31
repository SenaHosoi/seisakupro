from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path("top", views.index, name="top"),
    path("", views.index, name="top"),
    path("itiran", views.index2, name="itiran"),
    path("touroku", views.index3, name="touroku"),
    path("toukou", views.index4, name="toukou"),
    
]
#sena
#3141