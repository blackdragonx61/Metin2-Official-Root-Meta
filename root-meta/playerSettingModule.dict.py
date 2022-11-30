{'class': [],
 'func': [{'args': [], 'defaults': [], 'name': 'DefineSkillIndexDict'},
          {'args': ['name'], 'defaults': [], 'name': 'LoadGameData'},
          {'args': ['filename'], 'defaults': [], 'name': 'LoadGuildBuildingList'},
          {'args': [], 'defaults': [], 'name': 'OLD_SetNPC'},
          {'args': ['race', 'group', 'empire'], 'defaults': [0], 'name': 'RegisterSkill'},
          {'args': ['race', 'group', 'pos', 'num'], 'defaults': [], 'name': 'RegisterSkillAt'},
          {'args': ['race', 'name'], 'defaults': [], 'name': 'SetDoor'},
          {'args': ['mode', 'folder'], 'defaults': [], 'name': 'SetGeneralMotions'},
          {'args': ['race', 'name'], 'defaults': [], 'name': 'SetGuard'},
          {'args': ['race', 'name', 'grade'], 'defaults': [], 'name': 'SetGuildBuilding'},
          {'args': ['mode', 'folder'], 'defaults': [], 'name': 'SetIntroMotions'},
          {'args': ['race', 'name'], 'defaults': [], 'name': 'SetMovingNPC'},
          {'args': ['mode', 'folder'], 'defaults': [], 'name': 'SetNewGeneralMotions'},
          {'args': ['race', 'name'], 'defaults': [], 'name': 'SetOneNPC'},
          {'args': ['race'], 'defaults': [], 'name': 'SetWarp'},
          {'args': [], 'defaults': [], 'name': '__InitData'},
          {'args': [], 'defaults': [], 'name': '__LoadGameAssassin'},
          {'args': ['race', 'path'], 'defaults': [], 'name': '__LoadGameAssassinEx'},
          {'args': [], 'defaults': [], 'name': '__LoadGameEffect'},
          {'args': [], 'defaults': [], 'name': '__LoadGameEnemy'},
          {'args': [], 'defaults': [], 'name': '__LoadGameNPC'},
          {'args': [], 'defaults': [], 'name': '__LoadGameShaman'},
          {'args': ['race', 'path'], 'defaults': [], 'name': '__LoadGameShamanEx'},
          {'args': [], 'defaults': [], 'name': '__LoadGameSkill'},
          {'args': [], 'defaults': [], 'name': '__LoadGameSound'},
          {'args': [], 'defaults': [], 'name': '__LoadGameSura'},
          {'args': ['race', 'path'], 'defaults': [], 'name': '__LoadGameSuraEx'},
          {'args': [], 'defaults': [], 'name': '__LoadGameWarrior'},
          {'args': ['race', 'path'], 'defaults': [], 'name': '__LoadGameWarriorEx'},
          {'args': [], 'defaults': [], 'name': '__LoadGameWolfman'},
          {'args': ['race', 'path'], 'defaults': [], 'name': '__LoadGameWolfmanEx'},
          {'args': [], 'defaults': [], 'name': '__LoadRaceHeight'},
          {'args': [], 'defaults': [], 'name': '__LoadSetItemName'},
          {'args': [], 'defaults': [], 'name': '__LoadShopDeco'}],
 'import': ['skill', 'constInfo', 'localeInfo', 'item', '__builtin__', 'effect', 'emotion', 'app', 'chrmgrm2g', 'chr', 'guild', 'm2netm2g', 'playerm2g2'],
 'var': [{'name': 'ACTIVE_GUILD_SKILL_INDEX_LIST', 'type': 'tuple', 'value': (152, 153, 154, 155, 156, 157)},
         {'name': 'COMBO_INDEX_1', 'type': 'int', 'value': 0},
         {'name': 'COMBO_INDEX_2', 'type': 'int', 'value': 1},
         {'name': 'COMBO_INDEX_3', 'type': 'int', 'value': 2},
         {'name': 'COMBO_INDEX_4', 'type': 'int', 'value': 3},
         {'name': 'COMBO_INDEX_5', 'type': 'int', 'value': 4},
         {'name': 'COMBO_INDEX_6', 'type': 'int', 'value': 5},
         {'name': 'COMBO_TYPE_1', 'type': 'int', 'value': 0},
         {'name': 'COMBO_TYPE_2', 'type': 'int', 'value': 1},
         {'name': 'COMBO_TYPE_3', 'type': 'int', 'value': 2},
         {'name': 'FACE_IMAGE_DICT', 'type': 'dict', 'value': {0: 'd:/ymir work/ui/game/windows/face_warrior.sub', 1: 'd:/ymir work/ui/game/windows/face_assassin.sub', 2: 'd:/ymir work/ui/game/windows/face_sura.sub', 3: 'd:/ymir work/ui/game/windows/face_shaman.sub'}},
         {'name': 'GUILD_SKILL_BLESSARMOR', 'type': 'int', 'value': 153},
         {'name': 'GUILD_SKILL_DRAGONBLESS', 'type': 'int', 'value': 152},
         {'name': 'GUILD_SKILL_DRAGONBLOOD', 'type': 'int', 'value': 151},
         {'name': 'GUILD_SKILL_DRAGONWRATH', 'type': 'int', 'value': 155},
         {'name': 'GUILD_SKILL_MAGICUP', 'type': 'int', 'value': 156},
         {'name': 'GUILD_SKILL_SPPEDUP', 'type': 'int', 'value': 154},
         {'name': 'HORSE_SKILL_CHARGE', 'type': 'int', 'value': 172},
         {'name': 'HORSE_SKILL_SPLASH', 'type': 'int', 'value': 173},
         {'name': 'HORSE_SKILL_WILDATTACK', 'type': 'int', 'value': 171},
         {'name': 'JOB_ASSASSIN', 'type': 'int', 'value': 1},
         {'name': 'JOB_SHAMAN', 'type': 'int', 'value': 3},
         {'name': 'JOB_SURA', 'type': 'int', 'value': 2},
         {'name': 'JOB_WARRIOR', 'type': 'int', 'value': 0},
         {'name': 'JOB_WOLFMAN', 'type': 'int', 'value': 4},
         {'name': 'PASSIVE_GUILD_SKILL_INDEX_LIST', 'type': 'tuple', 'value': (151,)},
         {'name': 'RACE_ASSASSIN_M', 'type': 'int', 'value': 5},
         {'name': 'RACE_ASSASSIN_W', 'type': 'int', 'value': 1},
         {'name': 'RACE_SHAMAN_M', 'type': 'int', 'value': 7},
         {'name': 'RACE_SHAMAN_W', 'type': 'int', 'value': 3},
         {'name': 'RACE_SURA_M', 'type': 'int', 'value': 2},
         {'name': 'RACE_SURA_W', 'type': 'int', 'value': 6},
         {'name': 'RACE_WARRIOR_M', 'type': 'int', 'value': 0},
         {'name': 'RACE_WARRIOR_W', 'type': 'int', 'value': 4},
         {'name': 'RACE_WOLFMAN_M', 'type': 'int', 'value': 8},
         {'name': 'SKILL_INDEX_DICT',
          'type': 'dict',
          'value': {0: {1: (1, 2, 3, 4, 5, 6, 0, 0, 176, 137, 0, 138, 0, 139, 0), 2: (16, 17, 18, 19, 20, 21, 0, 0, 176, 137, 0, 138, 0, 139, 0), 'SUPPORT': (0, 0, 121, 134, 133, 129, 130, 131, 123, 124, 122, 132, 246)},
                    1: {1: (31, 32, 33, 34, 35, 36, 0, 0, 177, 137, 0, 138, 0, 139, 0, 140), 2: (46, 47, 48, 49, 50, 51, 0, 0, 178, 137, 0, 138, 0, 139, 0, 140), 'SUPPORT': (0, 0, 121, 134, 133, 129, 130, 131, 123, 124, 122, 132, 246)},
                    2: {1: (61, 62, 63, 64, 65, 66, 0, 0, 179, 137, 0, 138, 0, 139, 0), 2: (76, 77, 78, 79, 80, 81, 0, 0, 180, 137, 0, 138, 0, 139, 0), 'SUPPORT': (0, 0, 121, 134, 133, 129, 130, 131, 123, 124, 122, 132, 246)},
                    3: {1: (91, 92, 93, 94, 95, 96, 0, 0, 181, 137, 0, 138, 0, 139, 0), 2: (106, 107, 108, 109, 110, 111, 0, 0, 182, 137, 0, 138, 0, 139, 0), 'SUPPORT': (0, 0, 121, 134, 133, 129, 130, 131, 123, 124, 122, 132, 246)},
                    4: {1: (170, 171, 172, 173, 174, 175, 0, 0, 183, 137, 0, 138, 0, 139, 0), 2: (170, 171, 172, 173, 174, 175, 0, 0, 183, 137, 0, 138, 0, 139, 0), 'SUPPORT': (0, 0, 121, 134, 133, 129, 130, 131, 123, 124, 122, 132, 246)}}},
         {'name': '__doc__', 'type': 'NoneType', 'value': None},
         {'name': '__name__', 'type': 'str', 'value': 'playerSettingModule'},
         {'name': '__package__', 'type': 'NoneType', 'value': None},
         {'name': '__test__', 'type': 'dict', 'value': {}},
         {'name': 'isInitData', 'type': 'int', 'value': 1},
         {'name': 'loadGameDataDict', 'type': 'dict', 'value': {'ASSASSIN': 0, 'EFFECT': 0, 'ENEMY': 0, 'INIT': 0, 'NPC': 0, 'RACE_HEIGHT': None, 'SET_ITEM': None, 'SHAMAN': 0, 'SHOP': None, 'SKILL': 0, 'SOUND': 0, 'SURA': 0, 'WARRIOR': 0, 'WOLFMAN': 0}}]}
