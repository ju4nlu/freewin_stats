# freewin_stats

## Get player details

```
curl -X GET "https://open.faceit.com/data/v4/players?nickname=sombi" \
    -H "accept: application/json" \
    -H "Authorization: Bearer $FACEIT_DEV_API_KEY"
```

```
{
  "player_id": "5834ff8d-00e2-4d8d-a790-b684ae172fe2",
  "nickname": "sombi",
  "avatar": "https://assets.faceit-cdn.net/avatars/5834ff8d-00e2-4d8d-a790-b684ae172fe2_1560934561491.jpg",
  "country": "es",
  "cover_image": "https://assets.faceit-cdn.net/users_covers/5834ff8d-00e2-4d8d-a790-b684ae172fe2_1560934554472.jpg",
  "cover_featured_image": "",
  "infractions": {
    "last_infraction_date": "",
    "afk": 0,
    "leaver": 0,
    "qm_not_checkedin": 1,
    "qm_not_voted": 0
  },
  "platforms": {
    "steam": "STEAM_1:1:18020228"
  },
  "games": {
    "csgo": {
      "game_profile_id": "8f3ec7e3-469b-4b01-8c24-7fc07e63671b",
      "region": "EU",
      "regions": {
        "EU": {
          "selected_ladder_id": "cb94d2a1-da7c-488b-858c-b1080bdda2d1"
        }
      },
      "skill_level_label": "4",
      "game_player_id": "76561197996306185",
      "skill_level": 4,
      "faceit_elo": 1165,
      "game_player_name": "Drama Queen"
    }
  },
  "settings": {
    "language": "en"
  },
  "friends_ids": [
    "8eaf7401-27d4-4e4a-a7c7-96393de34e8d",
    "05e3b375-365b-4858-bcb4-af24b59fd2cd",
    "d48e954a-2f85-4a9d-a3c5-ce3842f99a4a",
    "e3dff11a-469c-4905-b03c-1443ff132916",
    "e6452859-42e0-4556-ba85-94594bc7ced0",
    "dbf09ed4-3848-459e-9ba3-13e3d60a0bfa",
    "ae358a06-3c3d-4843-babd-4c3cf32e1c94",
    "b3f109c7-7a9c-4bb0-bdaa-e9d95e97c901",
    "e8dc382d-e03e-48bb-88bd-787fa52304fb",
    "041c9f98-7d58-4c54-b1d2-a14b2fbd0bcc",
    "94e3b428-d0e3-4fe7-8e47-7d0af0abd050"
  ],
  "bans": [],
  "new_steam_id": "[U:1:36040457]",
  "steam_id_64": "76561197996306185",
  "steam_nickname": "s♦m _A_",
  "membership_type": "free",
  "memberships": [
    "free"
  ],
  "faceit_url": "https://www.faceit.com/{lang}/players/sombi"
}
```

## Get statistics of a player

```
curl -X GET "https://open.faceit.com/data/v4/players/5834ff8d-00e2-4d8d-a790-b684ae172fe2/stats/csgo" \
    -H "accept: application/json" \
    -H "Authorization: Bearer $FACEIT_DEV_API_KEY"
```

```
{
  "player_id": "5834ff8d-00e2-4d8d-a790-b684ae172fe2",
  "game_id": "csgo",
  "lifetime": {
    "Total Headshots %": "3859",
    "Win Rate %": "44",
    "Current Win Streak": "0",
    "Recent Results": [
      "0",
      "0",
      "1",
      "0",
      "0"
    ],
    "Longest Win Streak": "4",
    "Average K/D Ratio": "1.14",
    "Wins": "48",
    "Average Headshots %": "35",
    "Matches": "110",
    "K/D Ratio": "125.8"
  },
  "segments": [
    {
      "type": "Map",
      "mode": "5v5",
      "label": "de_mirage",
      "img_small": "https://cdn.faceit.com/static/stats_assets/csgo/maps/110x55/csgo-votable-maps-de_mirage-110x55.jpg",
      "img_regular": "https://cdn.faceit.com/static/stats_assets/csgo/maps/200x125/csgo-votable-maps-de_mirage-200x125.jpg",
      "stats": {
        "Wins": "12",
        "Quadro Kills": "2",
        "Total Headshots %": "986",
        "Average K/D Ratio": "1.09",
        "Average Headshots %": "35",
        "Matches": "28",
        "Headshots": "169",
        "Average Deaths": "17.43",
        "Average Quadro Kills": "0.07",
        "Average Triple Kills": "0.57",
        "K/D Ratio": "30.46",
        "Rounds": "733",
        "Deaths": "488",
        "Average K/R Ratio": "0.67",
        "K/R Ratio": "18.89",
        "Win Rate %": "43",
        "Penta Kills": "1",
        "MVPs": "55",
        "Average Assists": "3.18",
        "Average Kills": "17.61",
        "Average Penta Kills": "0.04",
        "Triple Kills": "16",
        "Headshots per Match": "6.04",
        "Average MVPs": "1.96",
        "Kills": "493",
        "Assists": "89"
      }
    },
    ...
  ]
}
```

