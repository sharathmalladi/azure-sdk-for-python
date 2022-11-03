# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class CreatedByType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity that created the resource."""

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"


class MultiFactorAuthProvider(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The multi-factor authorization provider to be used for just-in-time access requests."""

    AZURE = "Azure"
    NONE = "None"


class ProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The current provisioning state of the registration definition."""

    NOT_SPECIFIED = "NotSpecified"
    ACCEPTED = "Accepted"
    RUNNING = "Running"
    READY = "Ready"
    CREATING = "Creating"
    CREATED = "Created"
    DELETING = "Deleting"
    DELETED = "Deleted"
    CANCELED = "Canceled"
    FAILED = "Failed"
    SUCCEEDED = "Succeeded"
    UPDATING = "Updating"
