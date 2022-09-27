# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
FILE: rank_actions_and_reward_events_async.py
DESCRIPTION:
    This sample demos sending a rank and reward call to personalizer
USAGE: python rank_actions_and_reward_events_async.py
"""
import asyncio

from util import get_async_personalizer_client


async def main():
    client = get_async_personalizer_client()

    actions = [
        {
            "id": "Video1",
            "features": [
                {"videoType": "documentary", "videoLength": 35, "director": "CarlSagan"},
                {"mostWatchedByAge": "50-55"},
            ],
        },
        {
            "id": "Video2",
            "features": [
                {"videoType": "movie", "videoLength": 120, "director": "StevenSpielberg"},
                {"mostWatchedByAge": "40-45"},
            ],
        },
    ]
    context_features = [
        {"Features": {"day": "tuesday", "time": "night", "weather": "rainy"}},
        {
            "Features": {
                "payingUser": True,
                "favoriteGenre": "documentary",
                "hoursOnSite": 0.12,
                "lastWatchedType": "movie",
            },
        },
    ]

    request = {
        "actions": actions,
        "contextFeatures": context_features,
    }

    print("Sending rank request")
    rank_response = await client.rank(request)
    print("Rank returned response with event id {} and recommended {} as the best action"
          .format(rank_response.get("eventId"), rank_response.get("rewardActionId")))

    # The event response will be determined by how the user interacted with the action that was presented to them.
    # Let us say that they like the action. So we associate a reward of 1.
    print("Sending reward event")
    await client.events.reward(rank_response.get("eventId"), {"value": 1.0})
    print("Completed sending reward response")


if __name__ == "__main__":
    asyncio.run(main())
