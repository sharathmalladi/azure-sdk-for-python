# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.deploymentmanager import AzureDeploymentManager

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-deploymentmanager
# USAGE
    python create_a_topology_with_artifact_source.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = AzureDeploymentManager(
        credential=DefaultAzureCredential(),
        subscription_id="caac1590-e859-444f-a9e0-62091c0f5929",
    )

    response = client.service_topologies.create_or_update(
        resource_group_name="myResourceGroup",
        service_topology_name="myTopology",
        service_topology_info={
            "location": "centralus",
            "properties": {"artifactSourceId": "Microsoft.DeploymentManager/artifactSources/myArtifactSource"},
            "tags": {},
        },
    )
    print(response)


# x-ms-original-file: specification/deploymentmanager/resource-manager/Microsoft.DeploymentManager/preview/2019-11-01-preview/examples/servicetopology_createorupdate.json
if __name__ == "__main__":
    main()
