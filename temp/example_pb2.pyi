from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExampleEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FIRST_OPTION: _ClassVar[ExampleEnum]
    SECOND_OPTION: _ClassVar[ExampleEnum]
FIRST_OPTION: ExampleEnum
SECOND_OPTION: ExampleEnum

class NestedMessage(_message.Message):
    __slots__ = ("nested_int", "nested_string")
    NESTED_INT_FIELD_NUMBER: _ClassVar[int]
    NESTED_STRING_FIELD_NUMBER: _ClassVar[int]
    nested_int: int
    nested_string: str
    def __init__(self, nested_int: _Optional[int] = ..., nested_string: _Optional[str] = ...) -> None: ...

class ExampleMessage(_message.Message):
    __slots__ = ("int_field", "string_field", "bytes_field", "enum_field", "nested_message_field", "repeated_int_field", "repeated_nested_message_field")
    INT_FIELD_FIELD_NUMBER: _ClassVar[int]
    STRING_FIELD_FIELD_NUMBER: _ClassVar[int]
    BYTES_FIELD_FIELD_NUMBER: _ClassVar[int]
    ENUM_FIELD_FIELD_NUMBER: _ClassVar[int]
    NESTED_MESSAGE_FIELD_FIELD_NUMBER: _ClassVar[int]
    REPEATED_INT_FIELD_FIELD_NUMBER: _ClassVar[int]
    REPEATED_NESTED_MESSAGE_FIELD_FIELD_NUMBER: _ClassVar[int]
    int_field: int
    string_field: str
    bytes_field: bytes
    enum_field: ExampleEnum
    nested_message_field: NestedMessage
    repeated_int_field: _containers.RepeatedScalarFieldContainer[int]
    repeated_nested_message_field: _containers.RepeatedCompositeFieldContainer[NestedMessage]
    def __init__(self, int_field: _Optional[int] = ..., string_field: _Optional[str] = ..., bytes_field: _Optional[bytes] = ..., enum_field: _Optional[_Union[ExampleEnum, str]] = ..., nested_message_field: _Optional[_Union[NestedMessage, _Mapping]] = ..., repeated_int_field: _Optional[_Iterable[int]] = ..., repeated_nested_message_field: _Optional[_Iterable[_Union[NestedMessage, _Mapping]]] = ...) -> None: ...
