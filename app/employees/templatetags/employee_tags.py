from django.template import Library

from app.employees.models import Employee

register = Library()


@register.filter
def job_name(employee: Employee) -> str:
    """
    Returns the job name of the employee.
    """
    return [x[1] for x in employee.JOBS if x[0] == employee.job][0]
