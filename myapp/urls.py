from django.urls import path

from .import views

urlpatterns = [
    path('',views.index,name="index"),
    path('show_employee_details/',views.View,name="view"),
    path('add_new_employee/',views.Add,name="add"),
    path('modify_employee/<id>/',views.Edit,name="edit"),
    path('update/<id>',views.Update,name="update"),
    path('delete_emp/<id>',views.Deleting,name="delete"),
]
