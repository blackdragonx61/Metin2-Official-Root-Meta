{'class': [{'class': [],
            'func': [{'args': ['self'], 'defaults': [], 'name': 'Close'}, {'args': ['self'], 'defaults': [], 'name': 'OnUpdate'}, {'args': ['self'], 'defaults': [], 'name': '__del__'}, {'args': ['self', 'layer'], 'defaults': ['TOP_MOST'], 'name': '__init__'}],
            'import': [],
            'var': [{'name': 'BarHeight', 'type': 'int', 'value': 0},
                    {'name': 'CURTAIN_SPEED', 'type': 'int', 'value': 200},
                    {'name': 'CURTAIN_TIME', 'type': 'float', 'value': 0.25},
                    {'name': 'OnDoneEventList', 'type': 'list', 'value': []},
                    {'name': '__doc__', 'type': 'NoneType', 'value': None},
                    {'name': '__module__', 'type': 'str', 'value': 'uiQuest'},
                    {'name': '__qualname__', 'type': 'str', 'value': 'QuestCurtain'}]},
           {'class': [],
            'func': [{'args': ['self', 'parent', 'x', 'y', 'vnum'], 'defaults': [], 'name': 'CreateToolTip'},
                     {'args': ['self'], 'defaults': [], 'name': 'DestroyToolTip'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnMouseOverIn'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnMouseOverOut'},
                     {'args': ['self'], 'defaults': [], 'name': '__del__'},
                     {'args': ['self'], 'defaults': [], 'name': '__init__'}],
            'import': [],
            'var': [{'name': '__doc__', 'type': 'NoneType', 'value': None}, {'name': '__module__', 'type': 'str', 'value': 'uiQuest'}, {'name': '__qualname__', 'type': 'str', 'value': 'ItemToolTipImageBox'}]},
           {'class': [],
            'func': [{'args': ['self', 'speed'], 'defaults': [], 'name': 'FadeIn'},
                     {'args': ['self', 'speed'], 'defaults': [], 'name': 'FadeOut'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnUpdate'},
                     {'args': ['self', 'alpha'], 'defaults': [], 'name': 'SetAlpha'},
                     {'args': ['self', 'speed'], 'defaults': [], 'name': 'WhiteIn'},
                     {'args': ['self', 'speed'], 'defaults': [], 'name': 'WhiteOut'},
                     {'args': ['self'], 'defaults': [], 'name': '__EndFade'},
                     {'args': ['self', 'state', 'color', 'speed'], 'defaults': [], 'name': '__StartFade'},
                     {'args': ['self'], 'defaults': [], 'name': '__del__'},
                     {'args': ['self', 'index'], 'defaults': [], 'name': '__init__'}],
            'import': [],
            'var': [{'name': 'COLOR_BLACK', 'type': 'float', 'value': 1.0},
                    {'name': 'COLOR_WHITE', 'type': 'float', 'value': 0.0},
                    {'name': 'DEFAULT_FADE_SPEED', 'type': 'float', 'value': 0.035},
                    {'name': 'STATE_IN', 'type': 'int', 'value': 2},
                    {'name': 'STATE_OUT', 'type': 'int', 'value': 1},
                    {'name': 'STATE_WAIT', 'type': 'int', 'value': 0},
                    {'name': '__doc__', 'type': 'NoneType', 'value': None},
                    {'name': '__module__', 'type': 'str', 'value': 'uiQuest'},
                    {'name': '__qualname__', 'type': 'str', 'value': 'EventCurtain'}]},
           {'class': [],
            'func': [{'args': ['self'], 'defaults': [], 'name': 'OnRender'}, {'args': ['self'], 'defaults': [], 'name': '__del__'}, {'args': ['self', 'idx'], 'defaults': [], 'name': '__init__'}],
            'import': [],
            'var': [{'name': '__doc__', 'type': 'NoneType', 'value': None}, {'name': '__module__', 'type': 'str', 'value': 'uiQuest'}, {'name': '__qualname__', 'type': 'str', 'value': 'DescriptionWindow'}]},
           {'class': [],
            'func': [{'args': ['self', 'parent', 'title', 'desc', 'x', 'y'], 'defaults': [], 'name': 'CreateToolTip'},
                     {'args': ['self'], 'defaults': [], 'name': 'DestroyToolTip'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnMouseOverIn'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnMouseOverOut'},
                     {'args': ['self'], 'defaults': [], 'name': '__del__'},
                     {'args': ['self'], 'defaults': [], 'name': '__init__'}],
            'import': [],
            'var': [{'name': '__doc__', 'type': 'NoneType', 'value': None}, {'name': '__module__', 'type': 'str', 'value': 'uiQuest'}, {'name': '__qualname__', 'type': 'str', 'value': 'ToolTipImageBox'}]},
           {'class': [],
            'func': [{'args': ['self'], 'defaults': [], 'name': 'CallEvent'},
                     {'args': ['self'], 'defaults': [], 'name': 'DownEvent'},
                     {'args': ['self'], 'defaults': [], 'name': 'HideToolTip'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnRender'},
                     {'args': ['self'], 'defaults': [], 'name': 'ShowToolTip'},
                     {'args': ['self'], 'defaults': [], 'name': '__del__'},
                     {'args': ['self', 'layer', 'aColorUp', 'aColorDown', 'aColorOver'], 'defaults': ['UI', 1083808153, 1084926668, 1088282111], 'name': '__init__'}],
            'import': [],
            'var': [{'name': 'ColorDown', 'type': 'int', 'value': 1084926668},
                    {'name': 'ColorOver', 'type': 'int', 'value': 1088282111},
                    {'name': 'ColorUp', 'type': 'int', 'value': 1083808153},
                    {'name': 'DOWN', 'type': 'int', 'value': 1},
                    {'name': 'OVER', 'type': 'int', 'value': 2},
                    {'name': 'UP', 'type': 'int', 'value': 0},
                    {'name': '__doc__', 'type': 'NoneType', 'value': None},
                    {'name': '__module__', 'type': 'str', 'value': 'uiQuest'},
                    {'name': '__qualname__', 'type': 'str', 'value': 'BarButton'}]},
           {'class': [],
            'func': [{'args': ['self', 'parent', 'x', 'y', 'window_type', 'pos'], 'defaults': [], 'name': 'CreateToolTip'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnMouseOverIn'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnMouseOverOut'},
                     {'args': ['self'], 'defaults': [], 'name': '__del__'},
                     {'args': ['self'], 'defaults': [], 'name': '__init__'}],
            'import': [],
            'var': [{'name': '__doc__', 'type': 'NoneType', 'value': None}, {'name': '__module__', 'type': 'str', 'value': 'uiQuest'}, {'name': '__qualname__', 'type': 'str', 'value': 'CellItemToolTipImageBox'}]},
           {'class': [],
            'func': [{'args': ['self', 'f'], 'defaults': [], 'name': 'AddOnCloseEvent'},
                     {'args': ['self', 'f'], 'defaults': [], 'name': 'AddOnDoneEvent'},
                     {'args': ['self', 'x', 'y'], 'defaults': [], 'name': 'AdjustEventSetPosition'},
                     {'args': ['self', 'name', 'idx'], 'defaults': [], 'name': 'AppendQuestion'},
                     {'args': ['self', 'ai'], 'defaults': [], 'name': 'ClickAnswerEvent'},
                     {'args': ['self'], 'defaults': [], 'name': 'CloseSelf'},
                     {'args': ['self'], 'defaults': [], 'name': 'Destroy'},
                     {'args': ['self'], 'defaults': [], 'name': 'DoneEvent'},
                     {'args': ['self', 'speed'], 'defaults': [], 'name': 'FadeIn'},
                     {'args': ['self', 'speed'], 'defaults': [], 'name': 'FadeOut'},
                     {'args': ['self', 'skin'], 'defaults': [], 'name': 'LoadDialog'},
                     {'args': ['self', 'i'], 'defaults': [], 'name': 'MakeEachButton'},
                     {'args': ['self', 'button_type'], 'defaults': [], 'name': 'MakeNextButton'},
                     {'args': ['self'], 'defaults': [], 'name': 'MakeNextPrevPageButton'},
                     {'args': ['self'], 'defaults': [], 'name': 'MakeNextandCancelButton'},
                     {'args': ['self', 'n'], 'defaults': [], 'name': 'MakeQuestion'},
                     {'args': ['self', 'one', 'n'], 'defaults': [], 'name': 'NextQuestPageEvent'},
                     {'args': ['self', 'imgfile'], 'defaults': [], 'name': 'OnBackgroundImage'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnCancel'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnIMEReturn'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnIMEUpdate'},
                     {'args': ['self', 'x', 'y', 'filename', 'desc'], 'defaults': [''], 'name': 'OnImage'},
                     {'args': ['self', 'maxLen'], 'defaults': [], 'name': 'OnInput'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnInputAddcancel'},
                     {'args': ['self', 'filename', 'underTitle', 'title', 'desc', 'index', 'total'], 'defaults': [0, 1], 'name': 'OnInsertImage'},
                     {'args': ['self', 'vnum', 'index', 'total'], 'defaults': [0, 1], 'name': 'OnInsertImageShowItemToolTip'},
                     {'args': ['self', 'window_type', 'cell'], 'defaults': [], 'name': 'OnInsertImageShowItemToolTipByCell'},
                     {'args': ['self', 'type', 'idx', 'title', 'desc', 'index', 'total'], 'defaults': [0, 1], 'name': 'OnInsertItemIcon'},
                     {'args': ['self', 'key'], 'defaults': [], 'name': 'OnKeyDown'},
                     {'args': ['self', 'imgfile'], 'defaults': [], 'name': 'OnLeftImage'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnLongInput'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnPressEscapeKey'},
                     {'args': ['self', 'width', 'height'], 'defaults': [], 'name': 'OnSize'},
                     {'args': ['self', 'filename'], 'defaults': [], 'name': 'OnTitleImage'},
                     {'args': ['self', 'imgfile'], 'defaults': [], 'name': 'OnTopImage'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnUpdate'},
                     {'args': ['self', 'one', 'n'], 'defaults': [], 'name': 'PrevQuestPageEvent'},
                     {'args': ['self', 'n'], 'defaults': [], 'name': 'RefreshQuestPage'},
                     {'args': ['self', 'x', 'y'], 'defaults': [], 'name': 'SetEventSetPosition'},
                     {'args': ['self', 'f'], 'defaults': [], 'name': 'SetOnCloseEvent'},
                     {'args': ['self', 'speed'], 'defaults': [], 'name': 'WhiteIn'},
                     {'args': ['self', 'speed'], 'defaults': [], 'name': 'WhiteOut'},
                     {'args': ['self', 'filename'], 'defaults': [], 'name': '__GetQuestImageFileName'},
                     {'args': ['self'], 'defaults': [], 'name': '__del__'},
                     {'args': ['self', 'skin', 'idx'], 'defaults': [], 'name': '__init__'}],
            'import': [],
            'var': [{'name': 'QUEST_BUTTON_MAX_NUM', 'type': 'int', 'value': 8},
                    {'name': 'QUEST_CUT_WIDTH_LIMIT', 'type': 'int', 'value': 50},
                    {'name': 'QuestCurtain', 'type': 'QuestCurtain', 'value': <uiQuest.QuestCurtain object at 0x26C66EB0>},
                    {'name': 'SKIN_CINEMA', 'type': 'int', 'value': 5},
                    {'name': 'SKIN_NONE', 'type': 'int', 'value': 0},
                    {'name': 'TITLE_STATE_APPEAR', 'type': 'int', 'value': 1},
                    {'name': 'TITLE_STATE_DISAPPEAR', 'type': 'int', 'value': 3},
                    {'name': 'TITLE_STATE_NONE', 'type': 'int', 'value': 0},
                    {'name': 'TITLE_STATE_SHOW', 'type': 'int', 'value': 2},
                    {'name': '__doc__', 'type': 'NoneType', 'value': None},
                    {'name': '__module__', 'type': 'str', 'value': 'uiQuest'},
                    {'name': '__qualname__', 'type': 'str', 'value': 'QuestDialog'}]}],
 'func': [],
 'import': ['app', 'dbg', 'm2netm2g', 'playerm2g2', 'event', 'grp', 'localeInfo', '__builtin__', 'sys', 'grpImage', 'wndMgr', 'ui', 'time'],
 'var': [{'name': 'QUEST_BOARD_IMAGE_DIR', 'type': 'str', 'value': 'd:/ymir work/ui/game/questboard/'},
         {'name': '__doc__', 'type': 'NoneType', 'value': None},
         {'name': '__name__', 'type': 'str', 'value': 'uiQuest'},
         {'name': '__package__', 'type': 'NoneType', 'value': None},
         {'name': '__test__', 'type': 'dict', 'value': {}},
         {'name': 'cur_questpage_number', 'type': 'int', 'value': 1},
         {'name': 'entire_questbutton_number', 'type': 'int', 'value': 6},
         {'name': 'entire_questpage_number', 'type': 'int', 'value': 1},
         {'name': 'questbutton_max', 'type': 'int', 'value': 8}]}
