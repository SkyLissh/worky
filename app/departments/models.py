from typing import TypeAlias
from uuid import UUID, uuid4

from django.db.models import BooleanField, CharField, Model, QuerySet, UUIDField
from django.db.models.expressions import Combinable
from django.db.models.manager import Manager

_UUIDField = UUIDField[UUID | str | None, UUID]
_CharField: TypeAlias = CharField[str | int | Combinable, str]
_BooleanField: TypeAlias = BooleanField[bool | Combinable, bool]


class Department(Model):
    id: _UUIDField = UUIDField(primary_key=True, default=uuid4, editable=False)

    name: _CharField = CharField("Name", max_length=50)
    short_name: _CharField = CharField("Short name", max_length=20)
    active: _BooleanField = BooleanField("Active", default=True)

    objects: Manager["Department"] = QuerySet.as_manager()

    def __str__(self) -> str:
        return self.name
