{'class': [{'class': [],
            'func': [{'args': ['self'], 'defaults': [], 'name': 'ClearItem'},
                     {'args': ['self', 'line'], 'defaults': [], 'name': 'GetState'},
                     {'args': ['self', 'number', 'text', 'state', 'state2'], 'defaults': [0, 0], 'name': 'InsertItem'},
                     {'args': ['self', 'event_type', 'arg'], 'defaults': [], 'name': 'StateImageEventProgress'},
                     {'args': ['self'], 'defaults': [], 'name': '_LocateItem'},
                     {'args': ['self', 'layer'], 'defaults': ['UI'], 'name': '__init__'}],
            'import': [],
            'var': [{'name': 'STATE_IMAGE_PATH', 'type': 'tuple', 'value': ('', 'locale/hu/ui/login/choise_new.tga', 'locale/hu/ui/login/choise_special.tga', 'locale/hu/ui/login/choise_close.tga')},
                    {'name': 'STATE_IMAGE_TOOLTIP', 'type': 'tuple', 'value': ('', '\xdaJ', 'SPECI\xc1LIS', 'LEZ\xc1RT')},
                    {'name': '__doc__', 'type': 'NoneType', 'value': None},
                    {'name': '__module__', 'type': 'str', 'value': 'introLogin'},
                    {'name': '__qualname__', 'type': 'str', 'value': 'ServerListBox'}]},
           {'class': [],
            'func': [{'args': ['self'], 'defaults': [], 'name': 'AutoSelectChannel'},
                     {'args': ['self', 'quiz'], 'defaults': [], 'name': 'BINARY_OnRunupMatrixQuiz'},
                     {'args': ['self'], 'defaults': [], 'name': 'Close'},
                     {'args': ['self', 'id', 'pwd'], 'defaults': [], 'name': 'Connect'},
                     {'args': ['self'], 'defaults': [], 'name': 'EmptyFunc'},
                     {'args': ['self', 'addrKey', 'state'], 'defaults': [], 'name': 'NotifyChannelState'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnConnectFailure'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnEndCountDown'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnExit'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnHandShake'},
                     {'args': ['self', 'error'], 'defaults': [], 'name': 'OnLoginFailure'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnLoginStart'},
                     {'args': ['self', 'row1', 'row2', 'row3', 'row4', 'col1', 'col2', 'col3', 'col4'], 'defaults': [], 'name': 'OnMatrixCard'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnPressExitKey'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnUpdate'},
                     {'args': ['self'], 'defaults': [], 'name': 'Open'},
                     {'args': ['self', 'msg', 'event', 'ButtonName'], 'defaults': [0, 'Megszak\xedt'], 'name': 'PopupDisplayMessage'},
                     {'args': ['self', 'msg', 'func'], 'defaults': [0], 'name': 'PopupNotifyMessage'},
                     {'args': ['self'], 'defaults': [], 'name': 'SameLogin_OpenUI'},
                     {'args': ['self'], 'defaults': [], 'name': 'SetIDEditLineFocus'},
                     {'args': ['self'], 'defaults': [], 'name': 'SetPasswordEditLineFocus'},
                     {'args': ['self', 'channelID'], 'defaults': [], 'name': '__ChannelIDToChannelIndex'},
                     {'args': ['self'], 'defaults': [], 'name': '__DisconnectAndInputID'},
                     {'args': ['self'], 'defaults': [], 'name': '__DisconnectAndInputMatrix'},
                     {'args': ['self'], 'defaults': [], 'name': '__DisconnectAndInputPassword'},
                     {'args': ['self'], 'defaults': [], 'name': '__ExitGame'},
                     {'args': ['self'], 'defaults': [], 'name': '__GetChannelID'},
                     {'args': ['self', 'regionID', 'selServerID', 'selChannelID'], 'defaults': [], 'name': '__GetChannelName'},
                     {'args': ['self'], 'defaults': [], 'name': '__GetRegionID'},
                     {'args': ['self'], 'defaults': [], 'name': '__GetServerID'},
                     {'args': ['self'], 'defaults': [], 'name': '__LoadChannelInfo'},
                     {'args': ['self', 'loginInfoFileName'], 'defaults': [], 'name': '__LoadLoginInfo'},
                     {'args': ['self', 'fileName'], 'defaults': [], 'name': '__LoadScript'},
                     {'args': ['self'], 'defaults': [], 'name': '__OnAcceptMatrixCardData'},
                     {'args': ['self'], 'defaults': [], 'name': '__OnCancelMatrixCardData'},
                     {'args': ['self'], 'defaults': [], 'name': '__OnClickExitButton'},
                     {'args': ['self'], 'defaults': [], 'name': '__OnClickExitServerButton'},
                     {'args': ['self'], 'defaults': [], 'name': '__OnClickLoginButton'},
                     {'args': ['self'], 'defaults': [], 'name': '__OnClickMatrixAnswerCancel'},
                     {'args': ['self'], 'defaults': [], 'name': '__OnClickMatrixAnswerOK'},
                     {'args': ['self'], 'defaults': [], 'name': '__OnClickSelectConnectButton'},
                     {'args': ['self'], 'defaults': [], 'name': '__OnClickSelectRegionButton'},
                     {'args': ['self'], 'defaults': [], 'name': '__OnClickSelectServerButton'},
                     {'args': ['self'], 'defaults': [], 'name': '__OnCloseInputDialog'},
                     {'args': ['self'], 'defaults': [], 'name': '__OnSelectRegionGroup'},
                     {'args': ['self'], 'defaults': [], 'name': '__OnSelectServer'},
                     {'args': ['self'], 'defaults': [], 'name': '__OnSelectSettlementArea'},
                     {'args': ['self'], 'defaults': [], 'name': '__OpenLoginBoard'},
                     {'args': ['self'], 'defaults': [], 'name': '__OpenServerBoard'},
                     {'args': ['self'], 'defaults': [], 'name': '__RefreshServerList'},
                     {'args': ['self'], 'defaults': [], 'name': '__RefreshServerStateList'},
                     {'args': ['self'], 'defaults': [], 'name': '__RequestServerStateList'},
                     {'args': ['self'], 'defaults': [], 'name': '__SaveChannelInfo'},
                     {'args': ['self', 'key'], 'defaults': [], 'name': '__ServerBoard_OnKeyUp'},
                     {'args': ['self', 'regionID', 'targetServerID'], 'defaults': [], 'name': '__ServerIDToServerIndex'},
                     {'args': ['self', 'name'], 'defaults': [], 'name': '__SetServerInfo'},
                     {'args': ['self'], 'defaults': [], 'name': '__VirtualKeyboard_PressBackspace'},
                     {'args': ['self', 'code'], 'defaults': [], 'name': '__VirtualKeyboard_PressKey'},
                     {'args': ['self'], 'defaults': [], 'name': '__VirtualKeyboard_PressReturn'},
                     {'args': ['self'], 'defaults': [], 'name': '__VirtualKeyboard_SetAlphabetMode'},
                     {'args': ['self', 'keyCodes'], 'defaults': [], 'name': '__VirtualKeyboard_SetKeys'},
                     {'args': ['self'], 'defaults': [], 'name': '__VirtualKeyboard_SetLowerMode'},
                     {'args': ['self'], 'defaults': [], 'name': '__VirtualKeyboard_SetNumberMode'},
                     {'args': ['self'], 'defaults': [], 'name': '__VirtualKeyboard_SetSymbolMode'},
                     {'args': ['self'], 'defaults': [], 'name': '__VirtualKeyboard_SetUpperMode'},
                     {'args': ['self'], 'defaults': [], 'name': '__del__'},
                     {'args': ['self', 'stream'], 'defaults': [], 'name': '__init__'}],
            'import': [],
            'var': [{'name': 'IS_TEST', 'type': 'int', 'value': 0}, {'name': '__doc__', 'type': 'NoneType', 'value': None}, {'name': '__module__', 'type': 'str', 'value': 'introLogin'}, {'name': '__qualname__', 'type': 'str', 'value': 'LoginWindow'}]},
           {'class': [],
            'func': [{'args': ['self'], 'defaults': [], 'name': 'Close'},
                     {'args': ['self'], 'defaults': [], 'name': 'Destroy'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnPressExitKey'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnUpdate'},
                     {'args': ['self', 'waitTime'], 'defaults': [], 'name': 'Open'},
                     {'args': ['self', 'event'], 'defaults': [], 'name': 'SAFE_SetExitEvent'},
                     {'args': ['self', 'event'], 'defaults': [], 'name': 'SAFE_SetTimeOverEvent'},
                     {'args': ['self', 'waitTime'], 'defaults': [], 'name': 'SetCountDownMessage'},
                     {'args': ['self', 'text'], 'defaults': [], 'name': 'SetText'},
                     {'args': ['self'], 'defaults': [], 'name': '__LoadDialog'},
                     {'args': ['self'], 'defaults': [], 'name': '__del__'},
                     {'args': ['self'], 'defaults': [], 'name': '__init__'}],
            'import': [],
            'var': [{'name': '__doc__', 'type': 'NoneType', 'value': None}, {'name': '__module__', 'type': 'str', 'value': 'introLogin'}, {'name': '__qualname__', 'type': 'str', 'value': 'ConnectingDialog'}]},
           {'class': [],
            'func': [{'args': ['self'], 'defaults': [], 'name': 'ClearItem'}, {'args': ['self', 'number', 'text', 'text2', 'textColor'], 'defaults': [0], 'name': 'InsertItem'}, {'args': ['self', 'layer'], 'defaults': ['UI'], 'name': '__init__'}],
            'import': [],
            'var': [{'name': 'TEMPORARY_PLACE', 'type': 'int', 'value': 3}, {'name': '__doc__', 'type': 'NoneType', 'value': None}, {'name': '__module__', 'type': 'str', 'value': 'introLogin'}, {'name': '__qualname__', 'type': 'str', 'value': 'ChannelListBox'}]}],
 'func': [{'args': [], 'defaults': [], 'name': 'GetLoginDelay'}, {'args': [], 'defaults': [], 'name': 'IsFullBackImage'}, {'args': [], 'defaults': [], 'name': 'IsLoginDelay'}, {'args': [], 'defaults': [], 'name': 'IsRunupMatrixAuth'}, {'args': ['src'], 'defaults': [], 'name': 'Suffle'}],
 'import': ['uiWebLinkedBanner', 'app', 'dbg', 'm2netm2g', 'ime', 'grp', 'uiToolTip', 'systemSetting', 'uiScriptLocale', 'ui', 'localeInfo', 'uiCommon', 'snd', 'serverCommandParser', '__builtin__', 'uiWeb', 'serverInfo', 'wndMgr', 'constInfo', 'ServerStateChecker', 'musicInfo', 'time'],
 'var': [{'name': 'FULL_BACK_IMAGE', 'type': 'bool', 'value': False},
         {'name': 'LOGIN_DELAY_SEC', 'type': 'float', 'value': 0.0},
         {'name': 'PASSPOD_MSG_DICT', 'type': 'dict', 'value': {}},
         {'name': 'RUNUP_MATRIX_AUTH', 'type': 'bool', 'value': False},
         {'name': 'SKIP_LOGIN_PHASE', 'type': 'bool', 'value': False},
         {'name': 'SKIP_LOGIN_PHASE_SUPPORT_CHANNEL', 'type': 'bool', 'value': False},
         {'name': 'VIRTUAL_KEYBOARD_NUM_KEYS', 'type': 'int', 'value': 46},
         {'name': 'VIRTUAL_KEYBOARD_RAND_KEY', 'type': 'bool', 'value': True},
         {'name': '__doc__', 'type': 'NoneType', 'value': None},
         {'name': '__name__', 'type': 'str', 'value': 'introLogin'},
         {'name': '__package__', 'type': 'NoneType', 'value': None},
         {'name': '__test__', 'type': 'dict', 'value': {}}]}
