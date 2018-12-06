from typing import Any, Dict, List, Optional, Set, Tuple, Type, Union

from django.contrib.postgres.fields.citext import CIText
from django.db.backends.sqlite3.schema import DatabaseSchemaEditor
from django.db.migrations.operations.base import Operation
from django.db.migrations.state import ProjectState
from django.db.models.fields import Field
from django.db.models.indexes import Index
from django.db.models.manager import Manager

class ModelOperation(Operation):
    name: Any = ...
    def __init__(self, name: str) -> None: ...
    def name_lower(self) -> str: ...
    def references_model(self, name: str, app_label: Optional[str] = ...) -> bool: ...
    def reduce(self, operation: Operation, in_between: List[Operation], app_label: str = ...) -> bool: ...

class CreateModel(ModelOperation):
    serialization_expand_args: Any = ...
    fields: Any = ...
    options: Any = ...
    bases: Any = ...
    managers: Any = ...
    def __init__(
        self,
        name: str,
        fields: List[Tuple[str, Union[CIText, Field]]],
        options: Optional[Dict[str, Any]] = ...,
        bases: Optional[Union[Tuple[Type[Any], ...], Tuple[str, ...]]] = ...,
        managers: Optional[List[Tuple[str, Manager]]] = ...,
    ) -> None: ...
    def deconstruct(self) -> Tuple[str, List[Any], Dict[str, Union[Dict[str, str], List[Tuple[str, Field]], str]]]: ...
    def state_forwards(self, app_label: str, state: ProjectState) -> None: ...
    def database_forwards(
        self, app_label: str, schema_editor: DatabaseSchemaEditor, from_state: ProjectState, to_state: ProjectState
    ) -> None: ...
    def database_backwards(
        self, app_label: str, schema_editor: DatabaseSchemaEditor, from_state: ProjectState, to_state: ProjectState
    ) -> None: ...
    def describe(self) -> str: ...
    def references_model(self, name: str, app_label: str = ...) -> bool: ...
    def model_to_key(self, model: str) -> List[str]: ...
    def reduce(
        self, operation: Operation, in_between: List[Operation], app_label: str = ...
    ) -> Union[List[CreateModel], bool]: ...

class DeleteModel(ModelOperation):
    def deconstruct(self) -> Tuple[str, List[Any], Dict[str, str]]: ...
    def state_forwards(self, app_label: str, state: ProjectState) -> None: ...
    def database_forwards(
        self, app_label: str, schema_editor: DatabaseSchemaEditor, from_state: ProjectState, to_state: ProjectState
    ) -> None: ...
    def database_backwards(
        self, app_label: str, schema_editor: DatabaseSchemaEditor, from_state: ProjectState, to_state: ProjectState
    ) -> None: ...
    def describe(self) -> str: ...

class RenameModel(ModelOperation):
    old_name: Any = ...
    new_name: Any = ...
    def __init__(self, old_name: str, new_name: str) -> None: ...
    def old_name_lower(self) -> str: ...
    def new_name_lower(self) -> str: ...
    def deconstruct(self): ...
    def state_forwards(self, app_label: str, state: ProjectState) -> None: ...
    def database_forwards(
        self, app_label: str, schema_editor: DatabaseSchemaEditor, from_state: ProjectState, to_state: ProjectState
    ) -> None: ...
    def database_backwards(
        self, app_label: str, schema_editor: DatabaseSchemaEditor, from_state: ProjectState, to_state: ProjectState
    ) -> None: ...
    def references_model(self, name: Any, app_label: Optional[Any] = ...): ...
    def describe(self): ...
    def reduce(self, operation: AlterModelTable, in_between: List[Any], app_label: str = ...) -> bool: ...

class AlterModelTable(ModelOperation):
    table: Any = ...
    def __init__(self, name: str, table: Optional[str]) -> None: ...
    def deconstruct(self): ...
    def state_forwards(self, app_label: Any, state: Any) -> None: ...
    def database_forwards(self, app_label: Any, schema_editor: Any, from_state: Any, to_state: Any) -> None: ...
    def database_backwards(self, app_label: Any, schema_editor: Any, from_state: Any, to_state: Any): ...
    def describe(self): ...
    def reduce(self, operation: Any, in_between: Any, app_label: Optional[Any] = ...): ...

class ModelOptionOperation(ModelOperation):
    def reduce(self, operation: Operation, in_between: List[DeleteModel], app_label: str = ...) -> bool: ...

class FieldRelatedOptionOperation(ModelOptionOperation):
    def reduce(
        self, operation: Operation, in_between: List[Any], app_label: str = ...
    ) -> Union[List[Operation], bool]: ...

