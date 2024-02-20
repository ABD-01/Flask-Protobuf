
>>> cmd
<module 'tmcvp_command_pb2' from 'D:\\PROJECTS/V6.2Server/V6.2proto\\tmcvp_command_pb2.py'>
>>> cmdMsg
<module 'tmcvp_command_message_pb2' from 'D:\\PROJECTS/V6.2Server/V6.2proto\\tmcvp_command_message_pb2.py'>
>>> cmdMsg.commandMessageSubType
<google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x00000148958366E0>
>>> list(cmdMsg.commandMessageSubType) 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'EnumTypeWrapper' object is not iterable
>>> dir(cmdMsg.commandMessageSubType)  
['DESCRIPTOR', 'Name', 'Value', 'ValueType', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_enum_type', 'items', 'keys', 'values']
>>> items(cmdMsg.commandMessageSubType) 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'items' is not defined. Did you mean: 'iter'?
>>> cmdMsg.commandMessageSubType.items()
[('AbortFOTACommand', 0), ('FOTANotificationCommand', 1), ('OnDemandDMSVideoFileCommand', 2), ('GetFOTAStateCommand', 3), ('InitiateFOTACommand', 4), ('GetVINandSerialnumberCommand', 5), ('StartLightCommand', 6), ('StopLightCommand', 7), 
('FindCarLocationCommand', 8), ('ImmobilizeVehicleCommand', 9), ('MobilizeVehicleCommand', 10), ('AuthorizeUserCommand', 11), ('ConfigureTMCVPParaCommand', 12), ('ConfigureAIS140ParaCommand', 13), ('ReadTMLConfigureParaCommand', 14), ('ReadAIS140ConfigureParaCommand', 15), ('StartICReplicaCommand', 16), ('StopICReplicaCommand', 17), ('DriverIdAuthenticationStatusCommand', 18), ('CumminsSeedTokenResponseCommand', 19), ('CumminsNewCalDownloadCommand', 20), ('TMLCDConfigFileDownloadCommand', 21), ('CumminsFileDownloadCommand', 22), ('VoiceControllerCommand', 23), ('StartTCuLogExportCommand', 24), ('StopTCuLogExportCommand', 25), ('RemoteValidationCommand', 26), ('CertificateDownloadCommand', 27), ('SetCertificateStatusCommand', 28), ('CumminsCSUUDSParaTransferCommand', 29), ('AbortCSUCommand', 30)]
>>> cmdMsg.commandMessageSubType        
<google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x00000148958366E0>
>>> cmdMsg.commandMessageSubType(3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'EnumTypeWrapper' object is not callable
>>> cmdMsg.commandMessageSubType   
<google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x00000148958366E0>
>>> cmdMsg.commandMessageSubType(1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'EnumTypeWrapper' object is not callable
>>> cmdMsg.commandMessageSubType    
<google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x00000148958366E0>
>>> cmdMsg.commandMessageSubType
<google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x00000148958366E0>
>>> cmdMsg.commandMessageSubType.__dir__()
['_enum_type', 'DESCRIPTOR', '__module__', '__doc__', 'ValueType', '__init__', 'Name', 'Value', 'keys', 'values', 'items', '__getattr__', '__dict__', '__weakref__', '__new__', '__repr__', '__hash__', '__str__', '__getattribute__', '__setattr__', '__delattr__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__reduce_ex__', '__reduce__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']
>>> from tabulate import tabulate
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'tabulate'
>>> from tabulate import tabulate 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'tabulate'
>>> cmdMsg.commandMessageSubType.items()
[('AbortFOTACommand', 0), ('FOTANotificationCommand', 1), ('OnDemandDMSVideoFileCommand', 2), ('GetFOTAStateCommand', 3), ('InitiateFOTACommand', 4), ('GetVINandSerialnumberCommand', 5), ('StartLightCommand', 6), ('StopLightCommand', 7), 
('FindCarLocationCommand', 8), ('ImmobilizeVehicleCommand', 9), ('MobilizeVehicleCommand', 10), ('AuthorizeUserCommand', 11), ('ConfigureTMCVPParaCommand', 12), ('ConfigureAIS140ParaCommand', 13), ('ReadTMLConfigureParaCommand', 14), ('ReadAIS140ConfigureParaCommand', 15), ('StartICReplicaCommand', 16), ('StopICReplicaCommand', 17), ('DriverIdAuthenticationStatusCommand', 18), ('CumminsSeedTokenResponseCommand', 19), ('CumminsNewCalDownloadCommand', 20), ('TMLCDConfigFileDownloadCommand', 21), ('CumminsFileDownloadCommand', 22), ('VoiceControllerCommand', 23), ('StartTCuLogExportCommand', 24), ('StopTCuLogExportCommand', 25), ('RemoteValidationCommand', 26), ('CertificateDownloadCommand', 27), ('SetCertificateStatusCommand', 28), ('CumminsCSUUDSParaTransferCommand', 29), ('AbortCSUCommand', 30)]
>>> for k,v in cmdMsg.commandMessageSubType.items():
...     if v == 4:
...             print(k,v)
...             break
... 
InitiateFOTACommand 4
>>> subtype = 4
>>> a = cmdMsg.CommandMessage
>>> a
<class 'tmcvp_command_message_pb2.CommandMessage'>
>>> a = cmdMsg.CommandMessage()
>>> a

>>> dir(a)
['ByteSize', 'Clear', 'ClearExtension', 'ClearField', 'CopyFrom', 'DESCRIPTOR', 'DiscardUnknownFields', 'Extensions', 'FindInitializationErrors', 'FromString', 'HasExtension', 'HasField', 'IsInitialized', 'ListFields', 'MergeFrom', 'MergeFromString', 'ParseFromString', 'RegisterExtension', 'SerializePartialToString', 'SerializeToString', 'SetInParent', 'UnknownFields', 'WhichOneof', '_CheckCalledFromGeneratedFile', '_SetListener', '__class__', '__deepcopy__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__slots__', '__str__', '__subclasshook__', '__unicode__', '_extensions_by_name', '_extensions_by_number', 'command_payload', 'correlation_id', 'message_id', 'packet_status', 'priority', 'provisioning_state', 'subtype', 'time_stamp', 'type', 'vehicle_id', 'version']
>>> a.message_id = "3333 
  File "<stdin>", line 1
    a.message_id = "3333
                   ^
SyntaxError: unterminated string literal (detected at line 1)
>>> a.message_id = "33" 
>>> a
message_id: "33"

>>> a.correlation_id=4
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 4 has type int, but expected one of: bytes, unicode
>>> a.correlation_id=b'4'
>>> a.vehicle_id=b'MH12' 
>>> a
message_id: "33"
correlation_id: "4"
vehicle_id: "MH12"

>>> import tmcvp_common_pb2 as cmn
>>> cmn.eTcuMessageType
<google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x00000148957DF3D0>
>>> cmn.eTcuMessageType.items()
[('command', 0), ('commandResponse', 1), ('alert', 2), ('vehicleTelemetry', 3), ('vehicleEvent', 4), ('diagnosticsISOFcdm1', 5), ('vehicleGenericCAN', 6), ('vehicleIcCAN', 7), ('vehicleEmissionCAN', 8), ('vehiclePrognosticCAN', 9), ('vehicleISOGenericCAN', 10), ('vehicleISOIcCAN', 11), ('vehicleISOEmissionCAN', 12), ('vehicleISOPrognosticCAN', 13), ('cdHeartbeat', 14), ('csuUdsResult', 15), ('tcuHealthStatus', 16), ('cumminsFileUploadRequest', 17), ('cumminsFileUploadResponse', 18), ('cumminsFileUploadStatus', 19), ('fileUploadRequest', 20), ('fileUploadResponse', 21), ('fileUploadStatus', 22), ('fileUploadAck', 23), ('cumminsDMRequest', 24), ('cumminsDMResponse', 25), ('vehicleStateOfHealth', 26), ('tmlCD', 27), ('tmlCDISO', 28), ('diagnosticsFcdm1', 29)]
>>> {v:k for k,v in cmn.eTcuMessageType.items()}
{0: 'command', 1: 'commandResponse', 2: 'alert', 3: 'vehicleTelemetry', 4: 'vehicleEvent', 5: 'diagnosticsISOFcdm1', 6: 'vehicleGenericCAN', 7: 'vehicleIcCAN', 8: 'vehicleEmissionCAN', 9: 'vehiclePrognosticCAN', 10: 'vehicleISOGenericCAN', 11: 'vehicleISOIcCAN', 12: 'vehicleISOEmissionCAN', 13: 'vehicleISOPrognosticCAN', 14: 'cdHeartbeat', 15: 'csuUdsResult', 16: 'tcuHealthStatus', 17: 'cumminsFileUploadRequest', 18: 'cumminsFileUploadResponse', 19: 'cumminsFileUploadStatus', 20: 'fileUploadRequest', 21: 'fileUploadResponse', 22: 'fileUploadStatus', 23: 'fileUploadAck', 24: 'cumminsDMRequest', 25: 'cumminsDMResponse', 26: 'vehicleStateOfHealth', 27: 'tmlCD', 28: 'tmlCDISO', 29: 'diagnosticsFcdm1'}        
>>> {v:k for k,v in cmn.eTcuMessageType.items()}[subtype]
'vehicleEvent'
>>> cmn.eTcuMessageType.command
0   
>>> a
message_id: "33"   
correlation_id: "4"
vehicle_id: "MH12" 

>>> a.type = cmn.eTcuMessageType.command
>>> a
message_id: "33"
correlation_id: "4"
vehicle_id: "MH12"

>>> print(a)
message_id: "33"
correlation_id: "4"
vehicle_id: "MH12"

>>> a.type = cmn.eTcuMessageType.command
>>> type(a)
<class 'tmcvp_command_message_pb2.CommandMessage'>
>>> a.ListField()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: ListField. Did you mean: 'ListFields'?
>>> a.ListFields() 
[(<google.protobuf.pyext._message.FieldDescriptor object at 0x00000148952C8A60>, '33'), (<google.protobuf.pyext._message.FieldDescriptor object at 0x00000148958369B0>, '4'), (<google.protobuf.pyext._message.FieldDescriptor object at 0x0000014895837040>, 'MH12')]
>>> setattr(a,'type',  cmn.eTcuMessageType.command)
>>> a
message_id: "33"
correlation_id: "4"
vehicle_id: "MH12"

>>> a.ListFields()
[(<google.protobuf.pyext._message.FieldDescriptor object at 0x0000014895309BA0>, '33'), (<google.protobuf.pyext._message.FieldDescriptor object at 0x0000014895837100>, '4'), (<google.protobuf.pyext._message.FieldDescriptor object at 0x0000014895837130>, 'MH12')]
>>> getattr(a, 'type')
0
>>> a
message_id: "33"
correlation_id: "4"
vehicle_id: "MH12"

>>> a.subtype = subtype
>>> a
message_id: "33"
correlation_id: "4"
vehicle_id: "MH12"
subtype: InitiateFOTACommand

>>> a.type
0
>>> a.priority = 'priority' 
>>> a
message_id: "33"
correlation_id: "4"
vehicle_id: "MH12"
subtype: InitiateFOTACommand
priority: "priority"

>>> a.provisioning_state
0
>>> a.provisioning_state.__dir__()
['__new__', '__repr__', '__hash__', '__getattribute__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__add__', '__radd__', '__sub__', '__rsub__', '__mul__', '__rmul__', '__mod__', '__rmod__', '__divmod__', '__rdivmod__', '__pow__', '__rpow__', '__neg__', '__pos__', '__abs__', '__bool__', '__invert__', '__lshift__', '__rlshift__', '__rshift__', '__rrshift__', '__and__', '__rand__', '__xor__', '__rxor__', '__or__', '__ror__', '__int__', '__float__', '__floordiv__', '__rfloordiv__', '__truediv__', '__rtruediv__', '__index__', 'conjugate', 'bit_length', 'bit_count', 'to_bytes', 'from_bytes', 'as_integer_ratio', '__trunc__', '__floor__', '__ceil__', '__round__', '__getnewargs__', '__format__', 
'__sizeof__', 'real', 'imag', 'numerator', 'denominator', '__doc__', '__str__', '__setattr__', '__delattr__', '__init__', '__reduce_ex__', '__reduce__', '__subclasshook__', '__init_subclass__', '__dir__', '__class__']
>>> a.DESCRIPTOR
<google.protobuf.pyext._message.MessageDescriptor object at 0x0000014895836440>
>>> a.DESCRIPTOR.__dir__()
['GetOptions', 'CopyToProto', 'EnumValueName', 'name', 'full_name', '_concrete_class', 'file', 'fields', 'fields_by_name', 'fields_by_camelcase_name', 'fields_by_number', 'nested_types', 'nested_types_by_name', 'extensions', 'extensions_by_name', 'extension_ranges', 'enum_types', 'enum_types_by_name', 'enum_values_by_name', 'oneofs_by_name', 'oneofs', 'containing_type', 'is_extendable', 'has_options', '_options', '_serialized_options', 'syntax', '__doc__', '__new__', '__repr__', '__hash__', '__str__', '__getattribute__', '__setattr__', '__delattr__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__init__', '__reduce_ex__', '__reduce__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']
>>> a.DESCRIPTOR.fields   
<MessageFields sequence>
>>> [f.name for f in a.DESCRIPTOR.fields] 
['message_id', 'correlation_id', 'vehicle_id', 'type', 'subtype', 'priority', 'provisioning_state', 'version', 'time_stamp', 'packet_status', 'command_payload']
>>> f = next(iter(a.DESCRIPTOR.fields))
>>> f
<google.protobuf.pyext._message.FieldDescriptor object at 0x0000014895836E60>
>>> f.__dir__()
['GetOptions', 'full_name', 'name', 'camelcase_name', 'json_name', 'file', 'type', 'cpp_type', 'label', 'number', 'index', 'default_value', 'has_default_value', 'is_extension', 'id', '_cdescriptor', 'message_type', 'enum_type', 'containing_type', 'extension_scope', 'containing_oneof', 'has_options', 'has_presence', '_options', '_serialized_options', '__doc__', 'LABEL_OPTIONAL', 'LABEL_REQUIRED', 'LABEL_REPEATED', 'TYPE_DOUBLE', 'TYPE_FLOAT', 'TYPE_INT64', 'TYPE_UINT64', 'TYPE_INT32', 'TYPE_FIXED64', 'TYPE_FIXED32', 'TYPE_BOOL', 'TYPE_STRING', 'TYPE_GROUP', 'TYPE_MESSAGE', 'TYPE_BYTES', 'TYPE_UINT32', 'TYPE_ENUM', 'TYPE_SFIXED32', 'TYPE_SFIXED64', 'TYPE_SINT32', 'TYPE_SINT64', 'CPPTYPE_INT32', 'CPPTYPE_INT64', 'CPPTYPE_UINT32', 'CPPTYPE_UINT64', 'CPPTYPE_DOUBLE', 'CPPTYPE_FLOAT', 'CPPTYPE_BOOL', 'CPPTYPE_ENUM', 'CPPTYPE_STRING', 'CPPTYPE_MESSAGE', '__new__', '__repr__', '__hash__', '__str__', '__getattribute__', '__setattr__', '__delattr__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__init__', '__reduce_ex__', '__reduce__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']
>>> f.name
'message_id'
>>> f.GetOptions  
<built-in method GetOptions of google.protobuf.pyext._message.FieldDescriptor object at 0x0000014895836E60>
>>> f.GetOptions()

>>> help(f.GetOptions) 
Help on built-in function GetOptions:

GetOptions(...) method of google.protobuf.pyext._message.FieldDescriptor instance

>>> f.type             
9
>>> getattr(f, 'type')
9
>>> f.message_type
>>> [f.name for f in a.DESCRIPTOR.fields]
['message_id', 'correlation_id', 'vehicle_id', 'type', 'subtype', 'priority', 'provisioning_state', 'version', 'time_stamp', 'packet_status', 'command_payload']
>>> a.DESCRIPTOR.fields[3] 
<google.protobuf.pyext._message.FieldDescriptor object at 0x00000148958372B0>
>>> a.DESCRIPTOR.fields[3].__dir__()
['GetOptions', 'full_name', 'name', 'camelcase_name', 'json_name', 'file', 'type', 'cpp_type', 'label', 'number', 'index', 'default_value', 'has_default_value', 'is_extension', 'id', '_cdescriptor', 'message_type', 'enum_type', 'containing_type', 'extension_scope', 'containing_oneof', 'has_options', 'has_presence', '_options', '_serialized_options', '__doc__', 'LABEL_OPTIONAL', 'LABEL_REQUIRED', 'LABEL_REPEATED', 'TYPE_DOUBLE', 'TYPE_FLOAT', 'TYPE_INT64', 'TYPE_UINT64', 'TYPE_INT32', 'TYPE_FIXED64', 'TYPE_FIXED32', 'TYPE_BOOL', 'TYPE_STRING', 'TYPE_GROUP', 'TYPE_MESSAGE', 'TYPE_BYTES', 'TYPE_UINT32', 'TYPE_ENUM', 'TYPE_SFIXED32', 'TYPE_SFIXED64', 'TYPE_SINT32', 'TYPE_SINT64', 'CPPTYPE_INT32', 'CPPTYPE_INT64', 'CPPTYPE_UINT32', 'CPPTYPE_UINT64', 'CPPTYPE_DOUBLE', 'CPPTYPE_FLOAT', 'CPPTYPE_BOOL', 'CPPTYPE_ENUM', 'CPPTYPE_STRING', 'CPPTYPE_MESSAGE', '__new__', '__repr__', '__hash__', '__str__', '__getattribute__', '__setattr__', '__delattr__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__init__', '__reduce_ex__', '__reduce__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']
>>> a.DESCRIPTOR.fields[3].name     
'type'
>>> a.DESCRIPTOR.fields[3].label
1
>>> a.DESCRIPTOR.fields[3].default_value
0
>>> a.DESCRIPTOR.fields[3].tye          
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'google.protobuf.pyext._message.FieldDescriptor' object has no attribute 'tye'. Did you mean: 'type'?  
>>> a.DESCRIPTOR.fields[3].type 
14
>>> a.DESCRIPTOR.fields[3].message_type
>>> a.DESCRIPTOR.fields[3].type
14
>>> a.DESCRIPTOR.fields[6].name 
'provisioning_state'
>>> a.DESCRIPTOR.fields[6].type
14
>>> a
message_id: "33"
correlation_id: "4"
vehicle_id: "MH12"
subtype: InitiateFOTACommand
priority: "priority"

>>> a.type
0
>>> a
message_id: "33"
correlation_id: "4"
vehicle_id: "MH12"
subtype: InitiateFOTACommand
priority: "priority"

>>> a.provisioning_state
0
>>> cmn                      
<module 'tmcvp_common_pb2' from 'D:\\PROJECTS/V6.2Server/V6.2proto\\tmcvp_common_pb2.py'>
>>> cmn.provisioned
1
>>> cmn.eProvisioningState
<google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x00000148957DF340>
>>> cmn.eProvisioningState.items()
[('factory', 0), ('provisioned', 1), ('authorized', 2)]
>>> cmn.eProvisioningState.provisioned
1
>>> a.provisioning_state =  cmn.eProvisioningState.provisioned 
>>> a
message_id: "33"
correlation_id: "4"
vehicle_id: "MH12"
subtype: InitiateFOTACommand
priority: "priority"
provisioning_state: provisioned

>>> a.type
0
>>> a.message_type
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: message_type. Did you mean: 'message_id'?
>>> a
message_id: "33"
correlation_id: "4"
vehicle_id: "MH12"
subtype: InitiateFOTACommand
priority: "priority"
provisioning_state: provisioned

>>> type(a)
<class 'tmcvp_command_message_pb2.CommandMessage'>
>>> cmdMsg.CommandMessage
<class 'tmcvp_command_message_pb2.CommandMessage'>
>>> cmdMsg.CommandMessage.__dir__(0
... )
['__new__', '__repr__', '__hash__', '__getattribute__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__add__', '__radd__', '__sub__', '__rsub__', '__mul__', '__rmul__', '__mod__', '__rmod__', '__divmod__', '__rdivmod__', '__pow__', '__rpow__', '__neg__', '__pos__', '__abs__', '__bool__', '__invert__', '__lshift__', '__rlshift__', '__rshift__', '__rrshift__', '__and__', '__rand__', '__xor__', '__rxor__', '__or__', '__ror__', '__int__', '__float__', '__floordiv__', '__rfloordiv__', '__truediv__', '__rtruediv__', '__index__', 'conjugate', 'bit_length', 'bit_count', 'to_bytes', 'from_bytes', 'as_integer_ratio', '__trunc__', '__floor__', '__ceil__', '__round__', '__getnewargs__', '__format__', 
'__sizeof__', 'real', 'imag', 'numerator', 'denominator', '__doc__', '__str__', '__setattr__', '__delattr__', '__init__', '__reduce_ex__', '__reduce__', '__subclasshook__', '__init_subclass__', '__dir__', '__class__']
>>> cmdMsg.CommandMessage.__dir__() 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unbound method object.__dir__() needs an argument
>>> cmdMsg.CommandMessage().__dir__()
['DESCRIPTOR', '__module__', '__slots__', '__doc__', 'message_id', 'correlation_id', 'vehicle_id', 'type', 'subtype', 'priority', 'provisioning_state', 'version', 'time_stamp', 'packet_status', 'command_payload', '__new__', '__repr__', '__hash__', '__str__', '__getattribute__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__init__', '__deepcopy__', '__unicode__', 'ByteSize', 'Clear', 'ClearExtension', 'ClearField', 'CopyFrom', 'DiscardUnknownFields', 'FindInitializationErrors', 'FromString', 'HasExtension', 'HasField', 'IsInitialized', 'ListFields', 'MergeFrom', 'MergeFromString', 'ParseFromString', 'RegisterExtension', 'SerializePartialToString', 'SerializeToString', 'SetInParent', 'UnknownFields', 'WhichOneof', '_CheckCalledFromGeneratedFile', 'Extensions', '_extensions_by_name', '_extensions_by_number', '__setattr__', '__delattr__', '__reduce_ex__', '__reduce__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__', '_SetListener', '__getstate__', '__setstate__']
>>> cmdMsg.CommandMessage().DESCRIPTOR
<google.protobuf.pyext._message.MessageDescriptor object at 0x0000014895836440>
>>> cmdMsg.CommandMessage().DESCRIPTOR.__DIR__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'google.protobuf.pyext._message.MessageDescriptor' object has no attribute '__DIR__'. Did you mean: '__dir__'?
>>> cmdMsg.CommandMessage().DESCRIPTOR.__dir__() 
['GetOptions', 'CopyToProto', 'EnumValueName', 'name', 'full_name', '_concrete_class', 'file', 'fields', 'fields_by_name', 'fields_by_camelcase_name', 'fields_by_number', 'nested_types', 'nested_types_by_name', 'extensions', 'extensions_by_name', 'extension_ranges', 'enum_types', 'enum_types_by_name', 'enum_values_by_name', 'oneofs_by_name', 'oneofs', 'containing_type', 'is_extendable', 'has_options', '_options', '_serialized_options', 'syntax', '__doc__', '__new__', '__repr__', '__hash__', '__str__', '__getattribute__', '__setattr__', '__delattr__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__init__', '__reduce_ex__', '__reduce__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']
>>> cmdMsg.CommandMessage().DESCRIPTOR.fields   
<MessageFields sequence>
>>> [cmdMsg.CommandMessage().DESCRIPTOR.fields] 
[<MessageFields sequence>]
>>> list(cmdMsg.CommandMessage().DESCRIPTOR.fields) 
[<google.protobuf.pyext._message.FieldDescriptor object at 0x0000014895836E60>, <google.protobuf.pyext._message.FieldDescriptor object at 0x0000014895309B10>, <google.protobuf.pyext._message.FieldDescriptor object at 0x00000148958372B0>, 
<google.protobuf.pyext._message.FieldDescriptor object at 0x0000014895BEA8C0>, <google.protobuf.pyext._message.FieldDescriptor object at 0x0000014895BEAB90>, <google.protobuf.pyext._message.FieldDescriptor object at 0x0000014895BEABC0>, <google.protobuf.pyext._message.FieldDescriptor object at 0x0000014895BEABF0>, <google.protobuf.pyext._message.FieldDescriptor object at 0x0000014895BEAC80>, <google.protobuf.pyext._message.FieldDescriptor object at 0x0000014895BEAA10>, <google.protobuf.pyext._message.FieldDescriptor object at 0x0000014895BEACE0>, <google.protobuf.pyext._message.FieldDescriptor object at 0x0000014895BEAC50>]
>>> list([f.name for f in cmdMsg.CommandMessage().DESCRIPTOR.fields]) 
['message_id', 'correlation_id', 'vehicle_id', 'type', 'subtype', 'priority', 'provisioning_state', 'version', 'time_stamp', 'packet_status', 'command_payload']
>>> cmdMsg.CommandMessage().DESCRIPTOR.fields[10]   
<google.protobuf.pyext._message.FieldDescriptor object at 0x000001489538E290>
>>> cmdMsg.CommandMessage().DESCRIPTOR.fields[10].__dir__()
['GetOptions', 'full_name', 'name', 'camelcase_name', 'json_name', 'file', 'type', 'cpp_type', 'label', 'number', 'index', 'default_value', 'has_default_value', 'is_extension', 'id', '_cdescriptor', 'message_type', 'enum_type', 'containing_type', 'extension_scope', 'containing_oneof', 'has_options', 'has_presence', '_options', '_serialized_options', '__doc__', 'LABEL_OPTIONAL', 'LABEL_REQUIRED', 'LABEL_REPEATED', 'TYPE_DOUBLE', 'TYPE_FLOAT', 'TYPE_INT64', 'TYPE_UINT64', 'TYPE_INT32', 'TYPE_FIXED64', 'TYPE_FIXED32', 'TYPE_BOOL', 'TYPE_STRING', 'TYPE_GROUP', 'TYPE_MESSAGE', 'TYPE_BYTES', 'TYPE_UINT32', 'TYPE_ENUM', 'TYPE_SFIXED32', 'TYPE_SFIXED64', 'TYPE_SINT32', 'TYPE_SINT64', 'CPPTYPE_INT32', 'CPPTYPE_INT64', 'CPPTYPE_UINT32', 'CPPTYPE_UINT64', 'CPPTYPE_DOUBLE', 'CPPTYPE_FLOAT', 'CPPTYPE_BOOL', 'CPPTYPE_ENUM', 'CPPTYPE_STRING', 'CPPTYPE_MESSAGE', '__new__', '__repr__', '__hash__', '__str__', '__getattribute__', '__setattr__', '__delattr__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__init__', '__reduce_ex__', '__reduce__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']
>>> cmdMsg.CommandMessage().DESCRIPTOR.fields[10].type     
11
>>> cmdMsg.CommandMessage().DESCRIPTOR.fields[10].message_type
<google.protobuf.pyext._message.MessageDescriptor object at 0x0000014895836560>
>>> cmdMsg.CommandMessage().DESCRIPTOR.fields[10].message_type.__dir__()
['GetOptions', 'CopyToProto', 'EnumValueName', 'name', 'full_name', '_concrete_class', 'file', 'fields', 'fields_by_name', 'fields_by_camelcase_name', 'fields_by_number', 'nested_types', 'nested_types_by_name', 'extensions', 'extensions_by_name', 'extension_ranges', 'enum_types', 'enum_types_by_name', 'enum_values_by_name', 'oneofs_by_name', 'oneofs', 'containing_type', 'is_extendable', 'has_options', '_options', '_serialized_options', 'syntax', '__doc__', '__new__', '__repr__', '__hash__', '__str__', '__getattribute__', '__setattr__', '__delattr__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__init__', '__reduce_ex__', '__reduce__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']
>>> cmdMsg.CommandMessage().DESCRIPTOR.fields[10].message_type.file     
<google.protobuf.pyext._message.FileDescriptor object at 0x0000014895863B00>
>>> cmdMsg.CommandMessage().DESCRIPTOR.fields[10].message_type.name
'CommandPayload'
>>> a
message_id: "33"
correlation_id: "4"
vehicle_id: "MH12"
subtype: InitiateFOTACommand
priority: "priority"
provisioning_state: provisioned

>>> a.version = "2.2" 
>>> a
message_id: "33"
correlation_id: "4"
vehicle_id: "MH12"
subtype: InitiateFOTACommand
priority: "priority"
provisioning_state: provisioned
version: "2.2"

>>> a.time_stamp

>>> a.time_stamp.GetCurrentTime()
>>> a
message_id: "33"
correlation_id: "4"
vehicle_id: "MH12"
subtype: InitiateFOTACommand
priority: "priority"
provisioning_state: provisioned
version: "2.2"
time_stamp {
  seconds: 1707807003
  nanos: 680155000
}

>>> a.packet_status
0
>>> a.packet_status = cmn.Live
>>> a
message_id: "33"
correlation_id: "4"
vehicle_id: "MH12"
subtype: InitiateFOTACommand
priority: "priority"
provisioning_state: provisioned
version: "2.2"
time_stamp {
  seconds: 1707807003
  nanos: 680155000
}
packet_status: Live

>>> cmd
<module 'tmcvp_command_pb2' from 'D:\\PROJECTS/V6.2Server/V6.2proto\\tmcvp_command_pb2.py'>
>>> cmd.InitiateFOTACommandPayload
<class 'tmcvp_command_pb2.InitiateFOTACommandPayload'>
>>> cmd.InitiateFOTACommandPayload()

>>> cmd.InitiateFOTACommandPayload().__dir__()
['DESCRIPTOR', '__module__', '__slots__', '__doc__', 'totalNoOfFiles', 'firmwareDownloadPayload', '__new__', '__repr__', '__hash__', '__str__', '__getattribute__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__init__', '__deepcopy__', '__unicode__', 'ByteSize', 'Clear', 'ClearExtension', 'ClearField', 'CopyFrom', 'DiscardUnknownFields', 'FindInitializationErrors', 'FromString', 'HasExtension', 'HasField', 'IsInitialized', 'ListFields', 'MergeFrom', 'MergeFromString', 'ParseFromString', 'RegisterExtension', 'SerializePartialToString', 'SerializeToString', 'SetInParent', 'UnknownFields', 'WhichOneof', '_CheckCalledFromGeneratedFile', 'Extensions', '_extensions_by_name', '_extensions_by_number', '__setattr__', '__delattr__', '__reduce_ex__', '__reduce__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__', '_SetListener', '__getstate__', '__setstate__']
>>> cmd.InitiateFOTACommandPayload().DESCRIPTOR
<google.protobuf.pyext._message.MessageDescriptor object at 0x00000148958359C0>
>>> cmd.InitiateFOTACommandPayload().DESCRIPTOR.items()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'google.protobuf.pyext._message.MessageDescriptor' object has no attribute 'items'
>>> cmd.InitiateFOTACommandPayload().DESCRIPTOR.fields 
<MessageFields sequence>
>>> [f.name for f in cmd.InitiateFOTACommandPayload().DESCRIPTOR.fields] 
['totalNoOfFiles', 'firmwareDownloadPayload']
>>> cmd.InitiateFOTACommandPayload().DESCRIPTOR.fields
<MessageFields sequence>
>>> cmd.InitiateFOTACommandPayload().DESCRIPTOR.fields[1
... ]
<google.protobuf.pyext._message.FieldDescriptor object at 0x000001489538CF40>
>>> cmd.InitiateFOTACommandPayload().DESCRIPTOR.fields[1].name
'firmwareDownloadPayload'
>>> cmd.InitiateFOTACommandPayload().DESCRIPTOR.fields[1].type
11
>>> cmd.InitiateFOTACommandPayload().DESCRIPTOR.fields[1].message_type
<google.protobuf.pyext._message.MessageDescriptor object at 0x0000014895835990>
>>> cmd.InitiateFOTACommandPayload().DESCRIPTOR.fields[1].message_type.name
'FirmwareDownloadPayload'
>>> cmd.InitiateFOTACommandPayload()                                        

>>> a                                                                       
message_id: "33"
correlation_id: "4"
vehicle_id: "MH12"
subtype: InitiateFOTACommand
priority: "priority"
provisioning_state: provisioned
version: "2.2"
time_stamp {
  seconds: 1707807003
  nanos: 680155000
}
packet_status: Live

>>> a.command_payload = cmd.InitiateFOTACommandPayload()  
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: Assignment not allowed to field "command_payload" in protocol message object.
>>> a.command_payload = cmd.InitiateFOTACommandPayload()  
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: Assignment not allowed to field "command_payload" in protocol message object.
>>> a.command_payload.add()                              
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: add
>>> cmd.InitiateFOTACommandPayload()

>>> cmd.InitiateFOTACommandPayload().DESCRIPTOR.fields[1].message_type.name 
'FirmwareDownloadPayload'
>>> cmd.InitiateFOTACommandPayload().FirmwareDownloadPayload                
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: FirmwareDownloadPayload. Did you mean: 'firmwareDownloadPayload'?
>>> cmd.InitiateFOTACommandPayload().firmwareDownloadPayload 
[]
>>> cmd.InitiateFOTACommandPayload().firmwareDownloadPayload.add()

>>> a.command_payload      

>>> pyld = cmd.InitiateFOTACommandPayload()                       
>>> pyld.name
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: name
>>> pyld.DESCRIPTOR
<google.protobuf.pyext._message.MessageDescriptor object at 0x00000148958359C0>
>>> pyld.DESCRIPTOR.fields
<MessageFields sequence>
>>> pyld.DESCRIPTOR.fields.__len__()
2
>>> pyld.DESCRIPTOR.fields[0].name  
'totalNoOfFiles'
>>> pyld.DESCRIPTOR.fields[1].name   
'firmwareDownloadPayload'
>>> pyld.totalNoOfFiles = 3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 3 has type int, but expected one of: bytes, unicode
>>> pyld.totalNoOfFiles = "3" 
>>> pyld
totalNoOfFiles: "3"

>>> pyld.firmwareDownloadPayload
[]
>>> pyld.firmwareDownloadPayload = 5
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: Assignment not allowed to repeated field "firmwareDownloadPayload" in protocol message object.
>>> pyld.DESCRIPTOR.fields[1].__dir__()
['GetOptions', 'full_name', 'name', 'camelcase_name', 'json_name', 'file', 'type', 'cpp_type', 'label', 'number', 'index', 'default_value', 'has_default_value', 'is_extension', 'id', '_cdescriptor', 'message_type', 'enum_type', 'containing_type', 'extension_scope', 'containing_oneof', 'has_options', 'has_presence', '_options', '_serialized_options', '__doc__', 'LABEL_OPTIONAL', 'LABEL_REQUIRED', 'LABEL_REPEATED', 'TYPE_DOUBLE', 'TYPE_FLOAT', 'TYPE_INT64', 'TYPE_UINT64', 'TYPE_INT32', 'TYPE_FIXED64', 'TYPE_FIXED32', 'TYPE_BOOL', 'TYPE_STRING', 'TYPE_GROUP', 'TYPE_MESSAGE', 'TYPE_BYTES', 'TYPE_UINT32', 'TYPE_ENUM', 'TYPE_SFIXED32', 'TYPE_SFIXED64', 'TYPE_SINT32', 'TYPE_SINT64', 'CPPTYPE_INT32', 'CPPTYPE_INT64', 'CPPTYPE_UINT32', 'CPPTYPE_UINT64', 'CPPTYPE_DOUBLE', 'CPPTYPE_FLOAT', 'CPPTYPE_BOOL', 'CPPTYPE_ENUM', 'CPPTYPE_STRING', 'CPPTYPE_MESSAGE', '__new__', '__repr__', '__hash__', '__str__', '__getattribute__', '__setattr__', '__delattr__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__init__', '__reduce_ex__', '__reduce__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']
>>> pyld.DESCRIPTOR.fields[1].GetOptions 
<built-in method GetOptions of google.protobuf.pyext._message.FieldDescriptor object at 0x0000014895837490>
>>> pyld.DESCRIPTOR.fields[1].GetOptions()

>>> help(pyld.DESCRIPTOR.fields[1].GetOptions) 
Help on built-in function GetOptions:

GetOptions(...) method of google.protobuf.pyext._message.FieldDescriptor instance

>>> pyld.DESCRIPTOR.fields[1].message_type     
<google.protobuf.pyext._message.MessageDescriptor object at 0x0000014895835990>
>>> pyld.DESCRIPTOR.fields[1].message_type.fields
<MessageFields sequence>
>>> pyld.DESCRIPTOR.fields[1].message_type.fields.__list__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'DescriptorSequence' object has no attribute '__list__'. Did you mean: '__lt__'?
>>> (f.name for f in pyld.DESCRIPTOR.fields[1].message_type.fields) 
<generator object <genexpr> at 0x0000014895B83B50>
>>> [f.name for f in pyld.DESCRIPTOR.fields[1].message_type.fields] 
['seqNo', 'url', 'accessToken', 'fileCheckSum']
>>> pyld.DESCRIPTOR.fields[1].message_type                          
<google.protobuf.pyext._message.MessageDescriptor object at 0x0000014895835990>
>>> pyld.DESCRIPTOR.fields[0].message_type 
>>> [f.name for f in pyld.DESCRIPTOR.fields[1].message_type.fields]
['seqNo', 'url', 'accessToken', 'fileCheckSum']
>>> pyld                                                            
totalNoOfFiles: "3"

>>> a.command_payload = cmd.InitiateFOTACommandPayload() 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: Assignment not allowed to field "command_payload" in protocol message object.
>>> a.command_payload = pyld                             
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: Assignment not allowed to field "command_payload" in protocol message object.
>>> pyld = cmd.InitiateFOTACommandPayload()                         
>>> pyld = cmd.InitiateFOTACommandPayload.add() 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: add
>>> a.command_payload = pyld
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: Assignment not allowed to field "command_payload" in protocol message object.
>>> pyld

>>> [f.name for f in pyld.DESCRIPTOR.fields[1].message_type.fields]
['seqNo', 'url', 'accessToken', 'fileCheckSum']
>>> pyld.firmwareDownloadPayload = 5                                
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: Assignment not allowed to repeated field "firmwareDownloadPayload" in protocol message object.
>>> pyld.totalNoOfFiles = 3          
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 3 has type int, but expected one of: bytes, unicode
>>> pyld.totalNoOfFiles = "3"
>>> pyld                                       
totalNoOfFiles: "3"

>>> a.command_payload = pyld
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: Assignment not allowed to field "command_payload" in protocol message object.
>>> a.command_payload.Packpyld) 
  File "<stdin>", line 1
    a.command_payload.Packpyld)
                              ^
SyntaxError: unmatched ')'
>>> a.command_payload.Pack(pyld) 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: Pack
>>> a.command_payload.CopyFrom(pyld) 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Parameter to CopyFrom() must be instance of same class: expected TataMotors.Cv620.Cv.CommandPayload got TataMotors.Cv620.Cv.InitiateFOTACommandPayload.
>>> a.command_payload                

>>> a.command_payload.__dir__()
['DESCRIPTOR', '__module__', '__slots__', '__doc__', 'abortFOTACommand', 'fOTANotificationCommand', 'onDemandDMSVideoFileCommand', 'getFOTAStateCommand', 'initiateFOTACommand', 'getVINandserialnumberCommand', 'startLightCommand', 'stopLightCommand', 'findCarLocationCommand', 'immobilizeVehicleCommand', 'mobilizeVehicleCommand', 'authorizeUserCommand', 'configureTMCVPParaCommand', 'configureAIS140ParaCommand', 'readTMLConfigureParaCommand', 'readAIS140ConfigureParaCommand', 'startICReplicaCommand', 'stopICReplicaCommand', 'driverIdAuthenticationStatusCommand', 'cumminsSeedTokenResponseCommand', 'cumminsNewCalDownloadCommand', 'tmlCDConfigFileDownloadCommand', 'cumminsFileDownloadCommand', 'voiceControllerCommand', 'startTCuLogExportCommand', 'stopTCuLogExportCommand', 'remoteValidationCommand', 'certificateDownloadCommand', 'setCertificateStatusCommand', 'cumminsCSUUDSParaTransferCommand', 'abortCSUCommand', '__new__', '__repr__', '__hash__', '__str__', '__getattribute__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__init__', '__deepcopy__', '__unicode__', 'ByteSize', 'Clear', 'ClearExtension', 'ClearField', 'CopyFrom', 'DiscardUnknownFields', 'FindInitializationErrors', 'FromString', 'HasExtension', 'HasField', 'IsInitialized', 'ListFields', 'MergeFrom', 'MergeFromString', 'ParseFromString', 'RegisterExtension', 'SerializePartialToString', 'SerializeToString', 'SetInParent', 'UnknownFields', 'WhichOneof', '_CheckCalledFromGeneratedFile', 'Extensions', '_extensions_by_name', '_extensions_by_number', '__setattr__', '__delattr__', '__reduce_ex__', '__reduce__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__', '_SetListener', '__getstate__', '__setstate__']
>>> a.command_payload.DESCRIPTOR
<google.protobuf.pyext._message.MessageDescriptor object at 0x0000014895836560>
>>> [f.name for f in a.command_payload.DESCRIPTOR.fields] 
['abortFOTACommand', 'fOTANotificationCommand', 'onDemandDMSVideoFileCommand', 'getFOTAStateCommand', 'initiateFOTACommand', 'getVINandserialnumberCommand', 'startLightCommand', 'stopLightCommand', 'findCarLocationCommand', 'immobilizeVehicleCommand', 'mobilizeVehicleCommand', 'authorizeUserCommand', 'configureTMCVPParaCommand', 'configureAIS140ParaCommand', 'readTMLConfigureParaCommand', 'readAIS140ConfigureParaCommand', 'startICReplicaCommand', 'stopICReplicaCommand', 'driverIdAuthenticationStatusCommand', 'cumminsSeedTokenResponseCommand', 'cumminsNewCalDownloadCommand', 'tmlCDConfigFileDownloadCommand', 'cumminsFileDownloadCommand', 'voiceControllerCommand', 'startTCuLogExportCommand', 'stopTCuLogExportCommand', 'remoteValidationCommand', 'certificateDownloadCommand', 'setCertificateStatusCommand', 'cumminsCSUUDSParaTransferCommand', 'abortCSUCommand']
>>> a                           
message_id: "33"
correlation_id: "4"
vehicle_id: "MH12"
subtype: InitiateFOTACommand
priority: "priority"
provisioning_state: provisioned
version: "2.2"
time_stamp {
  seconds: 1707807003
  nanos: 680155000
}
packet_status: Live

>>> a.command_payload.Pack(pyld)     
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: Pack
>>> a.command_payload.initiateFOTACommand

>>> a.command_payload.initiateFOTACommand = pyld
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: Assignment not allowed to field "initiateFOTACommand" in protocol message object.
>>> a.command_payload.initiateFOTACommand.Pack(pyld)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: Pack
>>> a.command_payload.initiateFOTACommand.CopyFrom(pyld) 
>>> a
message_id: "33"
correlation_id: "4"
vehicle_id: "MH12"
subtype: InitiateFOTACommand
priority: "priority"
provisioning_state: provisioned
version: "2.2"
time_stamp {
  seconds: 1707807003
  nanos: 680155000
}
packet_status: Live
command_payload {
  initiateFOTACommand {
    totalNoOfFiles: "3"
  }
}

>>> a.command_payload.DESCRIPTOR.label
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'google.protobuf.pyext._message.MessageDescriptor' object has no attribute 'label'
>>> a.command_payload.DESCRIPTOR      
<google.protobuf.pyext._message.MessageDescriptor object at 0x0000014895836560>
>>> a.command_payload.DESCRIPTOR.__dir__
<built-in method __dir__ of google.protobuf.pyext._message.MessageDescriptor object at 0x0000014895836560>
>>> a.command_payload.DESCRIPTOR.__dir__()
['GetOptions', 'CopyToProto', 'EnumValueName', 'name', 'full_name', '_concrete_class', 'file', 'fields', 'fields_by_name', 'fields_by_camelcase_name', 'fields_by_number', 'nested_types', 'nested_types_by_name', 'extensions', 'extensions_by_name', 'extension_ranges', 'enum_types', 'enum_types_by_name', 'enum_values_by_name', 'oneofs_by_name', 'oneofs', 'containing_type', 'is_extendable', 'has_options', '_options', '_serialized_options', 'syntax', '__doc__', '__new__', '__repr__', '__hash__', '__str__', '__getattribute__', '__setattr__', '__delattr__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__init__', '__reduce_ex__', '__reduce__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']
>>> a.command_payload.__dir__()            
['DESCRIPTOR', '__module__', '__slots__', '__doc__', 'abortFOTACommand', 'fOTANotificationCommand', 'onDemandDMSVideoFileCommand', 'getFOTAStateCommand', 'initiateFOTACommand', 'getVINandserialnumberCommand', 'startLightCommand', 'stopLightCommand', 'findCarLocationCommand', 'immobilizeVehicleCommand', 'mobilizeVehicleCommand', 'authorizeUserCommand', 'configureTMCVPParaCommand', 'configureAIS140ParaCommand', 'readTMLConfigureParaCommand', 'readAIS140ConfigureParaCommand', 'startICReplicaCommand', 'stopICReplicaCommand', 'driverIdAuthenticationStatusCommand', 'cumminsSeedTokenResponseCommand', 'cumminsNewCalDownloadCommand', 'tmlCDConfigFileDownloadCommand', 'cumminsFileDownloadCommand', 'voiceControllerCommand', 'startTCuLogExportCommand', 'stopTCuLogExportCommand', 'remoteValidationCommand', 'certificateDownloadCommand', 'setCertificateStatusCommand', 'cumminsCSUUDSParaTransferCommand', 'abortCSUCommand', '__new__', '__repr__', '__hash__', '__str__', '__getattribute__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__init__', '__deepcopy__', '__unicode__', 'ByteSize', 'Clear', 'ClearExtension', 'ClearField', 'CopyFrom', 'DiscardUnknownFields', 'FindInitializationErrors', 'FromString', 'HasExtension', 'HasField', 'IsInitialized', 'ListFields', 'MergeFrom', 'MergeFromString', 'ParseFromString', 'RegisterExtension', 'SerializePartialToString', 'SerializeToString', 'SetInParent', 'UnknownFields', 'WhichOneof', '_CheckCalledFromGeneratedFile', 'Extensions', '_extensions_by_name', '_extensions_by_number', '__setattr__', '__delattr__', '__reduce_ex__', '__reduce__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__', '_SetListener', '__getstate__', '__setstate__']
>>> a.command_payload.DESCRIPTOR.__dir__()
['GetOptions', 'CopyToProto', 'EnumValueName', 'name', 'full_name', '_concrete_class', 'file', 'fields', 'fields_by_name', 'fields_by_camelcase_name', 'fields_by_number', 'nested_types', 'nested_types_by_name', 'extensions', 'extensions_by_name', 'extension_ranges', 'enum_types', 'enum_types_by_name', 'enum_values_by_name', 'oneofs_by_name', 'oneofs', 'containing_type', 'is_extendable', 'has_options', '_options', '_serialized_options', 'syntax', '__doc__', '__new__', '__repr__', '__hash__', '__str__', '__getattribute__', '__setattr__', '__delattr__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__init__', '__reduce_ex__', '__reduce__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']
>>> a.command_payload.DESCRIPTOR.fields
<MessageFields sequence>
>>> a.command_payload.DESCRIPTOR.fields[0]
<google.protobuf.pyext._message.FieldDescriptor object at 0x00000148951A7C40>
>>> [f.name for f in a.command_payload.DESCRIPTOR.fields] 
['abortFOTACommand', 'fOTANotificationCommand', 'onDemandDMSVideoFileCommand', 'getFOTAStateCommand', 'initiateFOTACommand', 'getVINandserialnumberCommand', 'startLightCommand', 'stopLightCommand', 'findCarLocationCommand', 'immobilizeVehicleCommand', 'mobilizeVehicleCommand', 'authorizeUserCommand', 'configureTMCVPParaCommand', 'configureAIS140ParaCommand', 'readTMLConfigureParaCommand', 'readAIS140ConfigureParaCommand', 'startICReplicaCommand', 'stopICReplicaCommand', 'driverIdAuthenticationStatusCommand', 'cumminsSeedTokenResponseCommand', 'cumminsNewCalDownloadCommand', 'tmlCDConfigFileDownloadCommand', 'cumminsFileDownloadCommand', 'voiceControllerCommand', 'startTCuLogExportCommand', 'stopTCuLogExportCommand', 'remoteValidationCommand', 'certificateDownloadCommand', 'setCertificateStatusCommand', 'cumminsCSUUDSParaTransferCommand', 'abortCSUCommand']
>>> [f.name for f in a.command_payload.initiateFOTACommand.DESCRIPTOR.fields] 
['totalNoOfFiles', 'firmwareDownloadPayload']
>>> [f.name, f.type for f in a.command_payload.initiateFOTACommand.DESCRIPTOR.fields] 
  File "<stdin>", line 1
    [f.name, f.type for f in a.command_payload.initiateFOTACommand.DESCRIPTOR.fields]
     ^^^^^^^^^^^^^^
SyntaxError: did you forget parentheses around the comprehension target?
>>> [(f.name, f.type) for f in a.command_payload.initiateFOTACommand.DESCRIPTOR.fields] 
[('totalNoOfFiles', 9), ('firmwareDownloadPayload', 11)]
>>> [(f.name, f.type, f.label) for f in a.command_payload.initiateFOTACommand.DESCRIPTOR.fields] 
[('totalNoOfFiles', 9, 1), ('firmwareDownloadPayload', 11, 3)]
>>> a.command_payload.initiateFOTACommand.CopyFrom(pyld)                                
>>> a
message_id: "33"
correlation_id: "4"
vehicle_id: "MH12"
subtype: InitiateFOTACommand
priority: "priority"
provisioning_state: provisioned
version: "2.2"
time_stamp {
  seconds: 1707807003
  nanos: 680155000
}
packet_status: Live
command_payload {
  initiateFOTACommand {
    totalNoOfFiles: "3"
  }
}

>>> pyld
totalNoOfFiles: "3"

>>> pyld.name
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: name
>>> pyld.__dir__()
['DESCRIPTOR', '__module__', '__slots__', '__doc__', 'totalNoOfFiles', 'firmwareDownloadPayload', '__new__', '__repr__', '__hash__', '__str__', '__getattribute__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__init__', '__deepcopy__', '__unicode__', 'ByteSize', 'Clear', 'ClearExtension', 'ClearField', 'CopyFrom', 'DiscardUnknownFields', 'FindInitializationErrors', 'FromString', 'HasExtension', 'HasField', 'IsInitialized', 'ListFields', 'MergeFrom', 'MergeFromString', 'ParseFromString', 'RegisterExtension', 'SerializePartialToString', 'SerializeToString', 'SetInParent', 'UnknownFields', 'WhichOneof', '_CheckCalledFromGeneratedFile', 'Extensions', '_extensions_by_name', '_extensions_by_number', '__setattr__', '__delattr__', '__reduce_ex__', '__reduce__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__', '_SetListener', '__getstate__', '__setstate__']
>>> pyld.DESCRIPTOR
<google.protobuf.pyext._message.MessageDescriptor object at 0x00000148958359C0>
>>> pyld.DESCRIPTOR.fields   
<MessageFields sequence>
>>> pyld.DESCRIPTOR.fields[1].name
'firmwareDownloadPayload'
>>> pyld.firmwareDownloadPayload
[]
>>> pyld.firmwareDownloadPayload.add()

>>> x = pyld.firmwareDownloadPayload.add() 
>>> type(x)
<class 'tmcvp_command_pb2.FirmwareDownloadPayload'>
>>> [f.name for f in x.DESCRIPTOR.fields] 
['seqNo', 'url', 'accessToken', 'fileCheckSum']
>>> x.seqNo = 2                           
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 2 has type int, but expected one of: bytes, unicode
>>> x.seqNo = bytes(2)
>>> x
seqNo: "\000\000"

>>> pyld
totalNoOfFiles: "3"
firmwareDownloadPayload {
}
firmwareDownloadPayload {
  seqNo: "\000\000"
}

>>> a
message_id: "33"
correlation_id: "4"
vehicle_id: "MH12"
subtype: InitiateFOTACommand
priority: "priority"
provisioning_state: provisioned
version: "2.2"
time_stamp {
  seconds: 1707807003
  nanos: 680155000
}
packet_status: Live
command_payload {
  initiateFOTACommand {
    totalNoOfFiles: "3"
  }
}

>>> a.command_payload.initiateFOTACommand.CopyFrom(pyld)
>>> a
message_id: "33"
correlation_id: "4"
vehicle_id: "MH12"
subtype: InitiateFOTACommand
priority: "priority"
provisioning_state: provisioned
version: "2.2"
time_stamp {
  seconds: 1707807003
  nanos: 680155000
}
packet_status: Live
command_payload {
  initiateFOTACommand {
    totalNoOfFiles: "3"
    firmwareDownloadPayload {
    }
    firmwareDownloadPayload {
      seqNo: "\000\000"
    }
  }
}

>>> a.ListFields()
[(<google.protobuf.pyext._message.FieldDescriptor object at 0x0000014895836E60>, '33'), (<google.protobuf.pyext._message.FieldDescriptor object at 0x000001489538CF40>, '4'), (<google.protobuf.pyext._message.FieldDescriptor object at 0x00000148951A7C40>, 'MH12'), (<google.protobuf.pyext._message.FieldDescriptor object at 0x0000014895309CC0>, 4), (<google.protobuf.pyext._message.FieldDescriptor object at 0x0000014895BEAC80>, 'priority'), (<google.protobuf.pyext._message.FieldDescriptor object at 0x0000014895BEAA10>, 1), (<google.protobuf.pyext._message.FieldDescriptor object at 0x0000014895BEAEF0>, '2.2'), (<google.protobuf.pyext._message.FieldDescriptor object at 0x0000014895BEB040>, seconds: 1707807003   
nanos: 680155000
), (<google.protobuf.pyext._message.FieldDescriptor object at 0x0000014895BEB160>, 76), (<google.protobuf.pyext._message.FieldDescriptor object at 0x0000014895BEAF50>, initiateFOTACommand {
  totalNoOfFiles: "3"
  firmwareDownloadPayload {
  }
  firmwareDownloadPayload {
    seqNo: "\000\000"
  }
}
)]
>>> a.SerializeToString()
b'\n\x0233\x12\x014\x1a\x04MH12(\x042\x08priority8\x01B\x032.2J\x0c\x08\x9b\xa2\xac\xae\x06\x10\xf8\xae\xa9\xc4\x02PLZ\r*\x0b\n\x013\x12\x00\x12\x04\n\x02\x00\x00'
>>> import paho.mqtt.client as mqtt
>>> mqttBroker = "test.mosquitto.org"
>>> client = mqtt.Client('test')          
>>> client.connect(mqttBroker, 1883)
0
>>> client.loop_start()
>>> client.publish("/device/ACCDEV14012078186/MQTTPROTOBUF/command", a.SerializeToString()) 
<paho.mqtt.client.MQTTMessageInfo object at 0x00000148979F3380>
>>> client.publish("/device/ACCDEV14012078186/MQTTPROTOBUF/command", a.SerializeToString())
<paho.mqtt.client.MQTTMessageInfo object at 0x00000148979F35B0>
>>> s = a.SerializeToString()         
>>> f = ''.join('{:02x}'.format(x) for x in s)
>>> print(f)
0a0233331201341a044d483132280432087072696f7269747938014203322e324a0c089ba2acae0610f8aea9c402504c5a0d2a0b0a0133120012040a020000
>>> a
message_id: "33"
correlation_id: "4"
vehicle_id: "MH12"
subtype: InitiateFOTACommand
priority: "priority"
provisioning_state: provisioned
version: "2.2"
time_stamp {
  seconds: 1707807003
  nanos: 680155000
}
packet_status: Live
command_payload {
  initiateFOTACommand {
    totalNoOfFiles: "3"
    firmwareDownloadPayload {
    }
    firmwareDownloadPayload {
      seqNo: "\000\000"
    }
  }
}

>>> a
message_id: "33"
correlation_id: "4"
vehicle_id: "MH12"
subtype: InitiateFOTACommand
priority: "priority"
provisioning_state: provisioned
version: "2.2"
time_stamp {
  seconds: 1707807003
  nanos: 680155000
}
packet_status: Live
command_payload {
  initiateFOTACommand {
    totalNoOfFiles: "3"
    firmwareDownloadPayload {
    }
    firmwareDownloadPayload {
      seqNo: "\000\000"
    }
  }
}

>>> cmd.InitiateFota
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'tmcvp_command_pb2' has no attribute 'InitiateFota'
>>> cmdMsg.InitiateFOTACommand
4
>>>     