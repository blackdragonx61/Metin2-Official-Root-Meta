{'class': [{'class': [],
            'func': [{'args': ['self', 'pet_id', 'slot', 'index'], 'defaults': [], 'name': 'SetPetSkill'},
                     {'args': ['self', 'pet_skill_vnum', 'value1', 'value2', 'color'], 'defaults': [], 'name': '__AppendAutoSkill'},
                     {'args': ['self', 'pet_skill_cool_time', 'color'], 'defaults': [], 'name': '__AppendCoolTime'},
                     {'args': ['self', 'curLevel', 'maxLevel'], 'defaults': [], 'name': '__AppendNextLevel'},
                     {'args': ['self', 'pet_skill_vnum', 'value', 'color'], 'defaults': [], 'name': '__AppendPassiveSkill'},
                     {'args': ['self'], 'defaults': [], 'name': '__AppendRemainsTime'},
                     {'args': ['self', 'pet_skill_vnum', 'value'], 'defaults': [], 'name': '__PassiveSkillExceptionDecsriptionValueChange'},
                     {'args': ['self'], 'defaults': [], 'name': '__del__'},
                     {'args': ['self'], 'defaults': [], 'name': '__init__'}],
            'import': [],
            'var': [{'name': 'PET_SKILL_APPLY_DATA_DICT',
                     'type': 'dict',
                     'value': {1: <cyfunction SA.<locals>.f at 0x07D9C088>,
                               2: <cyfunction SA.<locals>.f at 0x07D97F50>,
                               3: <cyfunction SA.<locals>.f at 0x07D97D40>,
                               4: <cyfunction SA.<locals>.f at 0x07D97EF8>,
                               5: <cyfunction SA.<locals>.f at 0x07D9C138>,
                               6: <cyfunction SA.<locals>.f at 0x07D9D3F8>,
                               7: <cyfunction SA.<locals>.f at 0x07D9D870>,
                               8: <cyfunction SA.<locals>.f at 0x07D9C5B0>,
                               9: <cyfunction SA.<locals>.f at 0x07D97B30>,
                               10: <cyfunction SAA.<locals>.f at 0x07D79AD8>,
                               11: <cyfunction SA.<locals>.f at 0x07D9C298>,
                               12: <cyfunction SA.<locals>.f at 0x07D9C2F0>,
                               13: <cyfunction SA.<locals>.f at 0x07D97500>,
                               14: <cyfunction SA.<locals>.f at 0x07D97CE8>,
                               15: <cyfunction SA.<locals>.f at 0x07D9CFA8>,
                               16: <cyfunction SA.<locals>.f at 0x07D9C558>,
                               17: <cyfunction SAA.<locals>.f at 0x07D79B30>,
                               18: <cyfunction SAN.<locals>.f at 0x07D79B88>}},
                    {'name': 'PET_SKILL_TOOL_TIP_WIDTH', 'type': 'int', 'value': 255},
                    {'name': '__doc__', 'type': 'NoneType', 'value': None},
                    {'name': '__module__', 'type': 'str', 'value': 'uiToolTip'},
                    {'name': '__qualname__', 'type': 'str', 'value': 'PetSkillToolTip'}]},
           {'class': [],
            'func': [{'args': ['self'], 'defaults': [], 'name': 'OnMouseLeftButtonDown'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnUpdate'},
                     {'args': ['self', 'tokens'], 'defaults': [], 'name': 'SetHyperlinkItem'},
                     {'args': ['self', 'tokens'], 'defaults': [], 'name': 'SetHyperlinkPetItem'},
                     {'args': ['self'], 'defaults': [], 'name': '__del__'},
                     {'args': ['self'], 'defaults': [], 'name': '__init__'}],
            'import': [],
            'var': [{'name': '__doc__', 'type': 'NoneType', 'value': None}, {'name': '__module__', 'type': 'str', 'value': 'uiToolTip'}, {'name': '__qualname__', 'type': 'str', 'value': 'HyperlinkItemToolTip'}]},
           {'class': [],
            'func': [{'args': ['self', 'itemVnum', 'metinSlot', 'attrSlot', 'pet_info'], 'defaults': [], 'name': 'AddHyperLinkPetItemData'},
                     {'args': ['self', 'itemVnum', 'metinSlot', 'attrSlot', 'flags', 'unbindTime', 'window_type', 'slotIndex'], 'defaults': [0, 0, 0, 1, -1], 'name': 'AddItemData'},
                     {'args': ['self', 'itemVnum', 'itemDesc', 'itemSummary', 'metinSlot', 'attrSlot'], 'defaults': [], 'name': 'AddItemData_Offline'},
                     {'args': ['self', 'itemVnum', 'metinSlot', 'attrSlot'], 'defaults': [0], 'name': 'AddRefineItemData'},
                     {'args': ['self', 'type', 'slotIndex'], 'defaults': [], 'name': 'AppendChangeLookInfoExchangeWIndow'},
                     {'args': ['self', 'changelookvnum'], 'defaults': [], 'name': 'AppendChangeLookInfoItemVnum'},
                     {'args': ['self', 'slotIndex'], 'defaults': [], 'name': 'AppendChangeLookInfoPrivateShopWIndow'},
                     {'args': ['self', 'slotIndex'], 'defaults': [], 'name': 'AppendChangeLookInfoShopWIndow'},
                     {'args': ['self', 'window_type', 'slotIndex'], 'defaults': [], 'name': 'AppendChangeLookInformation'},
                     {'args': ['self', 'endTime'], 'defaults': [], 'name': 'AppendMallItemLastTime'},
                     {'args': ['self'], 'defaults': [], 'name': 'AppendMetinInformation'},
                     {'args': ['self'], 'defaults': [], 'name': 'AppendMetinWearInformation'},
                     {'args': ['self', 'endTime'], 'defaults': [], 'name': 'AppendPetItemLastTime'},
                     {'args': ['self', 'price', 'cheque'], 'defaults': [0], 'name': 'AppendPrice'},
                     {'args': ['self', 'price', 'coinType'], 'defaults': [], 'name': 'AppendPriceBySecondaryCoin'},
                     {'args': ['self', 'item', 'metinSlot', 'limitIndex'], 'defaults': [], 'name': 'AppendRealTimeStartFirstUseLastTime'},
                     {'args': ['self', 'price', 'cheque', 'isPrivateShopBuilder'], 'defaults': [0, False], 'name': 'AppendSellingPrice'},
                     {'args': ['self', 'text', 'color', 'centerAlign'], 'defaults': [-4079167, True], 'name': 'AppendTextLine'},
                     {'args': ['self', 'text', 'color', 'centerAlign'], 'defaults': [-4079167, True], 'name': 'AppendTextLineAcce'},
                     {'args': ['self', 'metinSlot'], 'defaults': [], 'name': 'AppendTimerBasedOnWearLastTime'},
                     {'args': ['self', 'restMin'], 'defaults': [], 'name': 'AppendUniqueItemLastTime'},
                     {'args': ['self'], 'defaults': [], 'name': 'AppendWearableInformation'},
                     {'args': ['self'], 'defaults': [], 'name': 'CanEquip'},
                     {'args': ['self'], 'defaults': [], 'name': 'ClearToolTip'},
                     {'args': ['self', 'affectType', 'affectValue'], 'defaults': [], 'name': 'GetAffectString'},
                     {'args': ['self', 'number'], 'defaults': [], 'name': 'GetMetinItemIndex'},
                     {'args': ['self', 'number'], 'defaults': [], 'name': 'GetMetinSocketType'},
                     {'args': ['self', 'price'], 'defaults': [], 'name': 'GetPriceColor'},
                     {'args': ['self', 'slotIndex'], 'defaults': [], 'name': 'SetAcceWindowItem'},
                     {'args': ['self', 'itemVnum'], 'defaults': [], 'name': 'SetAttendanceRewardItem'},
                     {'args': ['self', 'enable'], 'defaults': [], 'name': 'SetCannotUseItemForceSetDisableColor'},
                     {'args': ['self', 'slotIndex'], 'defaults': [], 'name': 'SetChangeLookWindowItem'},
                     {'args': ['self', 'slotIndex'], 'defaults': [], 'name': 'SetExchangeOwnerItem'},
                     {'args': ['self', 'slotIndex'], 'defaults': [], 'name': 'SetExchangeTargetItem'},
                     {'args': ['self', 'slotIndex'], 'defaults': [], 'name': 'SetGuildBankItem'},
                     {'args': ['self', 'slotIndex', 'window_type'], 'defaults': [1], 'name': 'SetInventoryItem'},
                     {'args': ['self', 'itemVnum'], 'defaults': [], 'name': 'SetItemToolTip'},
                     {'args': ['self', 'slotIndex'], 'defaults': [], 'name': 'SetMallItem'},
                     {'args': ['self', 'slotIndex'], 'defaults': [], 'name': 'SetPrivateSearchItem'},
                     {'args': ['self', 'invenType', 'invenPos', 'privateShopSlotIndex'], 'defaults': [], 'name': 'SetPrivateShopBuilderItem'},
                     {'args': ['self', 'baseSlotIndex', 'materialSlotIndex', 'window_type'], 'defaults': [1], 'name': 'SetResulItemAttrMove'},
                     {'args': ['self', 'slotIndex'], 'defaults': [], 'name': 'SetSafeBoxItem'},
                     {'args': ['self', 'slotIndex'], 'defaults': [], 'name': 'SetShopItem'},
                     {'args': ['self', 'slotIndex', 'cointype'], 'defaults': [], 'name': 'SetShopItemBySecondaryCoin'},
                     {'args': ['self', 'attrSlot'], 'defaults': [], 'name': '__AdjustAttrMaxWidth'},
                     {'args': ['self', 'desc'], 'defaults': [], 'name': '__AdjustDescMaxWidth'},
                     {'args': ['self', 'attrSlot', 'desc'], 'defaults': [], 'name': '__AdjustMaxWidth'},
                     {'args': ['self'], 'defaults': [], 'name': '__AppendAbilityPotionInformation'},
                     {'args': ['self', 'oriitemVnum', 'window_type', 'slotIndex', 'metinSlot'], 'defaults': [], 'name': '__AppendAcceItemAffectInformation'},
                     {'args': ['self', 'metinSlot', 'mtrlVnum'], 'defaults': [], 'name': '__AppendAccessoryMetinSlotInfo'},
                     {'args': ['self'], 'defaults': [], 'name': '__AppendAffectInformation'},
                     {'args': ['self', 'slotIndex', 'window_type', 'metinSlot'], 'defaults': [], 'name': '__AppendAffectInformationAcce'},
                     {'args': ['self'], 'defaults': [], 'name': '__AppendAttackGradeInfo'},
                     {'args': ['self'], 'defaults': [], 'name': '__AppendAttackPowerInfo'},
                     {'args': ['self', 'item'], 'defaults': [], 'name': '__AppendAttackSpeedInfo'},
                     {'args': ['self', 'itemVnum'], 'defaults': [], 'name': '__AppendAttendanceRewardItemicon'},
                     {'args': ['self', 'attrSlot'], 'defaults': [], 'name': '__AppendAttributeInformation'},
                     {'args': ['self', 'itemVnum', 'attrSlot', 'slotIndex', 'window_type', 'metinSlot'], 'defaults': [], 'name': '__AppendAttributeInformationAcce'},
                     {'args': ['self', 'size'], 'defaults': [], 'name': '__AppendFishInfo'},
                     {'args': ['self', 'itemVnum'], 'defaults': [], 'name': '__AppendHairIcon'},
                     {'args': ['self'], 'defaults': [], 'name': '__AppendLimitInformation'},
                     {'args': ['self'], 'defaults': [], 'name': '__AppendMagicAttackInfo'},
                     {'args': ['self'], 'defaults': [], 'name': '__AppendMagicDefenceInfo'},
                     {'args': ['self', 'metinSlot'], 'defaults': [], 'name': '__AppendMetinSlotInfo'},
                     {'args': ['self', 'index', 'metinSlotData', 'custumAffectString', 'custumAffectString2', 'leftTime'], 'defaults': ['', '', 0], 'name': '__AppendMetinSlotInfo_AppendMetinSocketData'},
                     {'args': ['self', 'metinSlot'], 'defaults': [], 'name': '__AppendMetinSlotInfo_IsEmptySlotList'},
                     {'args': ['self', 'mobVnum'], 'defaults': [], 'name': '__AppendMonsterCardItemIcon'},
                     {'args': ['self', 'metinSlot'], 'defaults': [], 'name': '__AppendPetBagItemInfomation'},
                     {'args': ['self', 'metinSlot', 'isFeedWindow'], 'defaults': [False], 'name': '__AppendPetEggItemInformation'},
                     {'args': ['self', 'curLevel', 'curEXP', 'maxEXP'], 'defaults': [], 'name': '__AppendPickInformation'},
                     {'args': ['self'], 'defaults': [], 'name': '__AppendPotionInformation'},
                     {'args': ['self', 'itemVnum'], 'defaults': [], 'name': '__AppendPrivateSearchItemicon'},
                     {'args': ['self', 'itemVnum', 'endTime'], 'defaults': [], 'name': '__AppendRealTimeToolTip'},
                     {'args': ['self', 'curLevel', 'curEXP', 'maxEXP'], 'defaults': [], 'name': '__AppendRodInformation'},
                     {'args': ['self', 'window_type', 'slotIndex'], 'defaults': [], 'name': '__AppendSealInformation'},
                     {'args': ['self', 'metinSlot'], 'defaults': [], 'name': '__AppendUpBringingPetItemInfomation'},
                     {'args': ['self', 'dwVnum'], 'defaults': [], 'name': '__DragonSoulInfoString'},
                     {'args': ['self', 'affectType', 'affectValue'], 'defaults': [], 'name': '__GetAffectString'},
                     {'args': ['self', 'index', 'value'], 'defaults': [], 'name': '__GetAttributeColor'},
                     {'args': ['self', 'evol_level'], 'defaults': [], 'name': '__GetEvolName'},
                     {'args': ['self', 'attrSlot'], 'defaults': [], 'name': '__IsAttr'},
                     {'args': ['self', 'itemVnum'], 'defaults': [], 'name': '__IsCostumeHair'},
                     {'args': ['self', 'itemVnum'], 'defaults': [], 'name': '__IsHair'},
                     {'args': ['self', 'itemVnum'], 'defaults': [], 'name': '__IsNewHair'},
                     {'args': ['self', 'itemVnum'], 'defaults': [], 'name': '__IsNewHair2'},
                     {'args': ['self', 'itemVnum'], 'defaults': [], 'name': '__IsNewHair3'},
                     {'args': ['self', 'itemVnum'], 'defaults': [], 'name': '__IsOldHair'},
                     {'args': ['self', 'itemVnum'], 'defaults': [], 'name': '__IsPolymorphItem'},
                     {'args': ['self', 'itemVnum', 'metinSlot', 'attrSlot'], 'defaults': [], 'name': '__SetItemTitle'},
                     {'args': ['self'], 'defaults': [], 'name': '__SetNormalItemTitle'},
                     {'args': ['self', 'monsterVnum'], 'defaults': [], 'name': '__SetPolymorphItemTitle'},
                     {'args': ['self', 'skillIndex', 'bookName', 'skillGrade'], 'defaults': [], 'name': '__SetSkillBookToolTip'},
                     {'args': ['self'], 'defaults': [], 'name': '__SetSpecialItemTitle'},
                     {'args': ['self'], 'defaults': [], 'name': '__del__'},
                     {'args': ['self'], 'defaults': [], 'name': '__init__'}],
            'import': [],
            'var': [{'name': 'AFFECT_DICT',
                     'type': 'dict',
                     'value': {1: <cyfunction SA.<locals>.f at 0x07D9D240>,
                               2: <cyfunction SA.<locals>.f at 0x07D9D2F0>,
                               3: <cyfunction SA.<locals>.f at 0x07D9C608>,
                               4: <cyfunction SA.<locals>.f at 0x07D9CB30>,
                               5: <cyfunction SA.<locals>.f at 0x07D9DA80>,
                               6: <cyfunction SA.<locals>.f at 0x07D9C710>,
                               7: <cyfunction SA.<locals>.f at 0x07D9C3F8>,
                               8: <cyfunction SA.<locals>.f at 0x07D9D450>,
                               9: <cyfunction SA.<locals>.f at 0x07D9C5B0>,
                               10: <cyfunction SA.<locals>.f at 0x07D9CAD8>,
                               11: <cyfunction SA.<locals>.f at 0x07D9DA28>,
                               12: <cyfunction SA.<locals>.f at 0x07D97B88>,
                               13: <cyfunction SA.<locals>.f at 0x07D9C348>,
                               14: <cyfunction SA.<locals>.f at 0x07D9C240>,
                               15: <cyfunction SA.<locals>.f at 0x07D975B0>,
                               16: <cyfunction SA.<locals>.f at 0x07D97B30>,
                               17: <cyfunction SA.<locals>.f at 0x07D97138>,
                               18: <cyfunction SA.<locals>.f at 0x07D97030>,
                               19: <cyfunction SA.<locals>.f at 0x07D97240>,
                               20: <cyfunction SA.<locals>.f at 0x07D97190>,
                               21: <cyfunction SA.<locals>.f at 0x07D97348>,
                               22: <cyfunction SA.<locals>.f at 0x07D970E0>,
                               23: <cyfunction SA.<locals>.f at 0x07D9C298>,
                               24: <cyfunction SA.<locals>.f at 0x07D9C2F0>,
                               25: <cyfunction SA.<locals>.f at 0x07D979D0>,
                               26: <cyfunction SA.<locals>.f at 0x07D97608>,
                               27: <cyfunction SA.<locals>.f at 0x07D97500>,
                               28: <cyfunction SA.<locals>.f at 0x07D97660>,
                               29: <cyfunction SA.<locals>.f at 0x07D97FA8>,
                               30: <cyfunction SA.<locals>.f at 0x07D9C030>,
                               31: <cyfunction SA.<locals>.f at 0x07D97E48>,
                               32: <cyfunction SA.<locals>.f at 0x07D97D98>,
                               33: <cyfunction SA.<locals>.f at 0x07D97EA0>,
                               34: <cyfunction SA.<locals>.f at 0x07D9D608>,
                               35: <cyfunction SA.<locals>.f at 0x07D9D768>,
                               36: <cyfunction SA.<locals>.f at 0x07D9D710>,
                               37: <cyfunction SA.<locals>.f at 0x07D9D818>,
                               38: <cyfunction SA.<locals>.f at 0x07D9C0E0>,
                               39: <cyfunction SA.<locals>.f at 0x07D97CE8>,
                               40: <cyfunction SA.<locals>.f at 0x07D97C90>,
                               41: <cyfunction SA.<locals>.f at 0x07D97BE0>,
                               42: <cyfunction SA.<locals>.f at 0x07D97978>,
                               43: <cyfunction SA.<locals>.f at 0x07D976B8>,
                               44: <cyfunction SA.<locals>.f at 0x07D97710>,
                               45: <cyfunction SA.<locals>.f at 0x07D978C8>,
                               46: <cyfunction SA.<locals>.f at 0x07D97C38>,
                               47: <cyfunction SA.<locals>.f at 0x07D97920>,
                               48: <cyfunction SNA.<locals>.f at 0x07D97818>,
                               49: <cyfunction SNA.<locals>.f at 0x07D977C0>,
                               50: <cyfunction SNA.<locals>.f at 0x07D97768>,
                               52: <cyfunction SA.<locals>.f at 0x07D9C558>,
                               53: <cyfunction SA.<locals>.f at 0x07D9C3A0>,
                               54: <cyfunction SA.<locals>.f at 0x07D9C6B8>,
                               55: <cyfunction SA.<locals>.f at 0x07D9CBE0>,
                               56: <cyfunction SA.<locals>.f at 0x07D9CC38>,
                               58: <cyfunction SA.<locals>.f at 0x07D9D3A0>,
                               59: <cyfunction SA.<locals>.f at 0x07D973A0>,
                               60: <cyfunction SA.<locals>.f at 0x07D97088>,
                               61: <cyfunction SA.<locals>.f at 0x07D972F0>,
                               62: <cyfunction SA.<locals>.f at 0x07D97298>,
                               63: <cyfunction SA.<locals>.f at 0x07D971E8>,
                               64: <cyfunction SA.<locals>.f at 0x07D9CC90>,
                               65: <cyfunction SA.<locals>.f at 0x07D9CD98>,
                               66: <cyfunction SA.<locals>.f at 0x07D9CE48>,
                               67: <cyfunction SA.<locals>.f at 0x07D9D088>,
                               68: <cyfunction SA.<locals>.f at 0x07D9CFA8>,
                               69: <cyfunction SA.<locals>.f at 0x07D97A28>,
                               70: <cyfunction SA.<locals>.f at 0x07D97A80>,
                               71: <cyfunction SA.<locals>.f at 0x07D9D978>,
                               72: <cyfunction SA.<locals>.f at 0x07D9D4A8>,
                               73: <cyfunction SA.<locals>.f at 0x07D9D9D0>,
                               74: <cyfunction SA.<locals>.f at 0x07D9D500>,
                               76: <cyfunction SA.<locals>.f at 0x07D9CEA0>,
                               77: <cyfunction SA.<locals>.f at 0x07D9D0E0>,
                               78: <cyfunction SA.<locals>.f at 0x07D9C088>,
                               79: <cyfunction SA.<locals>.f at 0x07D97D40>,
                               80: <cyfunction SA.<locals>.f at 0x07D97F50>,
                               81: <cyfunction SA.<locals>.f at 0x07D97EF8>,
                               82: <cyfunction SA.<locals>.f at 0x07D9C818>,
                               84: <cyfunction SA.<locals>.f at 0x07D9C660>,
                               85: <cyfunction SA.<locals>.f at 0x07D9CB88>,
                               86: <cyfunction SA.<locals>.f at 0x07D9D3F8>,
                               87: <cyfunction SA.<locals>.f at 0x07D9D7C0>,
                               88: <cyfunction SA.<locals>.f at 0x07D9D6B8>,
                               89: <cyfunction SA.<locals>.f at 0x07D9D660>,
                               90: <cyfunction SA.<locals>.f at 0x07D79EF8>,
                               91: <cyfunction SA.<locals>.f at 0x07D79F50>,
                               92: <cyfunction SA.<locals>.f at 0x07D974A8>,
                               93: <cyfunction SA.<locals>.f at 0x07D97450>,
                               94: <cyfunction SA.<locals>.f at 0x07D973F8>,
                               95: <cyfunction SA.<locals>.f at 0x07D9C138>,
                               96: <cyfunction SA.<locals>.f at 0x07D97DF0>,
                               97: <cyfunction SA.<locals>.f at 0x07D79FA8>,
                               98: <cyfunction SA.<locals>.f at 0x07D9D870>}},
                    {'name': 'ANTI_FLAG_DICT', 'type': 'dict', 'value': {0: 4, 1: 8, 2: 16, 3: 32, 4: 262144}},
                    {'name': 'ATTRIBUTE_NEED_WIDTH', 'type': 'dict', 'value': {23: 230, 24: 230, 25: 230, 26: 220, 27: 210, 35: 210, 36: 210, 37: 210, 38: 210, 39: 210, 40: 210, 41: 210, 42: 220, 43: 230, 45: 230}},
                    {'name': 'CHARACTER_COUNT', 'type': 'int', 'value': 5},
                    {'name': 'CHARACTER_NAMES', 'type': 'tuple', 'value': ('Krieger', 'Ninja', 'Sura', 'Schamane', 'Lykaner')},
                    {'name': 'FONT_COLOR', 'type': 'int', 'value': -4079167},
                    {'name': 'WEAR_COUNT', 'type': 'int', 'value': 10},
                    {'name': 'WEAR_NAMES', 'type': 'tuple', 'value': ('R\xfcstung', 'Helm', 'Schuhe', 'Armband', 'Waffe', 'Halskette', 'Ohrring', 'Einzigartig', 'Schild', 'Pfeil')},
                    {'name': '__doc__', 'type': 'NoneType', 'value': None},
                    {'name': '__module__', 'type': 'str', 'value': 'uiToolTip'},
                    {'name': '__qualname__', 'type': 'str', 'value': 'ItemToolTip'}]},
           {'class': [],
            'func': [{'args': ['self', 'skillIndex', 'skillGrade'], 'defaults': [0], 'name': 'AppendDefaultData'},
                     {'args': ['self', 'skillIndex', 'skillLevel'], 'defaults': [], 'name': 'AppendGuildSkillData'},
                     {'args': ['self', 'index', 'desc', 'color'], 'defaults': [], 'name': 'AppendMasterAffectDescription'},
                     {'args': ['self', 'needSP', 'continuationSP', 'color'], 'defaults': [], 'name': 'AppendNeedHP'},
                     {'args': ['self', 'needSP', 'continuationSP', 'color'], 'defaults': [], 'name': 'AppendNeedSP'},
                     {'args': ['self', 'index', 'desc'], 'defaults': [], 'name': 'AppendNextAffectDescription'},
                     {'args': ['self', 'skillGrade', 'skillLevel'], 'defaults': [], 'name': 'AppendPartySkillData'},
                     {'args': ['self', 'skillIndex'], 'defaults': [], 'name': 'AppendSkillConditionData'},
                     {'args': ['self', 'slotIndex', 'skillIndex', 'skillGrade', 'skillLevel', 'skillCurrentPercentage', 'skillNextPercentage'], 'defaults': [], 'name': 'AppendSkillDataNew'},
                     {'args': ['self', 'skillIndex', 'skillPercentage', 'color'], 'defaults': [], 'name': 'AppendSkillLevelDescriptionNew'},
                     {'args': ['self', 'skillIndex', 'skillLevel'], 'defaults': [], 'name': 'AppendSkillRequirement'},
                     {'args': ['self', 'skillIndex', 'skillGrade', 'skillLevel', 'maxLevel'], 'defaults': [], 'name': 'AppendSupportSkillDefaultData'},
                     {'args': ['self', 'skillIndex', 'skillLevel'], 'defaults': [], 'name': 'HasSkillLevelDescription'},
                     {'args': ['self', 'skillIndex', 'skillLevel'], 'defaults': [-1], 'name': 'SetSkill'},
                     {'args': ['self', 'slotIndex', 'skillIndex', 'skillGrade', 'skillLevel'], 'defaults': [], 'name': 'SetSkillNew'},
                     {'args': ['self', 'slotIndex', 'skillIndex', 'skillGrade'], 'defaults': [], 'name': 'SetSkillOnlyName'},
                     {'args': ['self', 'skillIndex', 'skillGrade'], 'defaults': [], 'name': '__AppendSkillGradeName'},
                     {'args': ['self', 'skillLevel', 'color'], 'defaults': [], 'name': '__AppendSummonDescription'},
                     {'args': ['self', 'skillIndex', 'skillGrade'], 'defaults': [], 'name': '__SetSkillTitle'},
                     {'args': ['self'], 'defaults': [], 'name': '__del__'},
                     {'args': ['self'], 'defaults': [], 'name': '__init__'}],
            'import': [],
            'var': [{'name': 'AFFECT_APPEND_TEXT_DICT', 'type': 'dict', 'value': {'DODGE': '%', 'REFLECT_MELEE': '%', 'RESIST_NORMAL': '%'}},
                    {'name': 'AFFECT_NAME_DICT',
                     'type': 'dict',
                     'value': {'ATT_GRADE': 'Angriffswert: +',
                               'ATT_SPEED': 'Angriffsgeschwindigkeit: +',
                               'DEF_GRADE': 'Verteidigung:',
                               'DODGE': 'Gegnerischer Angriffswert: -',
                               'HP': 'Angriffswert:',
                               'MOV_SPEED': 'Bewegungsgeschwindigkeit: +',
                               'REFLECT_MELEE': 'Chance, Nahkampf-Angriff zu reflektieren:',
                               'RESIST_NORMAL': 'Widerstand gegen k\xf6rperlichen Schaden:'}},
                    {'name': 'PARTY_SKILL_ATTACKER_AFFECT_LIST', 'type': 'tuple', 'value': ((36, 3), (26, 1), (32, 2))},
                    {'name': 'PARTY_SKILL_EXPERIENCE_AFFECT_LIST', 'type': 'tuple', 'value': ((2, 2, 10), (8, 3, 20), (14, 4, 30), (22, 5, 45), (28, 6, 60), (34, 7, 80), (38, 8, 100))},
                    {'name': 'PARTY_SKILL_PLUS_GRADE_AFFECT_LIST', 'type': 'tuple', 'value': ((4, 2, 1, 0), (10, 3, 2, 0), (16, 4, 2, 1), (24, 5, 2, 2))},
                    {'name': 'PARTY_SKILL_TOOL_TIP_WIDTH', 'type': 'int', 'value': 340},
                    {'name': 'POINT_NAME_DICT', 'type': 'dict', 'value': {1: 'Level', 15: 'Intelligenz'}},
                    {'name': 'SKILL_GRADE_NAME', 'type': 'dict', 'value': {1: '%s Meister', 2: '%s Gro\xdfmeister', 3: '%s Perfekter Meister'}},
                    {'name': 'SKILL_TOOL_TIP_WIDTH', 'type': 'int', 'value': 200},
                    {'name': '__doc__', 'type': 'NoneType', 'value': None},
                    {'name': '__module__', 'type': 'str', 'value': 'uiToolTip'},
                    {'name': '__qualname__', 'type': 'str', 'value': 'SkillToolTip'}]},
           {'class': [],
            'func': [{'args': ['self'], 'defaults': [], 'name': 'AlignHorizonalCenter'},
                     {'args': ['self', 'desc', 'limit', 'color'], 'defaults': [-4079167], 'name': 'AppendDescription'},
                     {'args': ['self'], 'defaults': [], 'name': 'AppendHorizontalLine'},
                     {'args': ['self', 'size'], 'defaults': [], 'name': 'AppendSpace'},
                     {'args': ['self', 'text', 'color', 'centerAlign'], 'defaults': [-4079167, True], 'name': 'AppendTextLine'},
                     {'args': ['self', 'text', 'color', 'centerAlign'], 'defaults': [-4079167, True], 'name': 'AutoAppendTextLine'},
                     {'args': ['self'], 'defaults': [], 'name': 'ClearToolTip'},
                     {'args': ['self', 'value', 'isSpecial'], 'defaults': [False], 'name': 'GetChangeTextLineColor'},
                     {'args': ['self', 'curValue', 'limitValue'], 'defaults': [], 'name': 'GetLimitTextLineColor'},
                     {'args': ['self'], 'defaults': [], 'name': 'HideToolTip'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnUpdate'},
                     {'args': ['self'], 'defaults': [], 'name': 'ResizeToolTip'},
                     {'args': ['self', 'fontName'], 'defaults': [], 'name': 'SetDefaultFontName'},
                     {'args': ['self', 'flag'], 'defaults': [], 'name': 'SetFollow'},
                     {'args': ['self', 'width', 'height'], 'defaults': [12], 'name': 'SetThinBoardSize'},
                     {'args': ['self', 'name'], 'defaults': [], 'name': 'SetTitle'},
                     {'args': ['self', 'x', 'y'], 'defaults': [-1, -1], 'name': 'SetToolTipPosition'},
                     {'args': ['self'], 'defaults': [], 'name': 'ShowToolTip'},
                     {'args': ['self', 'description', 'characterLimitation', 'color'], 'defaults': [-4079167], 'name': '__AppendDescription_EasternLanguage'},
                     {'args': ['self', 'desc', 'color'], 'defaults': [-4079167], 'name': '__AppendDescription_WesternLanguage'},
                     {'args': ['self'], 'defaults': [], 'name': '__del__'},
                     {'args': ['self', 'width', 'isPickable'], 'defaults': [190, False], 'name': '__init__'}],
            'import': [],
            'var': [{'name': 'CANNOT_LEVEL_UP_COLOR', 'type': 'int', 'value': -1738635},
                    {'name': 'CAN_LEVEL_UP_COLOR', 'type': 'long', 'value': 4287546002L},
                    {'name': 'CHANGELOOK_ITEMNAME_COLOR', 'type': 'long', 'value': 4290569564L},
                    {'name': 'CHANGELOOK_TITLE_COLOR', 'type': 'long', 'value': 4287348223L},
                    {'name': 'CONDITION_COLOR', 'type': 'long', 'value': 4290688125L},
                    {'name': 'DISABLE_COLOR', 'type': 'int', 'value': -1738635},
                    {'name': 'ENABLE_COLOR', 'type': 'int', 'value': -4079167},
                    {'name': 'FONT_COLOR', 'type': 'int', 'value': -4079167},
                    {'name': 'HIGH_PRICE_COLOR', 'type': 'int', 'value': -14592},
                    {'name': 'LOW_PRICE_COLOR', 'type': 'int', 'value': -5066062},
                    {'name': 'MIDDLE_PRICE_COLOR', 'type': 'int', 'value': -2565928},
                    {'name': 'NEED_SKILL_POINT_COLOR', 'type': 'long', 'value': 4288322779L},
                    {'name': 'NEGATIVE_COLOR', 'type': 'int', 'value': -1738635},
                    {'name': 'NORMAL_COLOR', 'type': 'int', 'value': -4079167},
                    {'name': 'POSITIVE_COLOR', 'type': 'int', 'value': -7751539},
                    {'name': 'PRICE_COLOR', 'type': 'long', 'value': 4294949229L},
                    {'name': 'SPECIAL_POSITIVE_COLOR', 'type': 'int', 'value': -5185612},
                    {'name': 'SPECIAL_POSITIVE_COLOR2', 'type': 'int', 'value': -1967391},
                    {'name': 'SPECIAL_TITLE_COLOR', 'type': 'int', 'value': -14592},
                    {'name': 'TEXT_LINE_HEIGHT', 'type': 'int', 'value': 17},
                    {'name': 'TITLE_COLOR', 'type': 'int', 'value': -923968},
                    {'name': 'TOOL_TIP_HEIGHT', 'type': 'int', 'value': 10},
                    {'name': 'TOOL_TIP_WIDTH', 'type': 'int', 'value': 190},
                    {'name': '__doc__', 'type': 'NoneType', 'value': None},
                    {'name': '__module__', 'type': 'str', 'value': 'uiToolTip'},
                    {'name': '__qualname__', 'type': 'str', 'value': 'ToolTip'}]}],
 'func': [{'args': ['desc', 'limit'], 'defaults': [], 'name': 'SplitDescription'}, {'args': ['n'], 'defaults': [], 'name': 'chop'}],
 'import': ['shop', 'app', 'dbg', 'playerm2g2', 'skill', 'constInfo', 'grp', 'chr', 'mouseModule', 'safebox', 'localeInfo', 'exchange', '__builtin__', 'background', 'wndMgr', 'item', 'uiMonsterCard', 'ui', 'guildbank', 'grpText', 'nonplayer'],
 'var': [{'name': 'DESC_DEFAULT_MAX_COLS', 'type': 'int', 'value': 26},
         {'name': 'DESC_WESTERN_MAX_COLS', 'type': 'int', 'value': 35},
         {'name': 'DESC_WESTERN_MAX_WIDTH', 'type': 'int', 'value': 220},
         {'name': 'WARP_SCROLLS', 'type': 'list', 'value': [22011, 22000, 22010]},
         {'name': '__doc__', 'type': 'NoneType', 'value': None},
         {'name': '__name__', 'type': 'str', 'value': 'uiToolTip'},
         {'name': '__package__', 'type': 'NoneType', 'value': None},
         {'name': '__test__', 'type': 'dict', 'value': {}}]}