class AlterUniqueTogether(FieldRelatedOptionOperation):
    option_name: str = ...
    unique_together: Any = ...
    def __init__(self, name: str, unique_together: Set[Tuple[str, ...]]) -> None: ...
    def deconstruct(self) -> Tuple[str, List[Any], Dict[str, Union[Set[Tuple[str, str]], str]]]: ...
    def state_forwards(self, app_label: str, state: ProjectState) -> None: ...
    def database_forwards(
        self, app_label: str, schema_editor: DatabaseSchemaEditor, from_state: ProjectState, to_state: ProjectState
    ) -> None: ...
    def database_backwards(
        self, app_label: str, schema_editor: DatabaseSchemaEditor, from_state: ProjectState, to_state: ProjectState
    ) -> None: ...
    def references_field(self, model_name: str, name: str, app_label: Optional[str] = ...) -> bool: ...
    def describe(self) -> str: ...

class AlterIndexTogether(FieldRelatedOptionOperation):
    option_name: str = ...
    index_together: Any = ...
    def __init__(self, name: str, index_together: Set[Tuple[str, str]]) -> None: ...
    def deconstruct(self): ...
    def state_forwards(self, app_label: Any, state: Any) -> None: ...
    def database_forwards(self, app_label: Any, schema_editor: Any, from_state: Any, to_state: Any) -> None: ...
    def database_backwards(self, app_label: Any, schema_editor: Any, from_state: Any, to_state: Any): ...
    def references_field(self, model_name: str, name: str, app_label: Optional[str] = ...) -> bool: ...
    def describe(self): ...

class AlterOrderWithRespectTo(FieldRelatedOptionOperation):
    name: str
    order_with_respect_to: str = ...
    def __init__(self, name: str, order_with_respect_to: str) -> None: ...
    def deconstruct(self): ...
    def state_forwards(self, app_label: Any, state: Any) -> None: ...
    def database_forwards(self, app_label: Any, schema_editor: Any, from_state: Any, to_state: Any) -> None: ...
    def database_backwards(self, app_label: Any, schema_editor: Any, from_state: Any, to_state: Any) -> None: ...
    def references_field(self, model_name: str, name: str, app_label: None = ...) -> bool: ...
    def describe(self): ...

class AlterModelOptions(ModelOptionOperation):
    ALTER_OPTION_KEYS: Any = ...
    options: Any = ...
    def __init__(self, name: str, options: Dict[str, str]) -> None: ...
    def deconstruct(self): ...
    def state_forwards(self, app_label: Any, state: Any) -> None: ...
    def database_forwards(self, app_label: Any, schema_editor: Any, from_state: Any, to_state: Any) -> None: ...
    def database_backwards(self, app_label: Any, schema_editor: Any, from_state: Any, to_state: Any) -> None: ...
    def describe(self): ...

class AlterModelManagers(ModelOptionOperation):
    serialization_expand_args: Any = ...
    managers: Any = ...
    def __init__(self, name: Any, managers: Any) -> None: ...
    def deconstruct(self): ...
    def state_forwards(self, app_label: Any, state: Any) -> None: ...
    def database_forwards(self, app_label: Any, schema_editor: Any, from_state: Any, to_state: Any) -> None: ...
    def database_backwards(self, app_label: Any, schema_editor: Any, from_state: Any, to_state: Any) -> None: ...
    def describe(self): ...

class IndexOperation(Operation):
    option_name: str = ...
    def model_name_lower(self): ...

class AddIndex(IndexOperation):
    model_name: str = ...
    index: django.db.models.indexes.Index = ...
    def __init__(self, model_name: str, index: Index) -> None: ...
    def state_forwards(self, app_label: Any, state: Any) -> None: ...
    def database_forwards(self, app_label: Any, schema_editor: Any, from_state: Any, to_state: Any) -> None: ...
    def database_backwards(self, app_label: Any, schema_editor: Any, from_state: Any, to_state: Any) -> None: ...
    def deconstruct(self): ...
    def describe(self): ...

class RemoveIndex(IndexOperation):
    model_name: str = ...
    name: str = ...
    def __init__(self, model_name: str, name: str) -> None: ...
    def state_forwards(self, app_label: Any, state: Any) -> None: ...
    def database_forwards(self, app_label: Any, schema_editor: Any, from_state: Any, to_state: Any) -> None: ...
    def database_backwards(self, app_label: Any, schema_editor: Any, from_state: Any, to_state: Any) -> None: ...
    def deconstruct(self): ...
    def describe(self): ...