## Get last 20 games of last month of a player

```
curl -X GET \
    "https://open.faceit.com/data/v4/players/5834ff8d-00e2-4d8d-a790-b684ae172fe2/history?game=csgo&offset=0&limit=20" \
    -H "accept: application/json" \
    -H "Authorization: Bearer $FACEIT_DEV_API_KEY"
```

```
{
  "items": [
    {
      "match_id": "1-a4d37b58-2c32-410a-b325-044e1df79eb3",
      "game_id": "csgo",
      "region": "EU",
      "match_type": "",
      "game_mode": "5v5",
      "max_players": 10,
      "teams_size": 5,
      "teams": {
        "faction2": {
          "team_id": "80c8c1b2-8a5c-46c2-8821-832bf0106a6e",
          "nickname": "team_uIVLucky",
          "avatar": "https://assets.faceit-cdn.net/avatars/80c8c1b2-8a5c-46c2-8821-832bf0106a6e_1582411198934.jpg",
          "type": "",
          "players": [
            {
              "player_id": "05e3b375-365b-4858-bcb4-af24b59fd2cd",
              "nickname": "XupinatoR",
              "avatar": "https://assets.faceit-cdn.net/avatars/05e3b375-365b-4858-bcb4-af24b59fd2cd_1550564501558.jpg",
              "skill_level": 5,
              "game_player_id": "76561198011374752",
              "game_player_name": "Miami Confirmed  ¯\\_(ツ)_/¯",
              "faceit_url": "https://www.faceit.com/{lang}/players/XupinatoR"
            },
            {
              "player_id": "5834ff8d-00e2-4d8d-a790-b684ae172fe2",
              "nickname": "sombi",
              "avatar": "https://assets.faceit-cdn.net/avatars/5834ff8d-00e2-4d8d-a790-b684ae172fe2_1560934561491.jpg",
              "skill_level": 4,
              "game_player_id": "76561197996306185",
              "game_player_name": "Drama Queen",
              "faceit_url": "https://www.faceit.com/{lang}/players/sombi"
            },
            {
              "player_id": "dbf09ed4-3848-459e-9ba3-13e3d60a0bfa",
              "nickname": "rAstab0i",
              "avatar": "",
              "skill_level": 3,
              "game_player_id": "76561198014288063",
              "game_player_name": "rAsti /34/",
              "faceit_url": "https://www.faceit.com/{lang}/players/rAstab0i"
            },
            {
              "player_id": "e8dc382d-e03e-48bb-88bd-787fa52304fb",
              "nickname": "m3ndo-",
              "avatar": "https://assets.faceit-cdn.net/avatars/e8dc382d-e03e-48bb-88bd-787fa52304fb_1551214111483.jpg",
              "skill_level": 5,
              "game_player_id": "76561197963371304",
              "game_player_name": "m3ndo",
              "faceit_url": "https://www.faceit.com/{lang}/players/m3ndo-"
            },
            {
              "player_id": "80c8c1b2-8a5c-46c2-8821-832bf0106a6e",
              "nickname": "uIVLucky",
              "avatar": "https://assets.faceit-cdn.net/avatars/80c8c1b2-8a5c-46c2-8821-832bf0106a6e_1582411198934.jpg",
              "skill_level": 4,
              "game_player_id": "76561198314802688",
              "game_player_name": "That I Would Be Good",
              "faceit_url": "https://www.faceit.com/{lang}/players/uIVLucky"
            }
          ]
        },
        "faction1": {
          "team_id": "02fa782f-2463-4a89-b5ae-45769e378203",
          "nickname": "team_STEAM_1:1:13",
          "avatar": "https://assets.faceit-cdn.net/avatars/02fa782f-2463-4a89-b5ae-45769e378203_1550646330350.jpg",
          "type": "",
          "players": [
            {
              "player_id": "5a7561e4-c45f-45e3-8f49-890919707c2e",
              "nickname": "iNSPY",
              "avatar": "https://assets.faceit-cdn.net/avatars/5a7561e4-c45f-45e3-8f49-890919707c2e_1582224708072.jpg",
              "skill_level": 3,
              "game_player_id": "76561198371665507",
              "game_player_name": "iNSPY",
              "faceit_url": "https://www.faceit.com/{lang}/players/iNSPY"
            },
            {
              "player_id": "a03fbfa5-a9ee-47e0-92ba-55c71a9321fd",
              "nickname": "Zeeyka",
              "avatar": "https://assets.faceit-cdn.net/avatars/a03fbfa5-a9ee-47e0-92ba-55c71a9321fd_1582638034711.jpg",
              "skill_level": 2,
              "game_player_id": "76561198156312589",
              "game_player_name": "✪ Zeeyka",
              "faceit_url": "https://www.faceit.com/{lang}/players/Zeeyka"
            },
            {
              "player_id": "f6af5962-c484-45ad-ba36-510661714f01",
              "nickname": "Phooncassis",
              "avatar": "https://assets.faceit-cdn.net/avatars/f6af5962-c484-45ad-ba36-510661714f01_1578579607950.jpg",
              "skill_level": 4,
              "game_player_id": "76561198795515700",
              "game_player_name": "76561198795515700",
              "faceit_url": "https://www.faceit.com/{lang}/players/Phooncassis"
            },
            {
              "player_id": "f82e072d-3905-4737-859a-56520bbf8257",
              "nickname": "Awpornn",
              "avatar": "https://assets.faceit-cdn.net/avatars/f82e072d-3905-4737-859a-56520bbf8257_1580594484744.jpg",
              "skill_level": 5,
              "game_player_id": "76561198884170856",
              "game_player_name": "satine",
              "faceit_url": "https://www.faceit.com/{lang}/players/Awpornn"
            },
            {
              "player_id": "02fa782f-2463-4a89-b5ae-45769e378203",
              "nickname": "STEAM_1:1:13",
              "avatar": "https://assets.faceit-cdn.net/avatars/02fa782f-2463-4a89-b5ae-45769e378203_1550646330350.jpg",
              "skill_level": 4,
              "game_player_id": "76561197986638743",
              "game_player_name": "shchelβan",
              "faceit_url": "https://www.faceit.com/{lang}/players/STEAM_1%3A1%3A13"
            }
          ]
        }
      },
      "playing_players": [
        "5a7561e4-c45f-45e3-8f49-890919707c2e",
        "a03fbfa5-a9ee-47e0-92ba-55c71a9321fd",
        "f6af5962-c484-45ad-ba36-510661714f01",
        "f82e072d-3905-4737-859a-56520bbf8257",
        "02fa782f-2463-4a89-b5ae-45769e378203",
        "05e3b375-365b-4858-bcb4-af24b59fd2cd",
        "5834ff8d-00e2-4d8d-a790-b684ae172fe2",
        "dbf09ed4-3848-459e-9ba3-13e3d60a0bfa",
        "e8dc382d-e03e-48bb-88bd-787fa52304fb",
        "80c8c1b2-8a5c-46c2-8821-832bf0106a6e"
      ],
      "competition_id": "42e160fc-2651-4fa5-9a9b-829199e27adb",
      "competition_name": "CS:GO 5v5",
      "competition_type": "matchmaking",
      "organizer_id": "faceit",
      "status": "finished",
      "started_at": 1582825363,
      "finished_at": 1582827639,
      "results": {
        "winner": "faction1",
        "score": {
          "faction1": 1,
          "faction2": 0
        }
      },
      "faceit_url": "https://www.faceit.com/{lang}/csgo/room/1-a4d37b58-2c32-410a-b325-044e1df79eb3"
    },
    ...
   }
  ]
}
```