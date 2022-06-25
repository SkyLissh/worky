from django.db.models.query import QuerySet
from django.forms import ModelForm
from django.views.generic import ListView, UpdateView

from app.employees.models import Employee


# Create your views here.
class EmployeeForm(ModelForm[Employee]):
    class Meta:
        model = Employee
        fields = "__all__"


class HomePageView(ListView[Employee]):
    model = Employee

    template_name: str = "employees/home.html"
    context_object_name: str = "employees"

    def get_queryset(self) -> QuerySet[Employee]:
        kword: str | None = self.request.GET.get("q")
        queryset: QuerySet[Employee] = Employee.objects.all()

        if kword:
            queryset = Employee.objects.filter(first_name__icontains=kword)

        return queryset


class EmployeeUpdateView(UpdateView[Employee, EmployeeForm]):
    model = Employee
    template_name = "employees/update.html"
    form_class = EmployeeForm
    success_url = "/"
