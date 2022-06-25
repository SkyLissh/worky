from django.urls import path

from app.employees.views import EmployeeUpdateView

urlpatterns = [
    path("update/<uuid:pk>", EmployeeUpdateView.as_view(), name="update"),
]
