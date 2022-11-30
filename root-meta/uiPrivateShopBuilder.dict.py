{'class': [{'class': [],
            'func': [{'args': ['self'], 'defaults': [], 'name': 'OnMouseLeftButtonUp'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnUpdate'},
                     {'args': ['self', 'vid', 'text'], 'defaults': [], 'name': 'Open'},
                     {'args': ['self'], 'defaults': [], 'name': '__MakeTextLine'},
                     {'args': ['self'], 'defaults': [], 'name': '__del__'},
                     {'args': ['self'], 'defaults': [], 'name': '__init__'}],
            'import': [],
            'var': [{'name': '__doc__', 'type': 'NoneType', 'value': None}, {'name': '__module__', 'type': 'str', 'value': 'uiPrivateShopBuilder'}, {'name': '__qualname__', 'type': 'str', 'value': 'PrivateShopAdvertisementBoard'}]},
           {'class': [],
            'func': [{'args': ['self'], 'defaults': [], 'name': 'AcceptInputPrice'},
                     {'args': ['self', 'interface'], 'defaults': [], 'name': 'BindInterface'},
                     {'args': ['self'], 'defaults': [], 'name': 'CancelInputPrice'},
                     {'args': ['self', 'slotIndex'], 'defaults': [], 'name': 'CantTradableItem'},
                     {'args': ['self'], 'defaults': [], 'name': 'Close'},
                     {'args': ['self'], 'defaults': [], 'name': 'Destroy'},
                     {'args': ['self', 'winType', 'SlotPos'], 'defaults': [], 'name': 'GetItemDataSocketValue'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnClose'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnOk'},
                     {'args': ['self', 'slotIndex'], 'defaults': [], 'name': 'OnOverInItem'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnOverOutItem'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnPressEscapeKey'},
                     {'args': ['self', 'selectedSlotPos'], 'defaults': [], 'name': 'OnSelectEmptySlot'},
                     {'args': ['self', 'selectedSlotPos'], 'defaults': [], 'name': 'OnSelectItemSlot'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnTop'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnUpdate'},
                     {'args': ['self', 'title'], 'defaults': [], 'name': 'Open'},
                     {'args': ['self'], 'defaults': [], 'name': 'PrvShopTabRefresh'},
                     {'args': ['self'], 'defaults': [], 'name': 'Refresh'},
                     {'args': ['self', 'inven'], 'defaults': [], 'name': 'SetInven'},
                     {'args': ['self', 'bCashItem'], 'defaults': [], 'name': 'SetIsCashItem'},
                     {'args': ['self', 'tooltipItem'], 'defaults': [], 'name': 'SetItemToolTip'},
                     {'args': ['self', 'page'], 'defaults': [], 'name': 'SetPrivateShopPage'},
                     {'args': ['self', 'tabCnt'], 'defaults': [], 'name': 'SetTabCount'},
                     {'args': ['self', 'i'], 'defaults': [], 'name': '__GetRealIndex'},
                     {'args': ['self'], 'defaults': [], 'name': '__LoadWindow'},
                     {'args': ['self'], 'defaults': [], 'name': '__SetDefaultShopDecoPosition'},
                     {'args': ['self'], 'defaults': [], 'name': '__SetMyShopDecoPosition'},
                     {'args': ['self'], 'defaults': [], 'name': '__del__'},
                     {'args': ['self'], 'defaults': [], 'name': '__init__'}],
            'import': [],
            'var': [{'name': '__doc__', 'type': 'NoneType', 'value': None}, {'name': '__module__', 'type': 'str', 'value': 'uiPrivateShopBuilder'}, {'name': '__qualname__', 'type': 'str', 'value': 'PrivateShopBuilder'}]},
           {'class': [],
            'func': [{'args': ['self'], 'defaults': [], 'name': 'OnMouseLeftButtonUp'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnUpdate'},
                     {'args': ['self', 'vid', 'text'], 'defaults': [], 'name': 'Open'},
                     {'args': ['self'], 'defaults': [], 'name': '__CalcFontColor'},
                     {'args': ['self'], 'defaults': [], 'name': '__MakeTextLine'},
                     {'args': ['self'], 'defaults': [], 'name': '__del__'},
                     {'args': ['self', 'type'], 'defaults': [], 'name': '__init__'}],
            'import': [],
            'var': [{'name': '__doc__', 'type': 'NoneType', 'value': None}, {'name': '__module__', 'type': 'str', 'value': 'uiPrivateShopBuilder'}, {'name': '__qualname__', 'type': 'str', 'value': 'PrivateShopTitleBar'}]}],
 'func': [{'args': [], 'defaults': [], 'name': 'Clear'},
          {'args': ['vid'], 'defaults': [], 'name': 'DeleteADBoard'},
          {'args': ['itemVNum'], 'defaults': [], 'name': 'GetPrivateShopItemCheque'},
          {'args': ['itemVNum'], 'defaults': [], 'name': 'GetPrivateShopItemPrice'},
          {'args': [], 'defaults': [], 'name': 'IsBuildingPrivateShop'},
          {'args': [], 'defaults': [], 'name': 'IsPrivateShopItemPriceList'},
          {'args': ['itemVNum', 'itemPrice', 'itemCheque'], 'defaults': [], 'name': 'SetPrivateShopItemPrice'},
          {'args': [], 'defaults': [], 'name': 'UpdateADBoard'}],
 'import': ['shop', 'chatm2g', 'app', 'm2netm2g', 'playerm2g2', 'systemSetting', 'chr', 'mouseModule', 'localeInfo', 'uiCommon', 'snd', '__builtin__', 'item', 'ui'],
 'var': [{'name': 'INVENTORY_PAGE_SIZE', 'type': 'int', 'value': 45},
         {'name': 'PRIVATE_SHOP_WON', 'type': 'int', 'value': 1},
         {'name': 'PRIVATE_SHOP_YANG', 'type': 'int', 'value': 0},
         {'name': '__doc__', 'type': 'NoneType', 'value': None},
         {'name': '__name__', 'type': 'str', 'value': 'uiPrivateShopBuilder'},
         {'name': '__package__', 'type': 'NoneType', 'value': None},
         {'name': '__test__', 'type': 'dict', 'value': {}},
         {'name': 'g_isBuildingPrivateShop', 'type': 'bool', 'value': False},
         {'name': 'g_itemPriceDict', 'type': 'dict', 'value': {}},
         {'name': 'g_privateShopAdvertisementBoardDict', 'type': 'dict', 'value': {}}]}
