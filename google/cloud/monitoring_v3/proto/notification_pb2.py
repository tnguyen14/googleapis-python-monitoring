# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/monitoring_v3/proto/notification.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import label_pb2 as google_dot_api_dot_label__pb2
from google.api import launch_stage_pb2 as google_dot_api_dot_launch__stage__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.cloud.monitoring_v3.proto import (
    common_pb2 as google_dot_cloud_dot_monitoring__v3_dot_proto_dot_common__pb2,
)
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/monitoring_v3/proto/notification.proto",
    package="google.monitoring.v3",
    syntax="proto3",
    serialized_options=b"\n\030com.google.monitoring.v3B\021NotificationProtoP\001Z>google.golang.org/genproto/googleapis/monitoring/v3;monitoring\252\002\032Google.Cloud.Monitoring.V3\312\002\032Google\\Cloud\\Monitoring\\V3\352\002\035Google::Cloud::Monitoring::V3",
    serialized_pb=b'\n3google/cloud/monitoring_v3/proto/notification.proto\x12\x14google.monitoring.v3\x1a\x16google/api/label.proto\x1a\x1dgoogle/api/launch_stage.proto\x1a\x19google/api/resource.proto\x1a-google/cloud/monitoring_v3/proto/common.proto\x1a\x1egoogle/protobuf/wrappers.proto"\xa5\x04\n\x1dNotificationChannelDescriptor\x12\x0c\n\x04name\x18\x06 \x01(\t\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12+\n\x06labels\x18\x04 \x03(\x0b\x32\x1b.google.api.LabelDescriptor\x12>\n\x0fsupported_tiers\x18\x05 \x03(\x0e\x32!.google.monitoring.v3.ServiceTierB\x02\x18\x01\x12-\n\x0claunch_stage\x18\x07 \x01(\x0e\x32\x17.google.api.LaunchStage:\xa0\x02\xea\x41\x9c\x02\n7monitoring.googleapis.com/NotificationChannelDescriptor\x12\x46projects/{project}/notificationChannelDescriptors/{channel_descriptor}\x12Porganizations/{organization}/notificationChannelDescriptors/{channel_descriptor}\x12\x44\x66olders/{folder}/notificationChannelDescriptors/{channel_descriptor}\x12\x01*"\xb7\x06\n\x13NotificationChannel\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x06 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x45\n\x06labels\x18\x05 \x03(\x0b\x32\x35.google.monitoring.v3.NotificationChannel.LabelsEntry\x12N\n\x0buser_labels\x18\x08 \x03(\x0b\x32\x39.google.monitoring.v3.NotificationChannel.UserLabelsEntry\x12Y\n\x13verification_status\x18\t \x01(\x0e\x32<.google.monitoring.v3.NotificationChannel.VerificationStatus\x12+\n\x07\x65nabled\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x31\n\x0fUserLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"W\n\x12VerificationStatus\x12#\n\x1fVERIFICATION_STATUS_UNSPECIFIED\x10\x00\x12\x0e\n\nUNVERIFIED\x10\x01\x12\x0c\n\x08VERIFIED\x10\x02:\xfe\x01\xea\x41\xfa\x01\n-monitoring.googleapis.com/NotificationChannel\x12>projects/{project}/notificationChannels/{notification_channel}\x12Horganizations/{organization}/notificationChannels/{notification_channel}\x12<folders/{folder}/notificationChannels/{notification_channel}\x12\x01*B\xc9\x01\n\x18\x63om.google.monitoring.v3B\x11NotificationProtoP\x01Z>google.golang.org/genproto/googleapis/monitoring/v3;monitoring\xaa\x02\x1aGoogle.Cloud.Monitoring.V3\xca\x02\x1aGoogle\\Cloud\\Monitoring\\V3\xea\x02\x1dGoogle::Cloud::Monitoring::V3b\x06proto3',
    dependencies=[
        google_dot_api_dot_label__pb2.DESCRIPTOR,
        google_dot_api_dot_launch__stage__pb2.DESCRIPTOR,
        google_dot_api_dot_resource__pb2.DESCRIPTOR,
        google_dot_cloud_dot_monitoring__v3_dot_proto_dot_common__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,
    ],
)


