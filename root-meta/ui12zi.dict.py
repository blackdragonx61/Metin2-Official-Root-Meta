{'class': [{'class': [],
            'func': [{'args': ['self'], 'defaults': [], 'name': 'Close'},
                     {'args': ['self'], 'defaults': [], 'name': 'Destroy'},
                     {'args': ['self'], 'defaults': [], 'name': 'NextMission'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnUpdate'},
                     {'args': ['self'], 'defaults': [], 'name': 'Open'},
                     {'args': ['self'], 'defaults': [], 'name': 'PressJumpButton'},
                     {'args': ['self', 'currentFloor', 'jumpCount', 'limitTime', 'elapseTime'], 'defaults': [], 'name': 'Refresh12ziTimer'},
                     {'args': ['self'], 'defaults': [], 'name': 'Show12ziJumpButton'},
                     {'args': ['self', 'time'], 'defaults': [], 'name': 'StartCoolTime'},
                     {'args': ['self'], 'defaults': [], 'name': '__LoadWindow'},
                     {'args': ['self'], 'defaults': [], 'name': '__del__'},
                     {'args': ['self'], 'defaults': [], 'name': '__init__'}],
            'import': [],
            'var': [{'name': '__doc__', 'type': 'NoneType', 'value': None}, {'name': '__module__', 'type': 'str', 'value': 'ui12zi'}, {'name': '__qualname__', 'type': 'str', 'value': 'FloorLimitTimeWindow'}]},
           {'class': [],
            'func': [{'args': ['self'], 'defaults': [], 'name': 'Close'},
                     {'args': ['self'], 'defaults': [], 'name': 'Destroy'},
                     {'args': ['self', 'value'], 'defaults': [], 'name': 'NextBeadUpdateTime'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnUpdate'},
                     {'args': ['self', 'value'], 'defaults': [], 'name': 'SetBeadCount'},
                     {'args': ['self'], 'defaults': [], 'name': '__LoadWindow'},
                     {'args': ['self'], 'defaults': [], 'name': '__del__'},
                     {'args': ['self'], 'defaults': [], 'name': '__init__'}],
            'import': [],
            'var': [{'name': '__doc__', 'type': 'NoneType', 'value': None}, {'name': '__module__', 'type': 'str', 'value': 'ui12zi'}, {'name': '__qualname__', 'type': 'str', 'value': 'BeadWindow'}]},
           {'class': [],
            'func': [{'args': ['self'], 'defaults': [], 'name': 'GetTextSize'},
                     {'args': ['self', 'text'], 'defaults': [], 'name': 'SetText'},
                     {'args': ['self', 'TextColor'], 'defaults': [], 'name': 'SetTextColor'},
                     {'args': ['self', 'PosX', 'PosY'], 'defaults': [], 'name': 'SetTooltipPosition'},
                     {'args': ['self'], 'defaults': [], 'name': '__del__'},
                     {'args': ['self'], 'defaults': [], 'name': '__init__'}],
            'import': [],
            'var': [{'name': '__doc__', 'type': 'NoneType', 'value': None}, {'name': '__module__', 'type': 'str', 'value': 'ui12zi'}, {'name': '__qualname__', 'type': 'str', 'value': 'MapTextToolTip'}]},
           {'class': [],
            'func': [{'args': ['self'], 'defaults': [], 'name': 'ButtonToolTipProgress'},
                     {'args': ['self'], 'defaults': [], 'name': 'Close'},
                     {'args': ['self'], 'defaults': [], 'name': 'Destroy'},
                     {'args': ['self', 'event_type', 'arg'], 'defaults': [], 'name': 'EventProgress'},
                     {'args': ['self', 'event_type', 'arg'], 'defaults': [], 'name': 'ItemToolTipEvent'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnCloseQuestionDialog'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnPressEscapeKey'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnUpdate'},
                     {'args': ['self', 'yellowmark', 'greenmark', 'yellowreward', 'greenreward', 'goldreward'], 'defaults': [], 'name': 'Open'},
                     {'args': ['self', 'arg'], 'defaults': [], 'name': 'OverInToolTipButton'},
                     {'args': ['self'], 'defaults': [], 'name': 'OverOutToolTipButton'},
                     {'args': ['self', 'type'], 'defaults': [], 'name': 'PressButton'},
                     {'args': ['self', 'value'], 'defaults': [], 'name': 'PressCheckButton'},
                     {'args': ['self', 'value'], 'defaults': [], 'name': 'SendClear'},
                     {'args': ['self', 'tooltipItem'], 'defaults': [], 'name': 'SetItemToolTip'},
                     {'args': ['self'], 'defaults': [], 'name': '__LoadWindow'},
                     {'args': ['self'], 'defaults': [], 'name': '__del__'},
                     {'args': ['self'], 'defaults': [], 'name': '__init__'}],
            'import': [],
            'var': [{'name': 'COLUMN_ITEM_LIST', 'type': 'tuple', 'value': (33001, 33002, 33003, 33004, 33005, 33006, 33007, 33008, 33009, 33010, 33011, 33012)},
                    {'name': 'COLUMN_SIZE', 'type': 'int', 'value': 12},
                    {'name': 'ROW_ITEM_LIST', 'type': 'tuple', 'value': (33013, 33014, 33015, 33016, 33017, 33018, 33019, 33020, 33021, 33022)},
                    {'name': 'ROW_SIZE', 'type': 'int', 'value': 10},
                    {'name': 'WEEKLY_COLUMN_LIST', 'type': 'tuple', 'value': ('H\xe9tf\xf5', 'Kedd', 'Szerda', 'Cs\xfct\xf6rt\xf6k', 'P\xe9ntek', 'Szombat/Vas\xe1rnap')},
                    {'name': 'WEEKLY_ROW_LIST', 'type': 'tuple', 'value': ('H\xe9tf\xf5', 'Kedd', 'Szerda', 'Cs\xfct\xf6rt\xf6k', 'P\xe9ntek', 'Szombat')},
                    {'name': '__doc__', 'type': 'NoneType', 'value': None},
                    {'name': '__module__', 'type': 'str', 'value': 'ui12zi'},
                    {'name': '__qualname__', 'type': 'str', 'value': 'Reward12ziWindow'}]}],
 'func': [],
 'import': ['app', 'playerm2g2', 'constInfo', 'grp', 'uiToolTip', 'systemSetting', 'chr', 'mouseModule', 'localeInfo', 'uiCommon', '__builtin__', 'background', 'wndMgr', 'm2netm2g', 'ui'],
 'var': [{'name': '__doc__', 'type': 'NoneType', 'value': None}, {'name': '__name__', 'type': 'str', 'value': 'ui12zi'}, {'name': '__package__', 'type': 'NoneType', 'value': None}, {'name': '__test__', 'type': 'dict', 'value': {}}]}
