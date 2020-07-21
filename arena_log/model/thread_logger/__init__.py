from arena_log.model.thread_logger import deck, event, inventory, \
    player_inventory, post_match, progression, track_reward_tier

THREAD_FACTORY = {
    'Deck.CreateDeckV3': deck.CreateDeckV3,
    'Deck.GetDeckListsV3': deck.GetDeckListsV3,
    'Deck.GetPreconDecksV3': deck.GetPreconDecksV3,
    'Deck.UpdateDeckV3': deck.UpdateDeckV3,
    'Event.UpdateDeckV3': event.UpdateDeckV3,
    'Event.DeckSubmitV3': event.DeckSubmitV3,
    'Event.GetActiveEventsV2': event.GetActiveEventsV2,
    'Event.GetActiveMatches': event.GetActiveMatches,
    'Event.GetCombinedRankInfo': event.GetCombinedRankInfo,
    'Event.GetPlayerCourseV2': event.GetPlayerCourseV2,
    'Event.GetPlayerCoursesV2': event.GetPlayerCoursesV2,
    'Event.GetSeasonAndRankDetail': event.GetSeasonAndRankDetail,
    'Event.Join': event.Join,
    'Event.JoinQueue': event.JoinQueue,
    'Event.MatchCreated': event.MatchCreated,
    'Inventory.Updated': inventory.Updated,
    'PlayerInventory.GetFormats': player_inventory.GetFormats,
    'PlayerInventory.GetPlayerCardsV3': player_inventory.GetPlayersCardsV3,
    'PlayerInventory.GetPlayerInventory': player_inventory.GetPlayerInventory,
    'PlayerInventory.GetRewardSchedule': player_inventory.GetRewardSchedule,
    'PostMatch.Update': post_match.Update,
    'Progression.GetPlayerProgress': progression.GetPlayerProgress,
    'TrackRewardTier.Updated': track_reward_tier.Updated,
    'Default': '',
}


def get_thread_class(thread_key):
    try:
        return THREAD_FACTORY[thread_key]
    except KeyError as err:
        print(err)
        raise KeyError
