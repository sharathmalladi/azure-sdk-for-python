from devtools_testutils import AzureRecordedTestCase
import helpers


class TestMultiSlotRank(AzureRecordedTestCase):

    @helpers.PersonalizerPreparer()
    def test_rank_with_no_context_features(self, **kwargs):
        personalizer_endpoint = kwargs.pop('personalizer_endpoint_multi_slot')
        personalizer_api_key = kwargs.pop('personalizer_api_key_multi_slot')
        client = helpers.create_personalizer_client(personalizer_endpoint, personalizer_api_key)
        event_id = "123456789";
        request = {"actions": get_actions(), "slots": get_slots(), "eventId": event_id}
        response = client.multi_slot.rank(request)
        assert event_id == response.get("eventId")
        slots = response.get("slots")
        assert len(slots) == len(get_slots())
        assert slots[0]['rewardActionId'] == "NewsArticle"
        assert slots[1]['rewardActionId'] == "SportsArticle"

    @helpers.PersonalizerPreparer()
    def test_rank_with_context_features(self, **kwargs):
        personalizer_endpoint = kwargs.pop('personalizer_endpoint_multi_slot')
        personalizer_api_key = kwargs.pop('personalizer_api_key_multi_slot')
        client = helpers.create_personalizer_client(personalizer_endpoint, personalizer_api_key)
        event_id = "123456789"
        request = {
            "eventId": event_id,
            "actions": get_actions(),
            "slots": get_slots(),
            "contextFeatures": get_context_features()
        }
        response = client.multi_slot.rank(request)
        slots = response.get("slots")
        assert len(slots) == len(get_slots())
        assert slots[0]['rewardActionId'] == "NewsArticle"
        assert slots[1]['rewardActionId'] == "SportsArticle"


def get_actions():
    return [
        {"id": "NewsArticle", "features": [{"type": "News"}]},
        {"id": "SportsArticle", "features": [{"type": "Sports"}]},
        {"id": "EntertainmentArticle", "features": [{"type": "Entertainment"}]},
    ]


def get_context_features():
    return [
        {"User": {"ProfileType": "AnonymousUser", "LatLong": "47.6,-122.1"}},
        {"Environment": {"DayOfMonth": "28", "MonthOfYear": "8", "Weather": "Sunny"}},
        {"Device": {"Mobile": True, "Windows": True}},
        {"RecentActivity": {"ItemsInCart": 3}},
    ]


def get_slots():
    return [{
        "id": "Main Article",
        "baselineAction": "NewsArticle",
        "features": [{"Size": "Large", "Position": "Top Middle"}],
        "excludedActions": ["SportsArticle", "EntertainmentArticle"],
    },
    {
        "id": "Side Bar",
        "baselineAction": "SportsArticle",
        "features": [{"Size": "Small", "Position": "Bottom Right"}],
        "excludedActions": ["EntertainmentArticle"],
    }]