_NOTIFICATIONCHANNEL_VERIFICATIONSTATUS = _descriptor.EnumDescriptor(
    name="VerificationStatus",
    full_name="google.monitoring.v3.NotificationChannel.VerificationStatus",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="VERIFICATION_STATUS_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="UNVERIFIED", index=1, number=1, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="VERIFIED", index=2, number=2, serialized_options=None, type=None
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=1270,
    serialized_end=1357,
)
_sym_db.RegisterEnumDescriptor(_NOTIFICATIONCHANNEL_VERIFICATIONSTATUS)


_NOTIFICATIONCHANNELDESCRIPTOR = _descriptor.Descriptor(
    name="NotificationChannelDescriptor",
    full_name="google.monitoring.v3.NotificationChannelDescriptor",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.monitoring.v3.NotificationChannelDescriptor.name",
            index=0,
            number=6,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="type",
            full_name="google.monitoring.v3.NotificationChannelDescriptor.type",
            index=1,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="display_name",
            full_name="google.monitoring.v3.NotificationChannelDescriptor.display_name",
            index=2,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="description",
            full_name="google.monitoring.v3.NotificationChannelDescriptor.description",
            index=3,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="labels",
            full_name="google.monitoring.v3.NotificationChannelDescriptor.labels",
            index=4,
            number=4,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="supported_tiers",
            full_name="google.monitoring.v3.NotificationChannelDescriptor.supported_tiers",
            index=5,
            number=5,
            type=14,
            cpp_type=8,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\030\001",
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="launch_stage",
            full_name="google.monitoring.v3.NotificationChannelDescriptor.launch_stage",
            index=6,
            number=7,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b"\352A\234\002\n7monitoring.googleapis.com/NotificationChannelDescriptor\022Fprojects/{project}/notificationChannelDescriptors/{channel_descriptor}\022Porganizations/{organization}/notificationChannelDescriptors/{channel_descriptor}\022Dfolders/{folder}/notificationChannelDescriptors/{channel_descriptor}\022\001*",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=239,
    serialized_end=788,
)


_NOTIFICATIONCHANNEL_LABELSENTRY = _descriptor.Descriptor(
    name="LabelsEntry",
    full_name="google.monitoring.v3.NotificationChannel.LabelsEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="google.monitoring.v3.NotificationChannel.LabelsEntry.key",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="value",
            full_name="google.monitoring.v3.NotificationChannel.LabelsEntry.value",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b"8\001",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1172,
    serialized_end=1217,
)

_NOTIFICATIONCHANNEL_USERLABELSENTRY = _descriptor.Descriptor(
    name="UserLabelsEntry",
    full_name="google.monitoring.v3.NotificationChannel.UserLabelsEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="google.monitoring.v3.NotificationChannel.UserLabelsEntry.key",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="value",
            full_name="google.monitoring.v3.NotificationChannel.UserLabelsEntry.value",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b"8\001",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1219,
    serialized_end=1268,
)

_NOTIFICATIONCHANNEL = _descriptor.Descriptor(
    name="NotificationChannel",
    full_name="google.monitoring.v3.NotificationChannel",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="type",
            full_name="google.monitoring.v3.NotificationChannel.type",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.monitoring.v3.NotificationChannel.name",
            index=1,
            number=6,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="display_name",
            full_name="google.monitoring.v3.NotificationChannel.display_name",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="description",
            full_name="google.monitoring.v3.NotificationChannel.description",
            index=3,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="labels",
            full_name="google.monitoring.v3.NotificationChannel.labels",
            index=4,
            number=5,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="user_labels",
            full_name="google.monitoring.v3.NotificationChannel.user_labels",
            index=5,
            number=8,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="verification_status",
            full_name="google.monitoring.v3.NotificationChannel.verification_status",
            index=6,
            number=9,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="enabled",
            full_name="google.monitoring.v3.NotificationChannel.enabled",
            index=7,
            number=11,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[
        _NOTIFICATIONCHANNEL_LABELSENTRY,
        _NOTIFICATIONCHANNEL_USERLABELSENTRY,
    ],
    enum_types=[_NOTIFICATIONCHANNEL_VERIFICATIONSTATUS],
    serialized_options=b"\352A\372\001\n-monitoring.googleapis.com/NotificationChannel\022>projects/{project}/notificationChannels/{notification_channel}\022Horganizations/{organization}/notificationChannels/{notification_channel}\022<folders/{folder}/notificationChannels/{notification_channel}\022\001*",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=791,
    serialized_end=1614,
)

