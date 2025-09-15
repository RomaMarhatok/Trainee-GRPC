from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GRPCNoteMessage(_message.Message):
    __slots__ = ("uuididf", "userUuididf", "name", "message")
    UUIDIDF_FIELD_NUMBER: _ClassVar[int]
    USERUUIDIDF_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    uuididf: str
    userUuididf: str
    name: str
    message: str
    def __init__(self, uuididf: _Optional[str] = ..., userUuididf: _Optional[str] = ..., name: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class GRPCCreateNoteMessage(_message.Message):
    __slots__ = ("uuididf", "name", "message", "userUuididf")
    UUIDIDF_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    USERUUIDIDF_FIELD_NUMBER: _ClassVar[int]
    uuididf: str
    name: str
    message: str
    userUuididf: str
    def __init__(self, uuididf: _Optional[str] = ..., name: _Optional[str] = ..., message: _Optional[str] = ..., userUuididf: _Optional[str] = ...) -> None: ...

class GRPCUpdateNoteMessage(_message.Message):
    __slots__ = ("uuididf", "name", "message")
    UUIDIDF_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    uuididf: str
    name: str
    message: str
    def __init__(self, uuididf: _Optional[str] = ..., name: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class GRPCDeleteNoteMessage(_message.Message):
    __slots__ = ("uuididf",)
    UUIDIDF_FIELD_NUMBER: _ClassVar[int]
    uuididf: str
    def __init__(self, uuididf: _Optional[str] = ...) -> None: ...

class GRPCGetNoteMessage(_message.Message):
    __slots__ = ("uuididf",)
    UUIDIDF_FIELD_NUMBER: _ClassVar[int]
    uuididf: str
    def __init__(self, uuididf: _Optional[str] = ...) -> None: ...

class GRPCGetListNoteMessage(_message.Message):
    __slots__ = ("userUuididf",)
    USERUUIDIDF_FIELD_NUMBER: _ClassVar[int]
    userUuididf: str
    def __init__(self, userUuididf: _Optional[str] = ...) -> None: ...

class GRPCNoteListMessage(_message.Message):
    __slots__ = ("notes",)
    NOTES_FIELD_NUMBER: _ClassVar[int]
    notes: _containers.RepeatedCompositeFieldContainer[GRPCNoteMessage]
    def __init__(self, notes: _Optional[_Iterable[_Union[GRPCNoteMessage, _Mapping]]] = ...) -> None: ...
