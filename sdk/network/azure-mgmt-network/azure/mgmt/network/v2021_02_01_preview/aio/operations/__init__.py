# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._operations import NetworkManagersOperations
from ._operations import NetworkManagerCommitsOperations
from ._operations import NetworkManagerDeploymentStatusOperations
from ._operations import EffectiveVirtualNetworksOperations
from ._operations import ActiveConnectivityConfigurationsOperations
from ._operations import ActiveSecurityAdminRulesOperations
from ._operations import ActiveSecurityUserRulesOperations
from ._operations import ConnectivityConfigurationsOperations
from ._operations import EffectiveConnectivityConfigurationsOperations
from ._operations import NetworkManagerEffectiveSecurityAdminRulesOperations
from ._operations import NetworkGroupsOperations
from ._operations import SecurityUserConfigurationsOperations
from ._operations import UserRuleCollectionsOperations
from ._operations import UserRulesOperations
from ._operations import SecurityAdminConfigurationsOperations
from ._operations import AdminRuleCollectionsOperations
from ._operations import AdminRulesOperations
from ._operations import NetworkSecurityPerimetersOperations
from ._operations import NspProfilesOperations
from ._operations import NspAccessRulesOperations
from ._operations import NspAssociationsOperations
from ._operations import NspAssociationReconcileOperations
from ._operations import PerimeterAssociableResourceTypesOperations
from ._operations import NspAccessRulesReconcileOperations
from ._operations import NspLinksOperations
from ._operations import NspLinkReconcileOperations
from ._operations import NspLinkReferencesOperations
from ._operations import NspLinkReferenceReconcileOperations

from ._patch import __all__ as _patch_all
from ._patch import *  # type: ignore # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "NetworkManagersOperations",
    "NetworkManagerCommitsOperations",
    "NetworkManagerDeploymentStatusOperations",
    "EffectiveVirtualNetworksOperations",
    "ActiveConnectivityConfigurationsOperations",
    "ActiveSecurityAdminRulesOperations",
    "ActiveSecurityUserRulesOperations",
    "ConnectivityConfigurationsOperations",
    "EffectiveConnectivityConfigurationsOperations",
    "NetworkManagerEffectiveSecurityAdminRulesOperations",
    "NetworkGroupsOperations",
    "SecurityUserConfigurationsOperations",
    "UserRuleCollectionsOperations",
    "UserRulesOperations",
    "SecurityAdminConfigurationsOperations",
    "AdminRuleCollectionsOperations",
    "AdminRulesOperations",
    "NetworkSecurityPerimetersOperations",
    "NspProfilesOperations",
    "NspAccessRulesOperations",
    "NspAssociationsOperations",
    "NspAssociationReconcileOperations",
    "PerimeterAssociableResourceTypesOperations",
    "NspAccessRulesReconcileOperations",
    "NspLinksOperations",
    "NspLinkReconcileOperations",
    "NspLinkReferencesOperations",
    "NspLinkReferenceReconcileOperations",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
