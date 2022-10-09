import pytest
from devtools_testutils import AzureRecordedTestCase
from devtools_testutils.aio import recorded_by_proxy_async
import personalizer_helpers_async

import personalizer_helpers


class TestMultiSlotEventAsync(AzureRecordedTestCase):

    @personalizer_helpers.PersonalizerPreparer()
    @recorded_by_proxy_async
    async def test_multi_slot_reward(self, **kwargs):
        personalizer_endpoint = kwargs.pop('personalizer_endpoint_multi_slot')
        personalizer_api_key = kwargs.pop('personalizer_api_key_multi_slot')
        client = personalizer_helpers_async.create_async_personalizer_client(personalizer_endpoint, personalizer_api_key)
        event_id = "123456789"
        await client.multi_slot_events.reward(event_id, {"reward": [{"slotId": "slot_id_to_be_rewarded", "value": 1.0}]})

    @personalizer_helpers.PersonalizerPreparer()
    @recorded_by_proxy_async
    async def test_multi_slot_activate(self, **kwargs):
        personalizer_endpoint = kwargs.pop('personalizer_endpoint_multi_slot')
        personalizer_api_key = kwargs.pop('personalizer_api_key_multi_slot')
        client = personalizer_helpers_async.create_async_personalizer_client(personalizer_endpoint, personalizer_api_key)
        event_id = "123456789"
        await client.multi_slot_events.activate(event_id)
