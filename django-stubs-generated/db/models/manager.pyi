from collections import OrderedDict
from datetime import date, datetime
from decimal import Decimal
from typing import Any, Dict, List, Optional, Tuple, Type, Union, TypeVar, Set, Generic
from unittest.mock import MagicMock

from django.contrib.sites.managers import CurrentSiteManager
from django.db.models import Q
from django.db.models.base import Model
from django.db.models.query import QuerySet, RawQuerySet

_T = TypeVar("_T", bound=Model)

class BaseManager:
    creation_counter: int = ...
    auto_created: bool = ...
    use_in_migrations: bool = ...
    def __new__(cls: Type[Manager], *args: Any, **kwargs: Any) -> Manager: ...
    model: Any = ...
    name: Any = ...
    def __init__(self) -> None: ...
    def deconstruct(self) -> Tuple[bool, str, None, Tuple, Dict[str, int]]: ...
    def check(self, **kwargs: Any) -> List[Any]: ...
    @classmethod
    def from_queryset(cls, queryset_class: Any, class_name: Optional[Any] = ...): ...
    def contribute_to_class(self, model: Type[Model], name: str) -> None: ...
    def db_manager(self, using: Optional[str] = ..., hints: Optional[Dict[str, Model]] = ...) -> Manager: ...
    @property
    def db(self) -> str: ...
    def get_queryset(self) -> QuerySet: ...
    def all(self) -> QuerySet: ...
    def __eq__(self, other: Optional[CurrentSiteManager]) -> bool: ...
    def __hash__(self): ...

class Manager(Generic[_T]):
    def exists(self) -> bool: ...
    def explain(self, *, format: Optional[Any] = ..., **options: Any) -> str: ...
    def raw(
        self,
        raw_query: str,
        params: Optional[Union[Dict[str, str], List[datetime], List[Decimal], List[str], Set[str], Tuple[int]]] = ...,
        translations: Optional[Dict[str, str]] = ...,
        using: None = ...,
    ) -> RawQuerySet: ...
    def values(self, *fields: Any, **expressions: Any) -> QuerySet: ...
    def values_list(self, *fields: Any, flat: bool = ..., named: bool = ...) -> QuerySet: ...
    def dates(self, field_name: str, kind: str, order: str = ...) -> QuerySet: ...
    def datetimes(self, field_name: str, kind: str, order: str = ..., tzinfo: None = ...) -> QuerySet: ...
    def none(self) -> QuerySet[_T]: ...
    def all(self) -> QuerySet[_T]: ...
    def filter(self, *args: Any, **kwargs: Any) -> QuerySet[_T]: ...
    def exclude(self, *args: Any, **kwargs: Any) -> QuerySet[_T]: ...
    def complex_filter(
        self, filter_obj: Union[Dict[str, datetime], Dict[str, QuerySet], Q, MagicMock]
    ) -> QuerySet[_T]: ...
    def union(self, *other_qs: Any, all: bool = ...) -> QuerySet[_T]: ...
    def intersection(self, *other_qs: Any) -> QuerySet[_T]: ...
    def difference(self, *other_qs: Any) -> QuerySet[_T]: ...
    def select_for_update(self, nowait: bool = ..., skip_locked: bool = ..., of: Tuple = ...) -> QuerySet: ...
    def select_related(self, *fields: Any) -> QuerySet[_T]: ...
    def prefetch_related(self, *lookups: Any) -> QuerySet[_T]: ...
    def annotate(self, *args: Any, **kwargs: Any) -> QuerySet[_T]: ...
    def order_by(self, *field_names: Any) -> QuerySet[_T]: ...
    def distinct(self, *field_names: Any) -> QuerySet[_T]: ...
    def extra(
        self,
        select: Optional[Union[Dict[str, int], Dict[str, str], OrderedDict]] = ...,
        where: Optional[List[str]] = ...,
        params: Optional[Union[List[int], List[str]]] = ...,
        tables: Optional[List[str]] = ...,
        order_by: Optional[Union[List[str], Tuple[str]]] = ...,
        select_params: Optional[Union[List[int], List[str], Tuple[int]]] = ...,
    ) -> QuerySet[_T]: ...
    def iterator(self, chunk_size: int = ...) -> Iterator[_T]: ...
    def aggregate(self, *args: Any, **kwargs: Any) -> Dict[str, Optional[Union[datetime, float]]]: ...
    def count(self) -> int: ...
    def get(self, *args: Any, **kwargs: Any) -> _T: ...
    def create(self, **kwargs: Any) -> _T: ...

class ManagerDescriptor:
    manager: Manager = ...
    def __init__(self, manager: Manager) -> None: ...
    def __get__(self, instance: Optional[Model], cls: Type[Model] = ...) -> Manager: ...

class EmptyManager(Manager):
    creation_counter: int
    name: None
    model: Optional[Type[Model]] = ...
    def __init__(self, model: Type[Model]) -> None: ...
    def get_queryset(self) -> QuerySet: ...
