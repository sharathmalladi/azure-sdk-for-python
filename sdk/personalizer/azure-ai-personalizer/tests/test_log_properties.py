from devtools_testutils import AzureTestCase
import personalizer_helpers

class TestLogProperties(AzureTestCase):

    @personalizer_helpers.PersonalizerPreparer()
    def test_delete_log(self, **kwargs):
        personalizer_endpoint = kwargs.pop('personalizer_endpoint_multi_slot')
        personalizer_api_key = kwargs.pop('personalizer_api_key_multi_slot')
        client =  personalizer_helpers.create_personalizer_client(personalizer_endpoint, personalizer_api_key)
        client.log.delete()
        log_properties = client.log.get_properties()
        date_range = log_properties.get("dateRange")
        if date_range is not None:
            assert "from" in date_range
            assert date_range["from"] is None
            assert "to" in date_range
            assert date_range["to"] is None