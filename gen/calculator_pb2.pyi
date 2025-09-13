from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CalculateOperationMessage(_message.Message):
    __slots__ = ("first_number", "oper", "second_number")
    FIRST_NUMBER_FIELD_NUMBER: _ClassVar[int]
    OPER_FIELD_NUMBER: _ClassVar[int]
    SECOND_NUMBER_FIELD_NUMBER: _ClassVar[int]
    first_number: float
    oper: str
    second_number: float

    def __init__(
        self,
        first_number: _Optional[float] = ...,
        oper: _Optional[str] = ...,
        second_number: _Optional[float] = ...,
    ) -> None: ...

class CalculatedMessage(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: float
    def __init__(self, result: _Optional[float] = ...) -> None: ...
