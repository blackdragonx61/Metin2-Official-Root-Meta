{'class': [{'class': [{'class': [],
                       'func': [{'args': ['self'], 'defaults': [], 'name': 'OnRender'}, {'args': ['self', 'index'], 'defaults': [], 'name': 'SetIndex'}, {'args': ['self'], 'defaults': [], 'name': '__del__'}, {'args': ['self'], 'defaults': [], 'name': '__init__'}],
                       'import': [],
                       'var': [{'name': '_DescriptionBox__desc_index', 'type': 'member_descriptor', 'value': <member '_DescriptionBox__desc_index' of 'DescriptionBox' objects>},
                               {'name': '__doc__', 'type': 'NoneType', 'value': None},
                               {'name': '__module__', 'type': 'str', 'value': 'uiMiniGameCatchKing'},
                               {'name': '__qualname__', 'type': 'str', 'value': 'CatchKingWaitingPage.DescriptionBox'},
                               {'name': '__slots__', 'type': 'str', 'value': '__desc_index'}]}],
            'func': [{'args': ['self', 'process_type', 'data'], 'defaults': [], 'name': 'CatchKingFlagProcess'},
                     {'args': ['self'], 'defaults': [], 'name': 'Close'},
                     {'args': ['self'], 'defaults': [], 'name': 'CloseStartDlg'},
                     {'args': ['self'], 'defaults': [], 'name': 'DecreaseMiniGameCatchKingCardCount'},
                     {'args': ['self'], 'defaults': [], 'name': 'Destroy'},
                     {'args': ['self'], 'defaults': [], 'name': 'NextDescriptionPage'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnPressEscapeKey'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnUpdate'},
                     {'args': ['self'], 'defaults': [], 'name': 'PrevDescriptionPage'},
                     {'args': ['self', 'tooltip'], 'defaults': [], 'name': 'SetItemToolTip'},
                     {'args': ['self'], 'defaults': [], 'name': 'Show'},
                     {'args': ['self'], 'defaults': [], 'name': '__ClickDownArrowButton'},
                     {'args': ['self'], 'defaults': [], 'name': '__ClickStartButton'},
                     {'args': ['self'], 'defaults': [], 'name': '__ClickUpArrowButton'},
                     {'args': ['self'], 'defaults': [], 'name': '__IsStartGame'},
                     {'args': ['self'], 'defaults': [], 'name': '__LoadWindow'},
                     {'args': ['self'], 'defaults': [], 'name': '__OverInChallengeText'},
                     {'args': ['self'], 'defaults': [], 'name': '__OverOutChallengeText'},
                     {'args': ['self', 'vnum'], 'defaults': [], 'name': '__SlotOverInItem'},
                     {'args': ['self'], 'defaults': [], 'name': '__SlotOverOutItem'},
                     {'args': ['self'], 'defaults': [], 'name': '__StartAccept'},
                     {'args': ['self'], 'defaults': [], 'name': '__StartCancel'},
                     {'args': ['self'], 'defaults': [], 'name': '__del__'},
                     {'args': ['self'], 'defaults': [], 'name': '__init__'}],
            'import': [],
            'var': [{'name': 'VISIBLE_LINE_COUNT', 'type': 'int', 'value': 8},
                    {'name': '_CatchKingWaitingPage__card_piece_count__card_count__card_piece_text__card_text__is_loaded__start_button__desc_board__description_box__desc_index__desc_y__btn_prev__btn_next__start_question_dialog__challenge_text_window__challenge_item_slot__challenge_item_count_text__challenge_up_arrow_button__challenge_down_arrow_button__tooltip_challenge__cur_challenge_count',
                     'type': 'member_descriptor',
                     'value': <member '_CatchKingWaitingPage__card_piece_count__card_count__card_piece_text__card_text__is_loaded__start_button__desc_board__description_box__desc_index__desc_y__btn_prev__btn_next__start_question_dialog__challenge_text_window__challenge_item_slot__challenge_item_count_text__challenge_up_arrow_button__challenge_down_arrow_button__tooltip_challenge__cur_challenge_count' of 'CatchKingWaitingPage' objects>},
                    {'name': '_CatchKingWaitingPage__tooltip', 'type': 'member_descriptor', 'value': <member '_CatchKingWaitingPage__tooltip' of 'CatchKingWaitingPage' objects>},
                    {'name': '__doc__', 'type': 'NoneType', 'value': None},
                    {'name': '__module__', 'type': 'str', 'value': 'uiMiniGameCatchKing'},
                    {'name': '__qualname__', 'type': 'str', 'value': 'CatchKingWaitingPage'},
                    {'name': '__slots__',
                     'type': 'tuple',
                     'value': ('__tooltip',
                               '__card_piece_count__card_count__card_piece_text__card_text__is_loaded__start_button__desc_board__description_box__desc_index__desc_y__btn_prev__btn_next__start_question_dialog__challenge_text_window__challenge_item_slot__challenge_item_count_text__challenge_up_arrow_button__challenge_down_arrow_button__tooltip_challenge__cur_challenge_count')}]},
           {'class': [],
            'func': [{'args': ['self', 'control_window'], 'defaults': [], 'name': 'BindControlWindow'},
                     {'args': ['self', 'src_type', 'src_index', 'dst_type', 'dst_index', 'number'], 'defaults': [], 'name': 'CardMoveHandToMyNumber'},
                     {'args': ['self', 'index'], 'defaults': [], 'name': 'ClickField'},
                     {'args': ['self', 'index', 'is_auto_click'], 'defaults': [False], 'name': 'ClickHand'},
                     {'args': ['self'], 'defaults': [], 'name': 'Close'},
                     {'args': ['self', 'src_type', 'src_index', 'dst_type', 'dst_index', 'number', 'end_func'], 'defaults': [None], 'name': 'CreateMoveImg'},
                     {'args': ['self'], 'defaults': [], 'name': 'Destroy'},
                     {'args': ['self', 'index', 'number', 'is_catch', 'is_mynumber_explosion', 'is_bingo', 'total_score', 'is_reward', 'is_search_number5'], 'defaults': [], 'name': 'FieldCardClickResult'},
                     {'args': ['self', 'data'], 'defaults': [], 'name': 'GameEndProcess'},
                     {'args': ['self', 'type', 'index'], 'defaults': [], 'name': 'GetCardPosition'},
                     {'args': ['self'], 'defaults': [], 'name': 'Initialize'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnPressEscapeKey'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnUpdate'},
                     {'args': ['self', 'index'], 'defaults': [], 'name': 'OverInFieldCard'},
                     {'args': ['self', 'index'], 'defaults': [], 'name': 'OverInHand'},
                     {'args': ['self', 'index'], 'defaults': [], 'name': 'OverOutFieldCard'},
                     {'args': ['self', 'index'], 'defaults': [], 'name': 'OverOutHand'},
                     {'args': ['self'], 'defaults': [], 'name': 'RewardSuccessPostProcess'},
                     {'args': ['self', 'type', 'index', 'number'], 'defaults': [], 'name': 'SetEndNumber'},
                     {'args': ['self', 'type', 'index'], 'defaults': [], 'name': 'SetExplosion'},
                     {'args': ['self', 'high_score'], 'defaults': [], 'name': 'SetHighScore'},
                     {'args': ['self', 'type', 'index', 'number'], 'defaults': [], 'name': 'SetNumber'},
                     {'args': ['self', 'score'], 'defaults': [], 'name': 'SetScore'},
                     {'args': ['self'], 'defaults': [], 'name': 'Show'},
                     {'args': ['self'], 'defaults': [], 'name': '__BindEvent'},
                     {'args': ['self'], 'defaults': [], 'name': '__BindObject'},
                     {'args': ['self'], 'defaults': [], 'name': '__CalculBingo'},
                     {'args': [], 'defaults': [], 'name': '__CardMoveCo'},
                     {'args': ['self', 'index', 'src_type', 'src_index', 'dst_type', 'dst_index', 'number'], 'defaults': [], 'name': '__CardMoveEndHandToMyNumber'},
                     {'args': ['self', 'new_state'], 'defaults': [], 'name': '__ChangeState'},
                     {'args': ['self'], 'defaults': [], 'name': '__ClearSuccessEffect'},
                     {'args': ['self'], 'defaults': [], 'name': '__ClickConfirmCheckButton'},
                     {'args': ['self'], 'defaults': [], 'name': '__ClickRewardButton'},
                     {'args': ['self'], 'defaults': [], 'name': '__CreateNumber5AnimationImage'},
                     {'args': ['self'], 'defaults': [], 'name': '__CreateObject'},
                     {'args': ['self'], 'defaults': [], 'name': '__ExplosionEnd'},
                     {'args': ['self', 'number', 'is_catch', 'is_mynumber_explosion', 'is_search_number5'], 'defaults': [], 'name': '__GetHelpMsgType'},
                     {'args': ['self'], 'defaults': [], 'name': '__HideNumber5Area'},
                     {'args': ['self', 'index'], 'defaults': [], 'name': '__IsFieldCardOpen'},
                     {'args': ['self'], 'defaults': [], 'name': '__LoadWindow'},
                     {'args': ['self'], 'defaults': [], 'name': '__OverInScore'},
                     {'args': ['self'], 'defaults': [], 'name': '__OverOutScore'},
                     {'args': ['self', 'index'], 'defaults': [], 'name': '__RefreshFieldCardArrow'},
                     {'args': ['self'], 'defaults': [], 'name': '__RefreshScore'},
                     {'args': ['self', 'type'], 'defaults': [], 'name': '__ShowHelpPopup'},
                     {'args': ['self', 'index'], 'defaults': [], 'name': '__ShowNumber5Area'},
                     {'args': ['self'], 'defaults': [], 'name': '__SuccessEffectEndFrameEvent'},
                     {'args': ['self'], 'defaults': [], 'name': '__SuccessExplosionEffectEndFrame1'},
                     {'args': ['self'], 'defaults': [], 'name': '__SuccessExplosionEffectEndFrame2'},
                     {'args': ['self'], 'defaults': [], 'name': '__SuccessExplosionEffectEndFrame3'},
                     {'args': ['self', 'cur_frame'], 'defaults': [], 'name': '__SuccessExplosionEffectKeyFrame1'},
                     {'args': ['self', 'cur_frame'], 'defaults': [], 'name': '__SuccessExplosionEffectKeyFrame2'},
                     {'args': ['self', 'cur_frame'], 'defaults': [], 'name': '__SuccessExplosionEffectKeyFrame3'},
                     {'args': ['self'], 'defaults': [], 'name': '__UpdateEvent'},
                     {'args': ['self'], 'defaults': [], 'name': '__del__'},
                     {'args': ['self'], 'defaults': [], 'name': '__init__'},
                     {'args': ['original_func'], 'defaults': [], 'name': 'coroutine_wrapper'}],
            'import': [],
            'var': [{'name': '__doc__', 'type': 'NoneType', 'value': None}, {'name': '__module__', 'type': 'str', 'value': 'uiMiniGameCatchKing'}, {'name': '__qualname__', 'type': 'str', 'value': 'CatchKingGamePage'}]},
           {'class': [],
            'func': [{'args': ['self'], 'defaults': [], 'name': 'GetCount'},
                     {'args': ['self', 'is_show'], 'defaults': [], 'name': 'SetArrow'},
                     {'args': ['self', 'is_show'], 'defaults': [], 'name': 'SetBingo'},
                     {'args': ['self', 'count'], 'defaults': [], 'name': 'SetCount'},
                     {'args': ['self', 'card_number'], 'defaults': [], 'name': 'SetEndNumber'},
                     {'args': ['self', 'card_number'], 'defaults': [], 'name': 'SetNumber'},
                     {'args': ['self', 'is_show'], 'defaults': [], 'name': 'SetShowOverImg'},
                     {'args': ['self'], 'defaults': [], 'name': '__ClickFunc'},
                     {'args': ['self', 'parent'], 'defaults': [], 'name': '__CreateArrowImg'},
                     {'args': ['self', 'parent'], 'defaults': [], 'name': '__CreateBingoImg'},
                     {'args': ['self', 'parent'], 'defaults': [], 'name': '__CreateCardOverImg'},
                     {'args': ['self', 'parent'], 'defaults': [], 'name': '__CreateCountImg'},
                     {'args': ['self', 'parent'], 'defaults': [], 'name': '__CreateDefaultCard'},
                     {'args': ['self'], 'defaults': [], 'name': '__CreateObject'},
                     {'args': ['self'], 'defaults': [], 'name': '__OverFunc'},
                     {'args': ['self'], 'defaults': [], 'name': '__OverOutFunc'},
                     {'args': ['self'], 'defaults': [], 'name': '__del__'},
                     {'args': ['self', 'parent', 'default_x', 'default_y', 'pos_type', 'index', 'click_func', 'over_func', 'overout_func'], 'defaults': [None, None, None], 'name': '__init__'}],
            'import': [],
            'var': [{'name': '__doc__', 'type': 'NoneType', 'value': None}, {'name': '__module__', 'type': 'str', 'value': 'uiMiniGameCatchKing'}, {'name': '__qualname__', 'type': 'str', 'value': 'CatchKingCard'}]},
           {'class': [],
            'func': [{'args': ['bad-module'], 'defaults': ['bad-module'], 'name': '__new__'}],
            'import': [],
            'var': [{'name': '__copy__', 'type': 'method_descriptor', 'value': <method '__copy__' of 'collections.deque' objects>},
                    {'name': '__delitem__', 'type': 'wrapper_descriptor', 'value': <slot wrapper '__delitem__' of 'collections.deque' objects>},
                    {'name': '__doc__', 'type': 'str', 'value': 'deque(iterable[, maxlen]) --> deque object\n\nBuild an ordered collection with optimized access from its endpoints.'},
                    {'name': '__eq__', 'type': 'wrapper_descriptor', 'value': <slot wrapper '__eq__' of 'collections.deque' objects>},
                    {'name': '__ge__', 'type': 'wrapper_descriptor', 'value': <slot wrapper '__ge__' of 'collections.deque' objects>},
                    {'name': '__getattribute__', 'type': 'wrapper_descriptor', 'value': <slot wrapper '__getattribute__' of 'collections.deque' objects>},
                    {'name': '__getitem__', 'type': 'wrapper_descriptor', 'value': <slot wrapper '__getitem__' of 'collections.deque' objects>},
                    {'name': '__gt__', 'type': 'wrapper_descriptor', 'value': <slot wrapper '__gt__' of 'collections.deque' objects>},
                    {'name': '__hash__', 'type': 'NoneType', 'value': None},
                    {'name': '__iadd__', 'type': 'wrapper_descriptor', 'value': <slot wrapper '__iadd__' of 'collections.deque' objects>},
                    {'name': '__init__', 'type': 'wrapper_descriptor', 'value': <slot wrapper '__init__' of 'collections.deque' objects>},
                    {'name': '__iter__', 'type': 'wrapper_descriptor', 'value': <slot wrapper '__iter__' of 'collections.deque' objects>},
                    {'name': '__le__', 'type': 'wrapper_descriptor', 'value': <slot wrapper '__le__' of 'collections.deque' objects>},
                    {'name': '__len__', 'type': 'wrapper_descriptor', 'value': <slot wrapper '__len__' of 'collections.deque' objects>},
                    {'name': '__lt__', 'type': 'wrapper_descriptor', 'value': <slot wrapper '__lt__' of 'collections.deque' objects>},
                    {'name': '__ne__', 'type': 'wrapper_descriptor', 'value': <slot wrapper '__ne__' of 'collections.deque' objects>},
                    {'name': '__reduce__', 'type': 'method_descriptor', 'value': <method '__reduce__' of 'collections.deque' objects>},
                    {'name': '__repr__', 'type': 'wrapper_descriptor', 'value': <slot wrapper '__repr__' of 'collections.deque' objects>},
                    {'name': '__reversed__', 'type': 'method_descriptor', 'value': <method '__reversed__' of 'collections.deque' objects>},
                    {'name': '__setitem__', 'type': 'wrapper_descriptor', 'value': <slot wrapper '__setitem__' of 'collections.deque' objects>},
                    {'name': 'append', 'type': 'method_descriptor', 'value': <method 'append' of 'collections.deque' objects>},
                    {'name': 'appendleft', 'type': 'method_descriptor', 'value': <method 'appendleft' of 'collections.deque' objects>},
                    {'name': 'clear', 'type': 'method_descriptor', 'value': <method 'clear' of 'collections.deque' objects>},
                    {'name': 'count', 'type': 'method_descriptor', 'value': <method 'count' of 'collections.deque' objects>},
                    {'name': 'extend', 'type': 'method_descriptor', 'value': <method 'extend' of 'collections.deque' objects>},
                    {'name': 'extendleft', 'type': 'method_descriptor', 'value': <method 'extendleft' of 'collections.deque' objects>},
                    {'name': 'maxlen', 'type': 'getset_descriptor', 'value': <attribute 'maxlen' of 'collections.deque' objects>},
                    {'name': 'pop', 'type': 'method_descriptor', 'value': <method 'pop' of 'collections.deque' objects>},
                    {'name': 'popleft', 'type': 'method_descriptor', 'value': <method 'popleft' of 'collections.deque' objects>},
                    {'name': 'remove', 'type': 'method_descriptor', 'value': <method 'remove' of 'collections.deque' objects>},
                    {'name': 'reverse', 'type': 'method_descriptor', 'value': <method 'reverse' of 'collections.deque' objects>},
                    {'name': 'rotate', 'type': 'method_descriptor', 'value': <method 'rotate' of 'collections.deque' objects>}]},
           {'class': [],
            'func': [{'args': ['self', 'type', 'data'], 'defaults': [], 'name': 'CatchKingFlagProcess'},
                     {'args': ['self', 'type', 'data'], 'defaults': [], 'name': 'CatchKingProcess'},
                     {'args': ['self', 'state'], 'defaults': [], 'name': 'ChangeState'},
                     {'args': ['self'], 'defaults': [], 'name': 'Close'},
                     {'args': ['self'], 'defaults': [], 'name': 'Destroy'},
                     {'args': ['self'], 'defaults': [], 'name': 'Open'},
                     {'args': ['self', 'tooltip'], 'defaults': [], 'name': 'SetItemToolTip'},
                     {'args': ['self'], 'defaults': [], 'name': 'Show'},
                     {'args': ['self'], 'defaults': [], 'name': '__LoadWindow'},
                     {'args': ['self'], 'defaults': [], 'name': '__del__'},
                     {'args': ['self'], 'defaults': [], 'name': '__init__'}],
            'import': [],
            'var': [{'name': '__doc__', 'type': 'NoneType', 'value': None}, {'name': '__module__', 'type': 'str', 'value': 'uiMiniGameCatchKing'}, {'name': '__qualname__', 'type': 'str', 'value': 'MiniGameCatchKing'}]}],
 'func': [{'args': ['card_number'], 'defaults': [], 'name': 'GetCardTooltip'},
          {'args': ['card_number'], 'defaults': [], 'name': 'GetEndImgPath'},
          {'args': ['card_number'], 'defaults': [], 'name': 'GetImgPath'},
          {'args': ['self', 'fileName'], 'defaults': [], 'name': 'LoadScript'},
          {'args': ['bad-module'], 'defaults': ['bad-module'], 'name': 'proxy'},
          {'args': ['wrapped', 'assigned', 'updated'], 'defaults': [('__module__', '__name__', '__doc__'), ('__dict__',)], 'name': 'wraps'}],
 'import': ['constInfo', 'uiScriptLocale', 'localeInfo', 'grpImage', 'event', 'uiToolTip', '__builtin__', 'ingameEventSystem', 'wndMgr', 'item', 'chatm2g', 'app', 'ui', 'm2netm2g', 'playerm2g2', 'grp', 'uiCommon', 'snd'],
 'var': [{'name': 'CARD_HEIGHT', 'type': 'int', 'value': 36},
         {'name': 'CARD_MOVE_SPEED', 'type': 'float', 'value': 25.0},
         {'name': 'CARD_NUMBER_1', 'type': 'int', 'value': 1},
         {'name': 'CARD_NUMBER_2', 'type': 'int', 'value': 2},
         {'name': 'CARD_NUMBER_3', 'type': 'int', 'value': 3},
         {'name': 'CARD_NUMBER_4', 'type': 'int', 'value': 4},
         {'name': 'CARD_NUMBER_5', 'type': 'int', 'value': 5},
         {'name': 'CARD_NUMBER_6', 'type': 'int', 'value': 6},
         {'name': 'CARD_NUMBER_K', 'type': 'int', 'value': 0},
         {'name': 'CARD_PACK', 'type': 'int', 'value': 7},
         {'name': 'CARD_WIDTH', 'type': 'int', 'value': 50},
         {'name': 'CATCHKING_CARD_COUNT_MAX', 'type': 'int', 'value': 999},
         {'name': 'CATCHKING_CARD_PIECE_COUNT_MAX', 'type': 'int', 'value': 25},
         {'name': 'CATCHKING_CHALLENGE_MAX', 'type': 'int', 'value': 5},
         {'name': 'CATCHKING_START_YANG', 'type': 'int', 'value': 30000},
         {'name': 'CATCHKING_WINDOW_HEIGHT', 'type': 'int', 'value': 336},
         {'name': 'CATCHKING_WINDOW_WIDTH', 'type': 'int', 'value': 392},
         {'name': 'CK_STATE_FIELD_CLICK', 'type': 'int', 'value': 2},
         {'name': 'CK_STATE_HAND_CLICK', 'type': 'int', 'value': 3},
         {'name': 'CK_STATE_REWARD', 'type': 'int', 'value': 4},
         {'name': 'CK_STATE_REWARD_END', 'type': 'int', 'value': 5},
         {'name': 'CK_STATE_START', 'type': 'int', 'value': 0},
         {'name': 'CK_STATE_WAIT', 'type': 'int', 'value': 1},
         {'name': 'DEFAULT_DESC_Y', 'type': 'int', 'value': 7},
         {'name': 'DESC_WIDTH_COUNT', 'type': 'int', 'value': 57},
         {'name': 'EVENT_TYPE_DELAY', 'type': 'int', 'value': 2},
         {'name': 'EVENT_TYPE_HAND_CARD_CLICK', 'type': 'int', 'value': 11},
         {'name': 'EVENT_TYPE_HELP_POPUP', 'type': 'int', 'value': 15},
         {'name': 'EVENT_TYPE_HIDE_NUMBER5_AREA', 'type': 'int', 'value': 14},
         {'name': 'EVENT_TYPE_INIT_FIELD_CARD', 'type': 'int', 'value': 0},
         {'name': 'EVENT_TYPE_INSER_DELAY', 'type': 'int', 'value': 1},
         {'name': 'EVENT_TYPE_POPUP', 'type': 'int', 'value': 10},
         {'name': 'EVENT_TYPE_SET_ARROW', 'type': 'int', 'value': 7},
         {'name': 'EVENT_TYPE_SET_END_NUMBER', 'type': 'int', 'value': 12},
         {'name': 'EVENT_TYPE_SET_NUMBER', 'type': 'int', 'value': 3},
         {'name': 'EVENT_TYPE_SET_SCORE', 'type': 'int', 'value': 6},
         {'name': 'EVENT_TYPE_SET_STATE', 'type': 'int', 'value': 5},
         {'name': 'EVENT_TYPE_SHOW_NUMBER5_AREA', 'type': 'int', 'value': 13},
         {'name': 'EVENT_TYPE_SUCCESS_EFFECT', 'type': 'int', 'value': 8},
         {'name': 'EVNET_TYPE_BINGO_CHECK', 'type': 'int', 'value': 9},
         {'name': 'EVNET_TYPE_SET_EXPLOSION', 'type': 'int', 'value': 4},
         {'name': 'FIELD_CARD_GEP_X', 'type': 'int', 'value': 1},
         {'name': 'FIELD_CARD_GEP_Y', 'type': 'int', 'value': 1},
         {'name': 'FIELD_CARD_MAX', 'type': 'int', 'value': 25},
         {'name': 'FIELD_CARD_Y', 'type': 'int', 'value': 5},
         {'name': 'FILED_CARD_X', 'type': 'int', 'value': 5},
         {'name': 'HAND_CARD_MAX', 'type': 'int', 'value': 6},
         {'name': 'HELP_MSG_TYPE_HIGH_NUMBER', 'type': 'int', 'value': 3},
         {'name': 'HELP_MSG_TYPE_LOW_NUMBER', 'type': 'int', 'value': 1},
         {'name': 'HELP_MSG_TYPE_SAME_NUMBER', 'type': 'int', 'value': 2},
         {'name': 'HELP_MSG_TYPE_SEARCH_NUMBER5', 'type': 'int', 'value': 4},
         {'name': 'LOW_TOTAL_SCORE', 'type': 'int', 'value': 400},
         {'name': 'MID_TOTAL_SCORE', 'type': 'int', 'value': 550},
         {'name': 'POS_TYPE_FIELD', 'type': 'int', 'value': 0},
         {'name': 'POS_TYPE_HAND', 'type': 'int', 'value': 1},
         {'name': 'POS_TYPE_MYNUMBER', 'type': 'int', 'value': 2},
         {'name': 'POS_TYPE_SELECTION_NUMER', 'type': 'int', 'value': 3},
         {'name': 'STATE_NONE', 'type': 'int', 'value': 0},
         {'name': 'STATE_PLAY', 'type': 'int', 'value': 2},
         {'name': 'STATE_WAITING', 'type': 'int', 'value': 1},
         {'name': 'TOTAL_SCORE_HIGH_FONT_COLOR', 'type': 'long', 'value': 4294967193L},
         {'name': 'TOTAL_SCORE_LOW_FONT_COLOR', 'type': 'int', 'value': -3750202},
         {'name': 'TOTAL_SCORE_MID_FONT_COLOR', 'type': 'long', 'value': 4293830912L},
         {'name': '__doc__', 'type': 'NoneType', 'value': None},
         {'name': '__name__', 'type': 'str', 'value': 'uiMiniGameCatchKing'},
         {'name': '__package__', 'type': 'NoneType', 'value': None},
         {'name': '__test__', 'type': 'dict', 'value': {}},
         {'name': 'card_default_count', 'type': 'dict', 'value': {1: 5, 2: 2, 3: 2, 4: 1, 5: 1, 6: 1}},
         {'name': 'card_end_img_path',
          'type': 'dict',
          'value': {1: 'd:/ymir work/ui/minigame/catchking/end_card_number_1.sub',
                    2: 'd:/ymir work/ui/minigame/catchking/end_card_number_2.sub',
                    3: 'd:/ymir work/ui/minigame/catchking/end_card_number_3.sub',
                    4: 'd:/ymir work/ui/minigame/catchking/end_card_number_4.sub',
                    5: 'd:/ymir work/ui/minigame/catchking/end_card_number_5.sub',
                    6: 'd:/ymir work/ui/minigame/catchking/end_card_number_6.sub'}},
         {'name': 'card_img_path',
          'type': 'dict',
          'value': {0: 'd:/ymir work/ui/minigame/catchking/card_number_k.sub',
                    1: 'd:/ymir work/ui/minigame/catchking/card_number_1.sub',
                    2: 'd:/ymir work/ui/minigame/catchking/card_number_2.sub',
                    3: 'd:/ymir work/ui/minigame/catchking/card_number_3.sub',
                    4: 'd:/ymir work/ui/minigame/catchking/card_number_4.sub',
                    5: 'd:/ymir work/ui/minigame/catchking/card_number_5.sub',
                    6: 'd:/ymir work/ui/minigame/catchking/card_number_6.sub',
                    7: 'd:/ymir work/ui/minigame/catchking/card_pack.sub'}},
         {'name': 'challenge_tooltip', 'type': 'tuple', 'value': ('Ha t\xf6bb %s-t teszel fel t\xe9tk\xe9nt, pont ugyanannyi l\xe1d\xe1t fogsz jutalmul kapni.', 'Maximum t\xe9t: %d Kir\xe1lypakli.')},
         {'name': 'score_tooltip', 'type': 'tuple', 'value': ('%s: 550 \xe9s felette', '%s: 400 \xe9s 549 k\xf6z\xf6tt', '%s: 10 \xe9s 399 k\xf6z\xf6tt', '10 b\xf3nusz pontot kapsz, ha minden k\xe1rty\xe1t felford\xedtasz egy vonalban.')}]}
