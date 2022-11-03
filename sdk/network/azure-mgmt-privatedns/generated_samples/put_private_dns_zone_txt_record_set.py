# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.privatedns import PrivateDnsManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-privatedns
# USAGE
    python put_private_dns_zone_txt_record_set.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = PrivateDnsManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="subscriptionId",
    )

    response = client.record_sets.create_or_update(
        resource_group_name="resourceGroup1",
        private_zone_name="privatezone1.com",
        record_type="TXT",
        relative_record_set_name="recordTXT",
        parameters={
            "properties": {
                "metadata": {"key1": "value1"},
                "ttl": 3600,
                "txtRecords": [{"value": ["string1", "string2"]}],
            }
        },
    )
    print(response)


# x-ms-original-file: specification/privatedns/resource-manager/Microsoft.Network/stable/2020-06-01/examples/RecordSetTXTPut.json
if __name__ == "__main__":
    main()
