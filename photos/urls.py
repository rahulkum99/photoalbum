from django.urls import path
from . import views
urlpatterns = [
    path('',views.gallery, name="gallery"),
    path('view-photo/<str:pk>/',views.viewPhoto , name="view-photo"),
    path('add-photo',views.addPhoto,name="add-photo"),
]