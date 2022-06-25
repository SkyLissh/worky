from django.contrib import admin

from app.employees.models import Employee, Skill


# Register your models here.
class EmployeeAdmin(admin.ModelAdmin[Employee]):
    list_display: tuple[str, ...] = ("first_name", "last_name", "job")

    search_fields: tuple[str] = ("first_name",)
    list_filter: tuple[str] = ("job",)

    filter_horizontal: tuple[str] = ("skills",)


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Skill)
