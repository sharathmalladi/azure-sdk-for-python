# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import ClassicAdministrator
from ._models_py3 import ClassicAdministratorListResult
from ._models_py3 import ErrorAdditionalInfo
from ._models_py3 import ErrorDetail
from ._models_py3 import ErrorResponse
from ._models_py3 import Permission
from ._models_py3 import PermissionGetResult
from ._models_py3 import ProviderOperation
from ._models_py3 import ProviderOperationsMetadata
from ._models_py3 import ProviderOperationsMetadataListResult
from ._models_py3 import ResourceType
from ._models_py3 import RoleAssignment
from ._models_py3 import RoleAssignmentCreateParameters
from ._models_py3 import RoleAssignmentFilter
from ._models_py3 import RoleAssignmentListResult
from ._models_py3 import RoleAssignmentProperties
from ._models_py3 import RoleAssignmentPropertiesWithScope
from ._models_py3 import RoleDefinition
from ._models_py3 import RoleDefinitionFilter
from ._models_py3 import RoleDefinitionListResult
from ._patch import __all__ as _patch_all
from ._patch import *  # type: ignore # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "ClassicAdministrator",
    "ClassicAdministratorListResult",
    "ErrorAdditionalInfo",
    "ErrorDetail",
    "ErrorResponse",
    "Permission",
    "PermissionGetResult",
    "ProviderOperation",
    "ProviderOperationsMetadata",
    "ProviderOperationsMetadataListResult",
    "ResourceType",
    "RoleAssignment",
    "RoleAssignmentCreateParameters",
    "RoleAssignmentFilter",
    "RoleAssignmentListResult",
    "RoleAssignmentProperties",
    "RoleAssignmentPropertiesWithScope",
    "RoleDefinition",
    "RoleDefinitionFilter",
    "RoleDefinitionListResult",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
