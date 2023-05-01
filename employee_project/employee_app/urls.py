from django.urls import path
from . import views
urlpatterns = [
    path('',views.employee_form, name='employee_insert'),#localhost:8000/employee
    path('<int:id>/',views.employee_form,name='employee_update'),#localhost:8000/employee/list
    path('list/',views.employee_list, name='employee_list'), #localhost:8000/employee/list
    path('delete/<int:id>/',views.employee_delete,name='employee_delete')
]