_NOTIFICATIONCHANNELDESCRIPTOR.fields_by_name[
    "labels"
].message_type = google_dot_api_dot_label__pb2._LABELDESCRIPTOR
_NOTIFICATIONCHANNELDESCRIPTOR.fields_by_name[
    "supported_tiers"
].enum_type = google_dot_cloud_dot_monitoring__v3_dot_proto_dot_common__pb2._SERVICETIER
_NOTIFICATIONCHANNELDESCRIPTOR.fields_by_name[
    "launch_stage"
].enum_type = google_dot_api_dot_launch__stage__pb2._LAUNCHSTAGE
_NOTIFICATIONCHANNEL_LABELSENTRY.containing_type = _NOTIFICATIONCHANNEL
_NOTIFICATIONCHANNEL_USERLABELSENTRY.containing_type = _NOTIFICATIONCHANNEL
_NOTIFICATIONCHANNEL.fields_by_name[
    "labels"
].message_type = _NOTIFICATIONCHANNEL_LABELSENTRY
_NOTIFICATIONCHANNEL.fields_by_name[
    "user_labels"
].message_type = _NOTIFICATIONCHANNEL_USERLABELSENTRY
_NOTIFICATIONCHANNEL.fields_by_name[
    "verification_status"
].enum_type = _NOTIFICATIONCHANNEL_VERIFICATIONSTATUS
_NOTIFICATIONCHANNEL.fields_by_name[
    "enabled"
].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_NOTIFICATIONCHANNEL_VERIFICATIONSTATUS.containing_type = _NOTIFICATIONCHANNEL
DESCRIPTOR.message_types_by_name[
    "NotificationChannelDescriptor"
] = _NOTIFICATIONCHANNELDESCRIPTOR
DESCRIPTOR.message_types_by_name["NotificationChannel"] = _NOTIFICATIONCHANNEL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NotificationChannelDescriptor = _reflection.GeneratedProtocolMessageType(
    "NotificationChannelDescriptor",
    (_message.Message,),
    {
        "DESCRIPTOR": _NOTIFICATIONCHANNELDESCRIPTOR,
        "__module__": "google.cloud.monitoring_v3.proto.notification_pb2",
        "__doc__": """A description of a notification channel. The descriptor includes the
  properties of the channel and the set of labels or fields that must be
  specified to configure channels of a given type.
  Attributes:
      name:
          The full REST resource name for this descriptor. The format
          is:  ::     projects/[PROJECT_ID_OR_NUMBER]/notificationChanne
          lDescriptors/[TYPE]  In the above, ``[TYPE]`` is the value of
          the ``type`` field.
      type:
          The type of notification channel, such as “email”, “sms”, etc.
          Notification channel types are globally unique.
      display_name:
          A human-readable name for the notification channel type. This
          form of the name is suitable for a user interface.
      description:
          A human-readable description of the notification channel type.
          The description may include a description of the properties of
          the channel and pointers to external documentation.
      labels:
          The set of labels that must be defined to identify a
          particular channel of the corresponding type. Each label
          includes a description for how that field should be populated.
      supported_tiers:
          The tiers that support this notification channel; the project
          service tier must be one of the supported_tiers.
      launch_stage:
          The product launch stage for channels of this type.
  """,
        # @@protoc_insertion_point(class_scope:google.monitoring.v3.NotificationChannelDescriptor)
    },
)
_sym_db.RegisterMessage(NotificationChannelDescriptor)

