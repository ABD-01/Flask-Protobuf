# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: example.proto
# Protobuf Python Version: 4.25.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rexample.proto\x12\x07\x45xample\":\n\rNestedMessage\x12\x12\n\nnested_int\x18\x01 \x01(\x05\x12\x15\n\rnested_string\x18\x02 \x01(\t\"\x89\x02\n\x0e\x45xampleMessage\x12\x11\n\tint_field\x18\x01 \x01(\x05\x12\x14\n\x0cstring_field\x18\x02 \x01(\t\x12\x13\n\x0b\x62ytes_field\x18\x03 \x01(\x0c\x12(\n\nenum_field\x18\x04 \x01(\x0e\x32\x14.Example.ExampleEnum\x12\x34\n\x14nested_message_field\x18\x05 \x01(\x0b\x32\x16.Example.NestedMessage\x12\x1a\n\x12repeated_int_field\x18\x06 \x03(\x05\x12=\n\x1drepeated_nested_message_field\x18\x07 \x03(\x0b\x32\x16.Example.NestedMessage*2\n\x0b\x45xampleEnum\x12\x10\n\x0c\x46IRST_OPTION\x10\x00\x12\x11\n\rSECOND_OPTION\x10\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'example_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_EXAMPLEENUM']._serialized_start=354
  _globals['_EXAMPLEENUM']._serialized_end=404
  _globals['_NESTEDMESSAGE']._serialized_start=26
  _globals['_NESTEDMESSAGE']._serialized_end=84
  _globals['_EXAMPLEMESSAGE']._serialized_start=87
  _globals['_EXAMPLEMESSAGE']._serialized_end=352
# @@protoc_insertion_point(module_scope)
