# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Person.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Person.proto',
  package='tutorial',
  serialized_pb='\n\x0cPerson.proto\x12\x08tutorial\"1\n\x06Person\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x0c\n\x04name\x18\x02 \x02(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t')




_PERSON = _descriptor.Descriptor(
  name='Person',
  full_name='tutorial.Person',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='tutorial.Person.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='tutorial.Person.name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='email', full_name='tutorial.Person.email', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=26,
  serialized_end=75,
)

DESCRIPTOR.message_types_by_name['Person'] = _PERSON

class Person(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PERSON

  # @@protoc_insertion_point(class_scope:tutorial.Person)


# @@protoc_insertion_point(module_scope)