NotificationChannel = _reflection.GeneratedProtocolMessageType(
    "NotificationChannel",
    (_message.Message,),
    {
        "LabelsEntry": _reflection.GeneratedProtocolMessageType(
            "LabelsEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _NOTIFICATIONCHANNEL_LABELSENTRY,
                "__module__": "google.cloud.monitoring_v3.proto.notification_pb2"
                # @@protoc_insertion_point(class_scope:google.monitoring.v3.NotificationChannel.LabelsEntry)
            },
        ),
        "UserLabelsEntry": _reflection.GeneratedProtocolMessageType(
            "UserLabelsEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _NOTIFICATIONCHANNEL_USERLABELSENTRY,
                "__module__": "google.cloud.monitoring_v3.proto.notification_pb2"
                # @@protoc_insertion_point(class_scope:google.monitoring.v3.NotificationChannel.UserLabelsEntry)
            },
        ),
        "DESCRIPTOR": _NOTIFICATIONCHANNEL,
        "__module__": "google.cloud.monitoring_v3.proto.notification_pb2",
        "__doc__": """A ``NotificationChannel`` is a medium through which an alert is
  delivered when a policy violation is detected. Examples of channels
  include email, SMS, and third-party messaging applications. Fields
  containing sensitive information like authentication tokens or contact
  info are only partially populated on retrieval.
  Attributes:
      type:
          The type of the notification channel. This field matches the
          value of the [NotificationChannelDescriptor.type][google.monit
          oring.v3.NotificationChannelDescriptor.type] field.
      name:
          The full REST resource name for this channel. The format is:
          ::     projects/[PROJECT_ID_OR_NUMBER]/notificationChannels/[C
          HANNEL_ID]  The ``[CHANNEL_ID]`` is automatically assigned by
          the server on creation.
      display_name:
          An optional human-readable name for this notification channel.
          It is recommended that you specify a non-empty and unique name
          in order to make it easier to identify the channels in your
          project, though this is not enforced. The display name is
          limited to 512 Unicode characters.
      description:
          An optional human-readable description of this notification
          channel. This description may provide additional details,
          beyond the display name, for the channel. This may not exceed
          1024 Unicode characters.
      labels:
          Configuration fields that define the channel and its behavior.
          The permissible and required labels are specified in the [Noti
          ficationChannelDescriptor.labels][google.monitoring.v3.Notific
          ationChannelDescriptor.labels] of the
          ``NotificationChannelDescriptor`` corresponding to the
          ``type`` field.
      user_labels:
          User-supplied key/value data that does not need to conform to
          the corresponding ``NotificationChannelDescriptor``\ ’s
          schema, unlike the ``labels`` field. This field is intended to
          be used for organizing and identifying the
          ``NotificationChannel`` objects.  The field can contain up to
          64 entries. Each key and value is limited to 63 Unicode
          characters or 128 bytes, whichever is smaller. Labels and
          values can contain only lowercase letters, numerals,
          underscores, and dashes. Keys must begin with a letter.
      verification_status:
          Indicates whether this channel has been verified or not. On a 
          [``ListNotificationChannels``][google.monitoring.v3.Notificati
          onChannelService.ListNotificationChannels] or [``GetNotificati
          onChannel``][google.monitoring.v3.NotificationChannelService.G
          etNotificationChannel] operation, this field is expected to be
          populated.  If the value is ``UNVERIFIED``, then it indicates
          that the channel is non-functioning (it both requires
          verification and lacks verification); otherwise, it is assumed
          that the channel works.  If the channel is neither
          ``VERIFIED`` nor ``UNVERIFIED``, it implies that the channel
          is of a type that does not require verification or that this
          specific channel has been exempted from verification because
          it was created prior to verification being required for
          channels of this type.  This field cannot be modified using a
          standard [``UpdateNotificationChannel``][google.monitoring.v3.
          NotificationChannelService.UpdateNotificationChannel]
          operation. To change the value of this field, you must call [`
          `VerifyNotificationChannel``][google.monitoring.v3.Notificatio
          nChannelService.VerifyNotificationChannel].
      enabled:
          Whether notifications are forwarded to the described channel.
          This makes it possible to disable delivery of notifications to
          a particular channel without removing the channel from all
          alerting policies that reference the channel. This is a more
          convenient approach when the change is temporary and you want
          to receive notifications from the same set of alerting
          policies on the channel at some point in the future.
  """,
        # @@protoc_insertion_point(class_scope:google.monitoring.v3.NotificationChannel)
    },
)
_sym_db.RegisterMessage(NotificationChannel)
_sym_db.RegisterMessage(NotificationChannel.LabelsEntry)
_sym_db.RegisterMessage(NotificationChannel.UserLabelsEntry)


DESCRIPTOR._options = None
_NOTIFICATIONCHANNELDESCRIPTOR.fields_by_name["supported_tiers"]._options = None
_NOTIFICATIONCHANNELDESCRIPTOR._options = None
_NOTIFICATIONCHANNEL_LABELSENTRY._options = None
_NOTIFICATIONCHANNEL_USERLABELSENTRY._options = None
_NOTIFICATIONCHANNEL._options = None
# @@protoc_insertion_point(module_scope)
