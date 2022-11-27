from django.urls import path

from .import views

urlpatterns = [
    path('',views.index,name="index"),
    path('/show_employee_details/',views.View,name="view"),
    path('/add_new_employee/',views.Add,name="add"),
    path('/update_employee/',views.Edit,name="edit"),
]
