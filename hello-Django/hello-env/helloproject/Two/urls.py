from django.urls import path

from Two import views

urlpatterns = [
    path('index/', views.index),
    path('addstudent/',views.add_student),
    path('getstudents/',views.get_students),
]
