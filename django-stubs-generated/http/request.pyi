from io import BytesIO
from typing import Any, Dict, Iterator, List, Optional, Tuple, Union, Callable

from django.contrib.sessions.backends.db import SessionStore
from django.core.handlers.wsgi import WSGIRequest
from django.utils.datastructures import MultiValueDict

RAISE_ERROR: Any
host_validation_re: Any

class UnreadablePostError(IOError): ...
class RawPostDataException(Exception): ...

class HttpRequest:
    csrf_cookie_needs_reset: bool
    csrf_processing_done: bool
    get_host: Callable
    sensitive_post_parameters: str
    session: SessionStore
    GET: Union[Dict[str, str], QueryDict] = ...
    POST: Union[Dict[str, str], QueryDict] = ...
    COOKIES: Dict[str, str] = ...
    META: Dict[str, Union[int, str]] = ...
    FILES: MultiValueDict = ...
    path: str = ...
    path_info: str = ...
    method: Optional[str] = ...
    resolver_match: None = ...
    content_type: None = ...
    content_params: None = ...
    def __init__(self) -> None: ...
    def get_host(self) -> str: ...
    def get_port(self) -> str: ...
    def get_full_path(self, force_append_slash: bool = ...) -> str: ...
    def get_full_path_info(self, force_append_slash: bool = ...) -> str: ...
    def get_signed_cookie(
        self, key: str, default: Any = ..., salt: str = ..., max_age: Optional[int] = ...
    ) -> Optional[str]: ...
    def get_raw_uri(self) -> str: ...
    def build_absolute_uri(self, location: Optional[str] = ...) -> str: ...
    @property
    def scheme(self) -> Optional[str]: ...
    def is_secure(self) -> bool: ...
    def is_ajax(self) -> bool: ...
    @property
    def encoding(self): ...
    @encoding.setter
    def encoding(self, val: Any) -> None: ...
    @property
    def upload_handlers(self): ...
    @upload_handlers.setter
    def upload_handlers(self, upload_handlers: Any) -> None: ...
    upload_handlers: Any = ...
    def parse_file_upload(
        self, META: Dict[str, Any], post_data: Union[BytesIO, WSGIRequest]
    ) -> Tuple[QueryDict, MultiValueDict]: ...
    @property
    def body(self) -> bytes: ...
    def close(self) -> None: ...
    def read(self, *args: Any, **kwargs: Any) -> bytes: ...
    def readline(self, *args: Any, **kwargs: Any) -> bytes: ...
    def __iter__(self) -> Iterator[bytes]: ...
    def xreadlines(self) -> None: ...
    def readlines(self): ...

class QueryDict(MultiValueDict):
    encoding: Any = ...
    def __init__(
        self, query_string: Optional[Union[bytes, str]] = ..., mutable: bool = ..., encoding: Optional[str] = ...
    ) -> None: ...
    @classmethod
    def fromkeys(
        cls,
        iterable: Union[List[bytes], List[str], int, str],
        value: Union[bytes, str] = ...,
        mutable: bool = ...,
        encoding: Optional[str] = ...,
    ) -> QueryDict: ...
    @property
    def encoding(self): ...
    @encoding.setter
    def encoding(self, value: Any) -> None: ...
    def __setitem__(self, key: str, value: Optional[Union[int, str]]) -> None: ...
    def __delitem__(self, key: str) -> None: ...
    def __copy__(self) -> QueryDict: ...
    def __deepcopy__(self, memo: Dict[Any, Any]) -> QueryDict: ...
    def setlist(self, key: str, list_: List[str]) -> None: ...
    def setlistdefault(self, key: str, default_list: None = ...) -> List[str]: ...
    def appendlist(self, key: Union[bytes, str], value: Union[List[str], bytes, str]) -> None: ...
    def pop(self, key: str, *args: Any) -> Optional[Union[List[str], str]]: ...
    def popitem(self) -> Any: ...
    def clear(self) -> None: ...
    def setdefault(self, key: str, default: str = ...) -> str: ...
    def copy(self) -> QueryDict: ...
    def urlencode(self, safe: Optional[str] = ...) -> str: ...

def bytes_to_text(s: Optional[Union[bytes, int, str]], encoding: str) -> Optional[Union[int, str]]: ...
def split_domain_port(host: str) -> Tuple[str, str]: ...
def validate_host(host: str, allowed_hosts: Union[List[str], str]) -> bool: ...
