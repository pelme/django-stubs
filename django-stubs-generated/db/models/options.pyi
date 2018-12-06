from typing import Any, Callable, Dict, Iterator, List, Optional, Set, Tuple, Type, Union

from django.apps.config import AppConfig
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.postgres.fields.array import ArrayField
from django.contrib.postgres.fields.citext import CIText
from django.contrib.sessions.base_session import AbstractBaseSession
from django.db.backends.sqlite3.base import DatabaseWrapper
from django.db.models.base import Model
from django.db.models.fields import Field
from django.db.models.fields.mixins import FieldCacheMixin
from django.db.models.fields.related import OneToOneField
from django.db.models.fields.reverse_related import ForeignObjectRel
from django.db.models.manager import Manager
from django.db.models.query_utils import PathInfo
from django.utils.datastructures import ImmutableList

PROXY_PARENTS: Any
EMPTY_RELATION_TREE: Any
IMMUTABLE_WARNING: str
DEFAULT_NAMES: Any

def normalize_together(
    option_together: Any
) -> Union[List[Union[Tuple[str, str], int]], Set[Tuple[str, str]], Tuple, int, str]: ...
def make_immutable_fields_list(
    name: str, data: Union[Iterator[Any], List[Union[ArrayField, CIText]], List[Union[Field, FieldCacheMixin]]]
) -> ImmutableList: ...

class Options:
    base_manager: django.db.models.manager.Manager
    concrete_fields: django.utils.datastructures.ImmutableList
    default_manager: django.db.models.manager.Manager
    fields: django.utils.datastructures.ImmutableList
    local_concrete_fields: django.utils.datastructures.ImmutableList
    managers: django.utils.datastructures.ImmutableList
    managers_map: Dict[str, django.db.models.manager.Manager]
    related_objects: django.utils.datastructures.ImmutableList
    FORWARD_PROPERTIES: Any = ...
    REVERSE_PROPERTIES: Any = ...
    default_apps: Any = ...
    local_fields: List[django.db.models.fields.Field] = ...
    local_many_to_many: List[django.db.models.fields.related.ManyToManyField] = ...
    private_fields: List[Any] = ...
    local_managers: List[django.db.models.manager.Manager] = ...
    base_manager_name: None = ...
    default_manager_name: None = ...
    model_name: Optional[str] = ...
    verbose_name: Optional[str] = ...
    verbose_name_plural: Optional[str] = ...
    db_table: str = ...
    ordering: List[str] = ...
    indexes: List[Any] = ...
    unique_together: Union[List[Any], Tuple] = ...
    index_together: Union[List[Any], Tuple] = ...
    select_on_save: bool = ...
    default_permissions: Tuple[str, str, str, str] = ...
    permissions: List[Any] = ...
    object_name: Optional[str] = ...
    app_label: str = ...
    get_latest_by: None = ...
    order_with_respect_to: None = ...
    db_tablespace: str = ...
    required_db_features: List[Any] = ...
    required_db_vendor: None = ...
    meta: Optional[
        Type[
            Union[
                django.contrib.auth.base_user.AbstractBaseUser.Meta,
                django.contrib.auth.models.AbstractUser.Meta,
                django.contrib.auth.models.PermissionsMixin.Meta,
                django.contrib.sessions.base_session.AbstractBaseSession.Meta,
            ]
        ]
    ] = ...
    pk: Optional[django.db.models.fields.Field] = ...
    auto_field: Optional[django.db.models.fields.AutoField] = ...
    abstract: bool = ...
    managed: bool = ...
    proxy: bool = ...
    proxy_for_model: None = ...
    concrete_model: Optional[Type[django.db.models.base.Model]] = ...
    swappable: None = ...
    parents: collections.OrderedDict = ...
    auto_created: bool = ...
    related_fkey_lookups: List[Any] = ...
    apps: django.apps.registry.Apps = ...
    default_related_name: None = ...
    def __init__(
        self,
        meta: Optional[
            Type[Union[AbstractBaseUser.Meta, AbstractUser.Meta, PermissionsMixin.Meta, AbstractBaseSession.Meta]]
        ],
        app_label: Optional[str] = ...,
    ) -> None: ...
    @property
    def label(self) -> str: ...
    @property
    def label_lower(self) -> str: ...
    @property
    def app_config(self) -> AppConfig: ...
    @property
    def installed(self): ...
    model: Type[django.db.models.base.Model] = ...
    original_attrs: Dict[str, Union[List[str], django.apps.registry.Apps, str]] = ...
    def contribute_to_class(self, cls: Type[Model], name: str) -> None: ...
    def add_manager(self, manager: Manager) -> None: ...
    def add_field(self, field: Union[GenericForeignKey, Field], private: bool = ...) -> None: ...
    def setup_pk(self, field: Field) -> None: ...
    def setup_proxy(self, target: Type[Model]) -> None: ...
    def can_migrate(self, connection: Union[DatabaseWrapper, str]) -> bool: ...
    @property
    def verbose_name_raw(self) -> Any: ...
    @property
    def swapped(self) -> Optional[str]: ...
    def managers(self) -> ImmutableList: ...
    def managers_map(self) -> Dict[str, Manager]: ...
    def base_manager(self) -> Manager: ...
    def default_manager(self) -> Manager: ...
    def fields(self) -> ImmutableList: ...
    def concrete_fields(self) -> ImmutableList: ...
    def local_concrete_fields(self) -> ImmutableList: ...
    def many_to_many(self) -> ImmutableList: ...
    def related_objects(self) -> ImmutableList: ...
    def fields_map(self) -> Dict[str, ForeignObjectRel]: ...
    def get_field(self, field_name: Union[Callable, str]) -> Union[Field, mixins.FieldCacheMixin]: ...
    def get_base_chain(self, model: Type[Model]) -> List[Type[Model]]: ...
    def get_parent_list(self) -> List[Type[Model]]: ...
    def get_ancestor_link(self, ancestor: Type[Model]) -> Optional[OneToOneField]: ...
    def get_path_to_parent(self, parent: Type[Model]) -> List[PathInfo]: ...
    def get_path_from_parent(self, parent: Type[Model]) -> List[PathInfo]: ...
    def get_fields(self, include_parents: bool = ..., include_hidden: bool = ...) -> ImmutableList: ...
