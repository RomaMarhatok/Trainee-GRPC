from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GRPCNoteMessage(_message.Message):
    __slots__ = ("uuid", "user_uuid", "name", "message")
    UUID_FIELD_NUMBER: _ClassVar[int]
    USER_UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    user_uuid: str
    name: str
    message: str
    def __init__(
        self,
        uuid: _Optional[str] = ...,
        user_uuid: _Optional[str] = ...,
        name: _Optional[str] = ...,
        message: _Optional[str] = ...,
    ) -> None: ...

class GRPCCreateNoteMessage(_message.Message):
    __slots__ = ("name", "message", "user_uuid")
    NAME_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    USER_UUID_FIELD_NUMBER: _ClassVar[int]
    name: str
    message: str
    user_uuid: str
    def __init__(
        self,
        name: _Optional[str] = ...,
        message: _Optional[str] = ...,
        user_uuid: _Optional[str] = ...,
    ) -> None: ...

class GRPCUpdateNoteMessage(_message.Message):
    __slots__ = ("uuid", "name", "message")
    UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    name: str
    message: str
    def __init__(
        self,
        uuid: _Optional[str] = ...,
        name: _Optional[str] = ...,
        message: _Optional[str] = ...,
    ) -> None: ...

class GRPCDeleteNoteMessage(_message.Message):
    __slots__ = ("uuid",)
    UUID_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    def __init__(self, uuid: _Optional[str] = ...) -> None: ...

class GRPCGetNoteMessage(_message.Message):
    __slots__ = ("uuid",)
    UUID_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    def __init__(self, uuid: _Optional[str] = ...) -> None: ...

class GRPCGetListNoteMessage(_message.Message):
    __slots__ = ("user_uuid",)
    USER_UUID_FIELD_NUMBER: _ClassVar[int]
    user_uuid: str
    def __init__(self, user_uuid: _Optional[str] = ...) -> None: ...

class GRPCNoteListMessage(_message.Message):
    __slots__ = ("notes",)
    NOTES_FIELD_NUMBER: _ClassVar[int]
    notes: _containers.RepeatedCompositeFieldContainer[GRPCNoteMessage]
    def __init__(
        self, notes: _Optional[_Iterable[_Union[GRPCNoteMessage, _Mapping]]] = ...
    ) -> None: ...
