{'class': [{'class': [],
            'func': [{'args': ['self', 'pid', 'name', 'mapIdx', 'channel'], 'defaults': [], 'name': 'AddPartyMember'},
                     {'args': ['self', 'distributionMode'], 'defaults': [], 'name': 'ChangePartyParameter'},
                     {'args': ['self'], 'defaults': [], 'name': 'Destroy'},
                     {'args': ['self'], 'defaults': [], 'name': 'DestroyPartyMemberInfoBoard'},
                     {'args': ['self'], 'defaults': [], 'name': 'ExitParty'},
                     {'args': ['self', 'pid', 'vid', 'mapIdx', 'channel'], 'defaults': [], 'name': 'LinkPartyMember'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnTogglePartyMenu'},
                     {'args': ['self'], 'defaults': [], 'name': 'PartyHealReady'},
                     {'args': ['self', 'pid'], 'defaults': [], 'name': 'RemovePartyMember'},
                     {'args': ['self'], 'defaults': [], 'name': 'UnlinkAllPartyMember'},
                     {'args': ['self', 'pid'], 'defaults': [], 'name': 'UnlinkPartyMember'},
                     {'args': ['self', 'pid'], 'defaults': [], 'name': 'UpdatePartyMemberInfo'},
                     {'args': ['self'], 'defaults': [], 'name': '__ArrangePartyMemberInfoBoard'},
                     {'args': ['self'], 'defaults': [], 'name': '__CreatePartyMenu'},
                     {'args': ['self'], 'defaults': [], 'name': '__CreatePartyMenuButton'},
                     {'args': ['self', 'pid'], 'defaults': [], 'name': '__FindPartyMemberInfoBoardByPID'},
                     {'args': ['self', 'vid'], 'defaults': [], 'name': '__FindPartyMemberInfoBoardByVID'},
                     {'args': ['self'], 'defaults': [], 'name': '__del__'},
                     {'args': ['self'], 'defaults': [], 'name': '__init__'}],
            'import': [],
            'var': [{'name': '__doc__', 'type': 'NoneType', 'value': None}, {'name': '__module__', 'type': 'str', 'value': 'uiParty'}, {'name': '__qualname__', 'type': 'str', 'value': 'PartyWindow'}]},
           {'class': [],
            'func': [{'args': ['self', 'distributionMode'], 'defaults': [], 'name': 'ChangePartyParameter'},
                     {'args': ['self'], 'defaults': [], 'name': 'Destroy'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnClickEXPDistributeParity'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnClickEXPLevel'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnPartyUseSkill'},
                     {'args': ['self'], 'defaults': [], 'name': 'PartyHealReady'},
                     {'args': ['self'], 'defaults': [], 'name': 'ShowLeaderButton'},
                     {'args': ['self'], 'defaults': [], 'name': 'ShowMemberButton'},
                     {'args': ['self'], 'defaults': [], 'name': '__ArrangeButtons'},
                     {'args': ['self'], 'defaults': [], 'name': '__ClearShowingButtons'},
                     {'args': ['self'], 'defaults': [], 'name': '__CreateButtons'},
                     {'args': ['self'], 'defaults': [], 'name': '__CreateModeButtons'},
                     {'args': ['self', 'name'], 'defaults': [], 'name': '__HideButton'},
                     {'args': ['self', 'mode'], 'defaults': [], 'name': '__SetModeButton'},
                     {'args': ['self', 'name'], 'defaults': [], 'name': '__ShowButton'},
                     {'args': ['self'], 'defaults': [], 'name': '__UpAllModeButtons'},
                     {'args': ['self'], 'defaults': [], 'name': '__del__'},
                     {'args': ['self'], 'defaults': [], 'name': '__init__'}],
            'import': [],
            'var': [{'name': 'BUTTON_NAME', 'type': 'tuple', 'value': ('Mindent \xfajratermelni', 'Csoport felbont\xe1s', 'Csoport elhagy\xe1sa')},
                    {'name': '__doc__', 'type': 'NoneType', 'value': None},
                    {'name': '__module__', 'type': 'str', 'value': 'uiParty'},
                    {'name': '__qualname__', 'type': 'str', 'value': 'PartyMenu'}]},
           {'class': [{'class': [],
                       'func': [{'args': ['self', 'text', 'x', 'y'], 'defaults': [], 'name': 'SetText'}, {'args': ['self'], 'defaults': [], 'name': '__del__'}, {'args': ['self'], 'defaults': [], 'name': '__init__'}],
                       'import': [],
                       'var': [{'name': '__doc__', 'type': 'NoneType', 'value': None}, {'name': '__module__', 'type': 'str', 'value': 'uiParty'}, {'name': '__qualname__', 'type': 'str', 'value': 'PartyMemberInfoBoard.TextToolTip'}]}],
            'func': [{'args': ['self'], 'defaults': [], 'name': 'Destroy'},
                     {'args': ['self'], 'defaults': [], 'name': 'GetCharacterName'},
                     {'args': ['self'], 'defaults': [], 'name': 'GetCharacterPID'},
                     {'args': ['self'], 'defaults': [], 'name': 'GetCharacterVID'},
                     {'args': ['self'], 'defaults': [], 'name': 'Link'},
                     {'args': ['self', 'index'], 'defaults': [], 'name': 'OnAffectOverIn'},
                     {'args': ['self', 'index'], 'defaults': [], 'name': 'OnAffectOverOut'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnExpel'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnMouseLeftButtonDown'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnMouseLeftButtonUp'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnMouseOverIn'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnMouseOverOut'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnMouseRightButtonDown'},
                     {'args': ['self', 'state'], 'defaults': [], 'name': 'OnSelectState'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnWarp'},
                     {'args': ['self', 'affectSlotIndex', 'affectValue'], 'defaults': [], 'name': 'SetAffect'},
                     {'args': ['self', 'hpPercentage'], 'defaults': [], 'name': 'SetCharacterHP'},
                     {'args': ['self', 'name'], 'defaults': [], 'name': 'SetCharacterName'},
                     {'args': ['self', 'pid'], 'defaults': [], 'name': 'SetCharacterPID'},
                     {'args': ['self', 'state'], 'defaults': [], 'name': 'SetCharacterState'},
                     {'args': ['self', 'vid'], 'defaults': [], 'name': 'SetCharacterVID'},
                     {'args': ['self', 'MapName'], 'defaults': [], 'name': 'SetCurrentMapName'},
                     {'args': ['self'], 'defaults': [], 'name': 'Unlink'},
                     {'args': ['self', 'x', 'y', 'state'], 'defaults': [], 'name': '__AppendStateButton'},
                     {'args': ['self'], 'defaults': [], 'name': '__CreateAffectToolTip'},
                     {'args': ['self'], 'defaults': [], 'name': '__CreateStateButton'},
                     {'args': ['self', 'img'], 'defaults': [], 'name': '__GetAffectNumber'},
                     {'args': ['self'], 'defaults': [], 'name': '__GetPartySkillLevel'},
                     {'args': ['self'], 'defaults': [], 'name': '__HideAllAffects'},
                     {'args': ['self'], 'defaults': [], 'name': '__HideStateButton'},
                     {'args': ['self'], 'defaults': [], 'name': '__LoadBoard'},
                     {'args': ['self'], 'defaults': [], 'name': '__SetAffectsMouseEvent'},
                     {'args': ['self'], 'defaults': [], 'name': '__ShowStateButton'},
                     {'args': ['self'], 'defaults': [], 'name': '__del__'},
                     {'args': ['self'], 'defaults': [], 'name': '__init__'}],
            'import': [],
            'var': [{'name': 'AFFECT_STRING_DICT',
                     'type': 'dict',
                     'value': {0: <cyfunction SA.<locals>.f at 0x0782D138>,
                               1: <cyfunction SA.<locals>.f at 0x07797FA8>,
                               2: <cyfunction SA.<locals>.f at 0x0782D1E8>,
                               3: <cyfunction SA.<locals>.f at 0x0782D088>,
                               4: <cyfunction SA.<locals>.f at 0x0782D190>,
                               5: <cyfunction SA.<locals>.f at 0x0782D030>,
                               6: <cyfunction SA.<locals>.f at 0x0782D0E0>,
                               7: <cyfunction SNA.<locals>.f at 0x0782D240>,
                               8: <cyfunction SNA.<locals>.f at 0x0782D298>}},
                    {'name': 'BOARD_COLOR', 'type': 'int', 'value': 2130706432},
                    {'name': 'BOARD_WIDTH', 'type': 'int', 'value': 106},
                    {'name': 'GAUGE_OUT_LINE_COLOR', 'type': 'int', 'value': 1291845631},
                    {'name': 'LINK_COLOR', 'type': 'int', 'value': -4079167},
                    {'name': 'MEMBER_BUTTON_EXPEL', 'type': 'int', 'value': 12},
                    {'name': 'MEMBER_BUTTON_IMAGE_FILE_NAME_DICT',
                     'type': 'dict',
                     'value': {1: 'party_state_leader', 2: 'party_state_attacker', 3: 'party_state_tanker', 4: 'party_state_buffer', 5: 'party_state_skill_master', 6: 'party_state_berserker', 7: 'party_state_defender', 10: 'party_state_normal', 11: 'party_skill_warp', 12: 'party_expel'}},
                    {'name': 'MEMBER_BUTTON_NORMAL', 'type': 'int', 'value': 10},
                    {'name': 'MEMBER_BUTTON_PATH', 'type': 'str', 'value': 'd:/ymir work/ui/game/windows/'},
                    {'name': 'MEMBER_BUTTON_WARP', 'type': 'int', 'value': 11},
                    {'name': 'PARTY_AFFECT_ATTACKER', 'type': 'int', 'value': 1},
                    {'name': 'PARTY_AFFECT_BERSERKER', 'type': 'int', 'value': 5},
                    {'name': 'PARTY_AFFECT_BUFFER', 'type': 'int', 'value': 3},
                    {'name': 'PARTY_AFFECT_DEFENDER', 'type': 'int', 'value': 6},
                    {'name': 'PARTY_AFFECT_EXPERIENCE', 'type': 'int', 'value': 0},
                    {'name': 'PARTY_AFFECT_INCREASE_AREA_150', 'type': 'int', 'value': 7},
                    {'name': 'PARTY_AFFECT_INCREASE_AREA_200', 'type': 'int', 'value': 8},
                    {'name': 'PARTY_AFFECT_SKILL_MASTER', 'type': 'int', 'value': 4},
                    {'name': 'PARTY_AFFECT_TANKER', 'type': 'int', 'value': 2},
                    {'name': 'PARTY_SKILL_HEAL', 'type': 'int', 'value': 1},
                    {'name': 'PARTY_SKILL_WARP', 'type': 'int', 'value': 2},
                    {'name': 'STATE_NAME_DICT', 'type': 'dict', 'value': {2: 'T\xe1mad\xf3nak kinevez.', 3: 'T\xf5rharcos be\xe1ll\xedt\xe1s.', 4: 'Blokkol\xf3nak kinevez.', 5: 'K\xe9szs\xe9g mesternek kinevez.', 6: 'D\xfch\xf6ng\xf5nek kinevez.', 7: 'V\xe9d\xf5nek kinevez.'}},
                    {'name': 'UNLINK_COLOR', 'type': 'int', 'value': -8421505},
                    {'name': '__doc__', 'type': 'NoneType', 'value': None},
                    {'name': '__module__', 'type': 'str', 'value': 'uiParty'},
                    {'name': '__qualname__', 'type': 'str', 'value': 'PartyMemberInfoBoard'}]}],
 'func': [],
 'import': ['constInfo', 'grp', 'uiToolTip', '__builtin__', 'app', 'm2netm2g', 'playerm2g2', 'ui', 'mouseModule', 'uiScriptLocale', 'localeInfo'],
 'var': [{'name': '__doc__', 'type': 'NoneType', 'value': None}, {'name': '__name__', 'type': 'str', 'value': 'uiParty'}, {'name': '__package__', 'type': 'NoneType', 'value': None}, {'name': '__test__', 'type': 'dict', 'value': {}}]}
