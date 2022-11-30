{'class': [{'class': [],
            'func': [{'args': ['self'], 'defaults': [], 'name': 'Disable'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnMouseLeftButtonDown'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnMouseLeftButtonUp'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnMouseOverIn'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnMouseOverOut'},
                     {'args': ['self', 'flag'], 'defaults': [], 'name': 'SetCheck'},
                     {'args': ['self'], 'defaults': [], 'name': '__del__'},
                     {'args': ['self', 'parent', 'x', 'y', 'event', 'filename'], 'defaults': ['d:/ymir work/ui/privatesearch/private_checkboxImg.sub'], 'name': '__init__'}],
            'import': [],
            'var': [{'name': '__doc__', 'type': 'NoneType', 'value': None}, {'name': '__module__', 'type': 'str', 'value': 'uiPrivateShopSearch'}, {'name': '__qualname__', 'type': 'str', 'value': 'CheckBox'}]},
           {'class': [],
            'func': [{'args': ['self'], 'defaults': [], 'name': 'Buy'},
                     {'args': ['self'], 'defaults': [], 'name': 'Close'},
                     {'args': ['self'], 'defaults': [], 'name': 'Destroy'},
                     {'args': ['self'], 'defaults': [], 'name': 'HidePageButton'},
                     {'args': ['self', 'n'], 'defaults': [], 'name': 'NumberToMoneyString'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnBuyAcceptEvent'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnBuyCloseEvent'},
                     {'args': ['self', 'Masksubtypenumber'], 'defaults': [], 'name': 'OnChangeItemSubTypeSlot'},
                     {'args': ['self', 'Masktypenumber'], 'defaults': [], 'name': 'OnChangeItemTypeSlot'},
                     {'args': ['self', 'jobnumber'], 'defaults': [], 'name': 'OnChangeJobSlot'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnPressEscapeKey'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnTop'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnUpdate'},
                     {'args': ['self', 'iscash'], 'defaults': [], 'name': 'Open'},
                     {'args': ['self', 'slotIndex'], 'defaults': [], 'name': 'OverInToolTip'},
                     {'args': ['self', 'slotIndex'], 'defaults': [], 'name': 'OverOutToolTip'},
                     {'args': ['self', 'number'], 'defaults': [], 'name': 'Pagebutton'},
                     {'args': ['self'], 'defaults': [], 'name': 'RefreshList'},
                     {'args': ['self'], 'defaults': [], 'name': 'Search'},
                     {'args': ['self', 'tooltip'], 'defaults': [], 'name': 'SetItemToolTip'},
                     {'args': ['self', 'maxsize', 'page'], 'defaults': [], 'name': 'ShowPageButton'},
                     {'args': ['self'], 'defaults': [], 'name': '__ClearItemSlotButtonList'},
                     {'args': ['self'], 'defaults': [], 'name': '__LoadWindow'},
                     {'args': ['self'], 'defaults': [], 'name': '__MakeResultSlot'},
                     {'args': ['self', 'arg'], 'defaults': [], 'name': '__SelectItem'},
                     {'args': ['self', 'index'], 'defaults': [], 'name': '__SelectItemSlotButtonList'},
                     {'args': ['self', 'slotIndex'], 'defaults': [], 'name': '__ShowToolTip'},
                     {'args': ['self'], 'defaults': [], 'name': '__del__'},
                     {'args': ['self'], 'defaults': [], 'name': '__init__'},
                     {'args': ['self'], 'defaults': [], 'name': 'clearEffectEtc'},
                     {'args': ['self'], 'defaults': [], 'name': 'clearPagebuttoncolor'},
                     {'args': ['self'], 'defaults': [], 'name': 'firstprevbutton'},
                     {'args': ['self'], 'defaults': [], 'name': 'lastnextbutton'},
                     {'args': ['self'], 'defaults': [], 'name': 'nextbutton'},
                     {'args': ['self'], 'defaults': [], 'name': 'prevbutton'}],
            'import': [],
            'var': [{'name': 'ARMOR_MASK_SUBTYPE_DIC', 'type': 'dict', 'value': {0: 'Armour', 1: 'Helmets', 2: 'Shields'}},
                    {'name': 'CLICK_LIMIT_TIME', 'type': 'int', 'value': 3},
                    {'name': 'COSTUMES_MASK_SUBTYPE_DIC', 'type': 'dict', 'value': {0: 'Weapon Skins', 1: 'Costumes', 2: 'Hairstyles', 3: 'Shoulder Sashes', 4: 'Other'}},
                    {'name': 'DRAGON_STONE_MASK_SUBTYPE_DIC', 'type': 'dict', 'value': {0: 'Diamond', 1: 'Ruby', 2: 'Jade', 3: 'Sapphire', 4: 'Garnet', 5: 'Onyx', 6: 'Other'}},
                    {'name': 'ETC_MASK_SUBTYPE_DIC', 'type': 'dict', 'value': {0: 'Chests | Boxes', 1: 'Marriage', 2: 'Event Items', 3: 'Soulbinding', 4: 'Art of War Books', 5: 'Polymorph Marbles', 6: 'Potion Production', 7: 'Other'}},
                    {'name': 'FISHING_PICK_MASK_SUBTYPE_DIC', 'type': 'dict', 'value': {0: 'Fishing Rods', 1: 'Pickaxes', 2: 'Fish', 3: 'Ores', 4: 'Other'}},
                    {'name': 'ITEM_MASK_MASK_SUBTYPE_DICS',
                     'type': 'dict',
                     'value': {1: {0: 'Mounts', 1: 'Pets', 2: 'Evolvable Pets', 3: 'Pet Eggs'},
                               2: {0: {0: 'One-handed Weapons', 3: 'Two-handed Weapons'}, 1: {0: 'One-handed Weapons', 1: 'Daggers', 2: 'Bows', 8: 'Arrows', 9: 'Quivers'}, 2: {0: 'One-handed Weapons'}, 3: {4: 'Bells', 6: 'Fans'}, 4: {5: 'Claws'}},
                               3: {0: 'Armour', 1: 'Helmets', 2: 'Shields'},
                               4: {0: 'Bracelets', 1: 'Shoes', 2: 'Necklaces', 3: 'Earrings', 4: 'Belts'},
                               5: {0: 'Materials', 1: 'Spirit Stones', 2: 'Other'},
                               6: {0: 'Consumables', 1: 'Hair Dyes', 2: 'Other'},
                               7: {0: 'Fishing Rods', 1: 'Pickaxes', 2: 'Fish', 3: 'Ores', 4: 'Other'},
                               8: {0: 'Diamond', 1: 'Ruby', 2: 'Jade', 3: 'Sapphire', 4: 'Garnet', 5: 'Onyx', 6: 'Other'},
                               9: {0: 'Weapon Skins', 1: 'Costumes', 2: 'Hairstyles', 3: 'Shoulder Sashes', 4: 'Other'},
                               10: {0: 'Ward | Boost', 1: 'Skill Books', 2: 'Books of Forgetfulness', 3: 'Other'},
                               11: {0: 'Consumables', 1: 'Other'},
                               12: {0: 'Chests | Boxes', 1: 'Marriage', 2: 'Event Items', 3: 'Soulbinding', 4: 'Art of War Books', 5: 'Polymorph Marbles', 6: 'Potion Production', 7: 'Other'}}},
                    {'name': 'ITEM_MASK_TYPE_DIC', 'type': 'dict', 'value': {1: 'Mounts | Pets', 2: 'Weapons', 3: 'Equipment', 4: 'Jewellery', 5: 'Upgrades', 6: 'Potions', 7: 'Fishing | Mining', 8: 'Dragon Stone Alchemy', 9: 'Costumes', 10: 'Skills', 11: 'Special Items', 12: 'Other'}},
                    {'name': 'JEWELRY_MASK_SUBTYPE_DIC', 'type': 'dict', 'value': {0: 'Bracelets', 1: 'Shoes', 2: 'Necklaces', 3: 'Earrings', 4: 'Belts'}},
                    {'name': 'JOB_MAX_COUNT', 'type': 'int', 'value': 5},
                    {'name': 'JOB_NAME_DIC', 'type': 'dict', 'value': {0: 'Warrior', 1: 'Ninja', 2: 'Sura', 3: 'Shaman', 4: 'Lycan'}},
                    {'name': 'MAX_CHAR_LEVEL', 'type': 'int', 'value': 105},
                    {'name': 'MAX_LINE_COUNT', 'type': 'int', 'value': 10},
                    {'name': 'MOUNT_PET_MASK_SUBTYPE_DIC', 'type': 'dict', 'value': {0: 'Mounts', 1: 'Pets', 2: 'Evolvable Pets', 3: 'Pet Eggs'}},
                    {'name': 'PAGEBUTTON_MAX_SIZE', 'type': 'int', 'value': 9},
                    {'name': 'PAGEBUTTON_NUMBER_SIZE', 'type': 'int', 'value': 5},
                    {'name': 'PAGEONE_MAX_SIZE', 'type': 'int', 'value': 50},
                    {'name': 'POTION_MASK_SUBTYPE_DIC', 'type': 'dict', 'value': {0: 'Consumables', 1: 'Hair Dyes', 2: 'Other'}},
                    {'name': 'SKILL_MASK_SUBTYPE_DIC', 'type': 'dict', 'value': {0: 'Ward | Boost', 1: 'Skill Books', 2: 'Books of Forgetfulness', 3: 'Other'}},
                    {'name': 'SPECIAL_TITLE_COLOR', 'type': 'long', 'value': 4283317552L},
                    {'name': 'TUNING_MASK_SUBTYPE_DIC', 'type': 'dict', 'value': {0: 'Materials', 1: 'Spirit Stones', 2: 'Other'}},
                    {'name': 'UNIQUE_MASK_SUBTYPE_DIC', 'type': 'dict', 'value': {0: 'Consumables', 1: 'Other'}},
                    {'name': 'WEAPON_MASK_SUBTYPE_DIC', 'type': 'dict', 'value': {0: {0: 'One-handed Weapons', 3: 'Two-handed Weapons'}, 1: {0: 'One-handed Weapons', 1: 'Daggers', 2: 'Bows', 8: 'Arrows', 9: 'Quivers'}, 2: {0: 'One-handed Weapons'}, 3: {4: 'Bells', 6: 'Fans'}, 4: {5: 'Claws'}}},
                    {'name': '__doc__', 'type': 'NoneType', 'value': None},
                    {'name': '__module__', 'type': 'str', 'value': 'uiPrivateShopSearch'},
                    {'name': '__qualname__', 'type': 'str', 'value': 'PrivateShopSeachWindow'}]},
           {'class': [],
            'func': [{'args': ['self'], 'defaults': [], 'name': 'Disable'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnMouseLeftButtonDown'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnMouseLeftButtonUp'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnMouseOverIn'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnMouseOverOut'},
                     {'args': ['self', 'event', 'arg'], 'defaults': [], 'name': 'SetEvent'},
                     {'args': ['self', 'text'], 'defaults': [], 'name': 'SetText'},
                     {'args': ['self'], 'defaults': [], 'name': '__del__'},
                     {'args': ['self', 'parent', 'x', 'y'], 'defaults': [], 'name': '__init__'}],
            'import': [],
            'var': [{'name': '__doc__', 'type': 'NoneType', 'value': None}, {'name': '__module__', 'type': 'str', 'value': 'uiPrivateShopSearch'}, {'name': '__qualname__', 'type': 'str', 'value': 'ActionTextSlot'}]},
           {'class': [],
            'func': [{'args': ['self'], 'defaults': [], 'name': 'Down'}, {'args': ['self'], 'defaults': [], 'name': 'OnRender'}, {'args': ['self'], 'defaults': [], 'name': 'Up'}, {'args': ['self'], 'defaults': [], 'name': '__del__'}, {'args': ['self', 'parent'], 'defaults': [], 'name': '__init__'}],
            'import': [],
            'var': [{'name': '__doc__', 'type': 'NoneType', 'value': None}, {'name': '__module__', 'type': 'str', 'value': 'uiPrivateShopSearch'}, {'name': '__qualname__', 'type': 'str', 'value': 'MouseReflector'}]}],
 'func': [{'args': ['bad-module'], 'defaults': ['bad-module'], 'name': 'proxy'}],
 'import': ['shop', 'uiCommon', 'grp', '__builtin__', 'chatm2g', 'app', 'item', 'm2netm2g', 'playerm2g2', 'ui', 'background', 'localeInfo'],
 'var': [{'name': '__doc__', 'type': 'NoneType', 'value': None}, {'name': '__name__', 'type': 'str', 'value': 'uiPrivateShopSearch'}, {'name': '__package__', 'type': 'NoneType', 'value': None}, {'name': '__test__', 'type': 'dict', 'value': {}}]}
