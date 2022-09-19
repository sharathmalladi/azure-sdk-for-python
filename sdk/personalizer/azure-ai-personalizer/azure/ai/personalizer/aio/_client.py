# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Awaitable, TYPE_CHECKING

from azure.core import AsyncPipelineClient
from azure.core.credentials import AzureKeyCredential
from azure.core.rest import AsyncHttpResponse, HttpRequest

from .._serialization import Deserializer, Serializer
from ._configuration import PersonalizerClientConfiguration
from .operations import (
    EvaluationsOperations,
    EventsOperations,
    FeatureImportancesOperations,
    LogOperations,
    ModelOperations,
    MultiSlotEventsOperations,
    MultiSlotOperations,
    PersonalizerClientOperationsMixin,
    PolicyOperations,
    ServiceConfigurationOperations,
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Dict


class PersonalizerClient(
    PersonalizerClientOperationsMixin
):  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """Personalizer Service is an Azure Cognitive Service that makes it easy to target content and
    experiences without complex pre-analysis or cleanup of past data. Given a context and
    featurized content, the Personalizer Service returns which content item to show to users in
    rewardActionId. As rewards are sent in response to the use of rewardActionId, the reinforcement
    learning algorithm will improve the model and improve performance of future rank calls.

    :ivar service_configuration: ServiceConfigurationOperations operations
    :vartype service_configuration:
     azure.ai.personalizer.aio.operations.ServiceConfigurationOperations
    :ivar policy: PolicyOperations operations
    :vartype policy: azure.ai.personalizer.aio.operations.PolicyOperations
    :ivar evaluations: EvaluationsOperations operations
    :vartype evaluations: azure.ai.personalizer.aio.operations.EvaluationsOperations
    :ivar events: EventsOperations operations
    :vartype events: azure.ai.personalizer.aio.operations.EventsOperations
    :ivar feature_importances: FeatureImportancesOperations operations
    :vartype feature_importances: azure.ai.personalizer.aio.operations.FeatureImportancesOperations
    :ivar log: LogOperations operations
    :vartype log: azure.ai.personalizer.aio.operations.LogOperations
    :ivar model: ModelOperations operations
    :vartype model: azure.ai.personalizer.aio.operations.ModelOperations
    :ivar multi_slot_events: MultiSlotEventsOperations operations
    :vartype multi_slot_events: azure.ai.personalizer.aio.operations.MultiSlotEventsOperations
    :ivar multi_slot: MultiSlotOperations operations
    :vartype multi_slot: azure.ai.personalizer.aio.operations.MultiSlotOperations
    :param endpoint: Supported Cognitive Services endpoint. Required.
    :type endpoint: str
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials.AzureKeyCredential
    :keyword api_version: Api Version. Default value is "2022-09-01-preview". Note that overriding
     this default value may result in unsupported behavior.
    :paramtype api_version: str
    """

    def __init__(self, endpoint: str, credential: AzureKeyCredential, **kwargs: Any) -> None:
        _endpoint = "{Endpoint}/personalizer"
        self._config = PersonalizerClientConfiguration(endpoint=endpoint, credential=credential, **kwargs)
        self._client = AsyncPipelineClient(base_url=_endpoint, config=self._config, **kwargs)

        self._serialize = Serializer()
        self._deserialize = Deserializer()
        self._serialize.client_side_validation = False
        self.service_configuration = ServiceConfigurationOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.policy = PolicyOperations(self._client, self._config, self._serialize, self._deserialize)
        self.evaluations = EvaluationsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.events = EventsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.feature_importances = FeatureImportancesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.log = LogOperations(self._client, self._config, self._serialize, self._deserialize)
        self.model = ModelOperations(self._client, self._config, self._serialize, self._deserialize)
        self.multi_slot_events = MultiSlotEventsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.multi_slot = MultiSlotOperations(self._client, self._config, self._serialize, self._deserialize)

    def send_request(self, request: HttpRequest, **kwargs: Any) -> Awaitable[AsyncHttpResponse]:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = await client.send_request(request)
        <AsyncHttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.AsyncHttpResponse
        """

        request_copy = deepcopy(request)
        path_format_arguments = {
            "Endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }

        request_copy.url = self._client.format_url(request_copy.url, **path_format_arguments)
        return self._client.send_request(request_copy, **kwargs)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "PersonalizerClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
