from typing import TYPE_CHECKING, Sequence, TypeAlias
from uuid import UUID, uuid4

from django.db.models import (
    CASCADE,
    CharField,
    ForeignKey,
    ImageField,
    ManyToManyField,
    Model,
    QuerySet,
    UUIDField,
)
from django.db.models.expressions import Combinable
from django.db.models.manager import Manager

if TYPE_CHECKING:
    from django.db.models.manager import RelatedManager

from app.departments.models import Department

_UUIDField: TypeAlias = UUIDField[UUID | str | None, UUID]
_CharField: TypeAlias = CharField[str | int | Combinable, str]
_ForeignKey: TypeAlias = ForeignKey[Department | Combinable, Department]

if TYPE_CHECKING:
    _ManyToManyField: TypeAlias = ManyToManyField[
        Sequence["Skill"], RelatedManager["Skill"]
    ]


class Skill(Model):
    id: _UUIDField = UUIDField(primary_key=True, default=uuid4, editable=False)

    skill: _CharField = CharField("Skill", max_length=50)

    def __str__(self) -> str:
        return f"{self.skill}"


class Employee(Model):
    JOBS = (
        ("S", "Software Engineer"),
        ("D", "Data Analyst"),
        ("Q", "Quality Assurance"),
        ("M", "Manager"),
        ("P", "Project Manager"),
        ("E", "Executive"),
    )

    id: _UUIDField = UUIDField(primary_key=True, default=uuid4, editable=False)

    first_name: _CharField = CharField("First name", max_length=50)
    last_name: _CharField = CharField("Last name", max_length=50)
    job: _CharField = CharField("Job", max_length=1, choices=JOBS)
    avatar = ImageField("Avatar", upload_to="employees/avatars/", blank=True, null=True)

    department: _ForeignKey = ForeignKey(Department, on_delete=CASCADE)
    skills: "_ManyToManyField" = ManyToManyField(Skill)

    objects: Manager["Employee"] = QuerySet.as_manager()

    def __str__(self) -> str:
        return f"{self.id} - {self.first_name} {self.last_name}"
