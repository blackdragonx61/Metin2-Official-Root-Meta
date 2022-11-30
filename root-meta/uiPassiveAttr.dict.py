{'class': [{'class': [],
            'func': [{'args': ['self', 'inven_window', 'inven_slot_index'], 'defaults': [], 'name': 'AttachToPassiveAttrSlot'},
                     {'args': ['self', 'interface'], 'defaults': [], 'name': 'BindInterface'},
                     {'args': ['self', 'request_page'], 'defaults': [], 'name': 'ClickActivateButton'},
                     {'args': ['self', 'is_packet_send'], 'defaults': [True], 'name': 'Close'},
                     {'args': ['self'], 'defaults': [], 'name': 'Destroy'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnPressEscapeKey'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnTop'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnUpdate'},
                     {'args': ['self'], 'defaults': [], 'name': 'Open'},
                     {'args': ['self', 'type', 'data'], 'defaults': [], 'name': 'PassiveAttrProcess'},
                     {'args': ['self'], 'defaults': [], 'name': 'RefreshPassiveAttrActivateButton'},
                     {'args': ['self'], 'defaults': [], 'name': 'RefreshPassiveAttrJobSlot'},
                     {'args': ['self'], 'defaults': [], 'name': 'RefreshPassiveAttrSubSlot'},
                     {'args': ['self', 'inven'], 'defaults': [], 'name': 'SetInven'},
                     {'args': ['self', 'tooltip_item'], 'defaults': [], 'name': 'SetItemToolTip'},
                     {'args': ['self', 'request_page'], 'defaults': [], 'name': '__ActivateDeactivateProcess'},
                     {'args': ['self', 'inven_window', 'inven_slot_index'], 'defaults': [], 'name': '__AttachToPassiveAttrSlot'},
                     {'args': ['self'], 'defaults': [], 'name': '__BindEvent'},
                     {'args': ['self'], 'defaults': [], 'name': '__BindObject'},
                     {'args': ['self', 'page'], 'defaults': [], 'name': '__CheckActivate'},
                     {'args': ['self', 'page'], 'defaults': [], 'name': '__CheckDeactivate'},
                     {'args': ['self'], 'defaults': [], 'name': '__CheckInvenCantMouseEvent'},
                     {'args': ['self'], 'defaults': [], 'name': '__CheckPassiveJobSlotCantMouseEvent'},
                     {'args': ['self'], 'defaults': [], 'name': '__ClearCurPageSubSlot'},
                     {'args': ['self'], 'defaults': [], 'name': '__ClickAddButton'},
                     {'args': ['self'], 'defaults': [], 'name': '__ClickChargeButton'},
                     {'args': ['self', 'button_object', 'request_page'], 'defaults': [], 'name': '__ClickPassiveAttrChangePage'},
                     {'args': ['self'], 'defaults': [], 'name': '__CreateQuestionPopup'},
                     {'args': ['self', 'slot_index'], 'defaults': [], 'name': '__GetInvenPos'},
                     {'args': ['self', 'page'], 'defaults': [], 'name': '__GetWearPos'},
                     {'args': ['self'], 'defaults': [], 'name': '__IsShowPopup'},
                     {'args': ['self', 'fileName'], 'defaults': [], 'name': '__LoadScript'},
                     {'args': ['self'], 'defaults': [], 'name': '__LoadWindow'},
                     {'args': ['self', 'slot_index'], 'defaults': [], 'name': '__OverInPassiveJobSlot'},
                     {'args': ['self', 'slot_index'], 'defaults': [], 'name': '__OverInSubSlot'},
                     {'args': ['self'], 'defaults': [], 'name': '__OverOutSlot'},
                     {'args': ['self', 'is_success'], 'defaults': [], 'name': '__PassiveAttrAddReresultProcess'},
                     {'args': ['self'], 'defaults': [], 'name': '__PassiveAttrChargeReresultProcess'},
                     {'args': ['self', 'slot_index'], 'defaults': [], 'name': '__SelectEmptySlot'},
                     {'args': ['self', 'is_equipment', 'window', 'index'], 'defaults': [], 'name': '__SendItemUsePacket'},
                     {'args': ['self', 'is_activate', 'page'], 'defaults': [], 'name': '__SendPassiveAttrActivateDeactivate'},
                     {'args': ['self', 'result_tuple'], 'defaults': [], 'name': '__SendPassiveAttrCharge'},
                     {'args': ['self', 'slot_index', 'inven_pos'], 'defaults': [], 'name': '__SetInvenPos'},
                     {'args': ['self', 'on_top_window'], 'defaults': [], 'name': '__SetOnTopWindow'},
                     {'args': ['self', 'newPage'], 'defaults': [], 'name': '__SetPassiveAttrPage'},
                     {'args': ['self'], 'defaults': [], 'name': '__Show'},
                     {'args': ['self', 'slot_index'], 'defaults': [], 'name': '__UnselectSlotPassiveJobSlot'},
                     {'args': ['self', 'slot_index'], 'defaults': [], 'name': '__UnselectSubSlot'},
                     {'args': ['self'], 'defaults': [], 'name': '__del__'},
                     {'args': ['self'], 'defaults': [], 'name': '__init__'}],
            'import': [],
            'var': [{'name': 'CantAttachToPassiveSlot', 'type': 'classmethod', 'value': <classmethod object at 0x19C4C750>},
                    {'name': '_PassiveAttr__COOLTIME_SECOND_ACTIVATE', 'type': 'int', 'value': 5},
                    {'name': '_PassiveAttr__COOLTIME_SECOND_EQUIPMENT', 'type': 'int', 'value': 5},
                    {'name': '_PassiveAttr__COOLTIME_SECOND_UNEQUIPMENT', 'type': 'int', 'value': 5},
                    {'name': '_PassiveAttr__ITEM_ATTRIBUTE_PASSIVE_JOB_MAX', 'type': 'int', 'value': 4},
                    {'name': '_PassiveAttr__SLOT_INDEX_ACCE', 'type': 'int', 'value': 4},
                    {'name': '_PassiveAttr__SLOT_INDEX_ARMOR', 'type': 'int', 'value': 3},
                    {'name': '_PassiveAttr__SLOT_INDEX_ELEMENT', 'type': 'int', 'value': 2},
                    {'name': '_PassiveAttr__SLOT_INDEX_JOB', 'type': 'int', 'value': 0},
                    {'name': '_PassiveAttr__SLOT_INDEX_MAX', 'type': 'int', 'value': 5},
                    {'name': '_PassiveAttr__SLOT_INDEX_WEAPON', 'type': 'int', 'value': 1},
                    {'name': '_PassiveAttr__SLOT_PAGE_DOWN', 'type': 'int', 'value': 2},
                    {'name': '_PassiveAttr__SLOT_PAGE_NONE', 'type': 'int', 'value': 0},
                    {'name': '_PassiveAttr__SLOT_PAGE_SIZE', 'type': 'int', 'value': 2},
                    {'name': '_PassiveAttr__SLOT_PAGE_UP', 'type': 'int', 'value': 1},
                    {'name': '_PassiveAttr__WRONG_VALUE', 'type': 'int', 'value': -1},
                    {'name': '_PassiveAttr__activate_button', 'type': 'member_descriptor', 'value': <member '_PassiveAttr__activate_button' of 'PassiveAttr' objects>},
                    {'name': '_PassiveAttr__activate_page__passive_job_slot_dict', 'type': 'member_descriptor', 'value': <member '_PassiveAttr__activate_page__passive_job_slot_dict' of 'PassiveAttr' objects>},
                    {'name': '_PassiveAttr__add_button', 'type': 'member_descriptor', 'value': <member '_PassiveAttr__add_button' of 'PassiveAttr' objects>},
                    {'name': '_PassiveAttr__charge_button', 'type': 'member_descriptor', 'value': <member '_PassiveAttr__charge_button' of 'PassiveAttr' objects>},
                    {'name': '_PassiveAttr__cooltime_activate', 'type': 'member_descriptor', 'value': <member '_PassiveAttr__cooltime_activate' of 'PassiveAttr' objects>},
                    {'name': '_PassiveAttr__cooltime_equip', 'type': 'member_descriptor', 'value': <member '_PassiveAttr__cooltime_equip' of 'PassiveAttr' objects>},
                    {'name': '_PassiveAttr__cooltime_unequip', 'type': 'member_descriptor', 'value': <member '_PassiveAttr__cooltime_unequip' of 'PassiveAttr' objects>},
                    {'name': '_PassiveAttr__cur_page', 'type': 'member_descriptor', 'value': <member '_PassiveAttr__cur_page' of 'PassiveAttr' objects>},
                    {'name': '_PassiveAttr__destroy_popup__charge_popup', 'type': 'member_descriptor', 'value': <member '_PassiveAttr__destroy_popup__charge_popup' of 'PassiveAttr' objects>},
                    {'name': '_PassiveAttr__first_use_popup', 'type': 'member_descriptor', 'value': <member '_PassiveAttr__first_use_popup' of 'PassiveAttr' objects>},
                    {'name': '_PassiveAttr__interface', 'type': 'member_descriptor', 'value': <member '_PassiveAttr__interface' of 'PassiveAttr' objects>},
                    {'name': '_PassiveAttr__inven', 'type': 'member_descriptor', 'value': <member '_PassiveAttr__inven' of 'PassiveAttr' objects>},
                    {'name': '_PassiveAttr__inven_pos_dict', 'type': 'member_descriptor', 'value': <member '_PassiveAttr__inven_pos_dict' of 'PassiveAttr' objects>},
                    {'name': '_PassiveAttr__is_loaded', 'type': 'member_descriptor', 'value': <member '_PassiveAttr__is_loaded' of 'PassiveAttr' objects>},
                    {'name': '_PassiveAttr__is_requesting_activate_deactivate', 'type': 'member_descriptor', 'value': <member '_PassiveAttr__is_requesting_activate_deactivate' of 'PassiveAttr' objects>},
                    {'name': '_PassiveAttr__is_requesting_add', 'type': 'member_descriptor', 'value': <member '_PassiveAttr__is_requesting_add' of 'PassiveAttr' objects>},
                    {'name': '_PassiveAttr__is_requesting_change_page', 'type': 'member_descriptor', 'value': <member '_PassiveAttr__is_requesting_change_page' of 'PassiveAttr' objects>},
                    {'name': '_PassiveAttr__is_requesting_charge', 'type': 'member_descriptor', 'value': <member '_PassiveAttr__is_requesting_charge' of 'PassiveAttr' objects>},
                    {'name': '_PassiveAttr__is_requesting_open', 'type': 'member_descriptor', 'value': <member '_PassiveAttr__is_requesting_open' of 'PassiveAttr' objects>},
                    {'name': '_PassiveAttr__page_button_dict', 'type': 'member_descriptor', 'value': <member '_PassiveAttr__page_button_dict' of 'PassiveAttr' objects>},
                    {'name': '_PassiveAttr__sub_slot', 'type': 'member_descriptor', 'value': <member '_PassiveAttr__sub_slot' of 'PassiveAttr' objects>},
                    {'name': '_PassiveAttr__tooltip_item', 'type': 'member_descriptor', 'value': <member '_PassiveAttr__tooltip_item' of 'PassiveAttr' objects>},
                    {'name': '__doc__', 'type': 'NoneType', 'value': None},
                    {'name': '__module__', 'type': 'str', 'value': 'uiPassiveAttr'},
                    {'name': '__qualname__', 'type': 'str', 'value': 'PassiveAttr'},
                    {'name': '__slots__',
                     'type': 'tuple',
                     'value': ('__is_loaded',
                               '__inven_pos_dict',
                               '__cur_page',
                               '__activate_page__passive_job_slot_dict',
                               '__sub_slot',
                               '__page_button_dict',
                               '__charge_button',
                               '__add_button',
                               '__activate_button',
                               '__tooltip_item',
                               '__interface',
                               '__inven',
                               '__first_use_popup',
                               '__destroy_popup__charge_popup',
                               '__is_requesting_open',
                               '__is_requesting_change_page',
                               '__is_requesting_charge',
                               '__is_requesting_add',
                               '__is_requesting_activate_deactivate',
                               '__cooltime_equip',
                               '__cooltime_unequip',
                               '__cooltime_activate')}]}],
 'func': [{'args': ['bad-module'], 'defaults': ['bad-module'], 'name': 'proxy'}],
 'import': ['uiCommon', '__builtin__', 'chatm2g', 'app', 'uiPrivateShopBuilder', 'item', 'm2netm2g', 'playerm2g2', 'ui', 'mouseModule', 'uiScriptLocale', 'localeInfo'],
 'var': [{'name': '__doc__', 'type': 'NoneType', 'value': None}, {'name': '__name__', 'type': 'str', 'value': 'uiPassiveAttr'}, {'name': '__package__', 'type': 'NoneType', 'value': None}, {'name': '__test__', 'type': 'dict', 'value': {}}]}
