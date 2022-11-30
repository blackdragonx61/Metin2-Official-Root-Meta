{'class': [{'class': [],
            'func': [{'args': ['self', 'pet_id', 'slot', 'index'], 'defaults': [], 'name': 'SetPetSkill'},
                     {'args': ['self', 'pet_skill_vnum', 'value1', 'value2', 'value3', 'value4', 'color'], 'defaults': [], 'name': '__AppendAutoDamageSkill'},
                     {'args': ['self', 'pet_skill_vnum', 'value1', 'value2', 'color'], 'defaults': [], 'name': '__AppendAutoSkill'},
                     {'args': ['self', 'pet_skill_cool_time', 'color'], 'defaults': [], 'name': '__AppendCoolTime'},
                     {'args': ['self', 'curLevel', 'maxLevel'], 'defaults': [], 'name': '__AppendNextLevel'},
                     {'args': ['self', 'pet_skill_vnum', 'value', 'color'], 'defaults': [], 'name': '__AppendPassiveSkill'},
                     {'args': ['self'], 'defaults': [], 'name': '__AppendRemainsTime'},
                     {'args': ['self', 'pet_skill_vnum', 'value'], 'defaults': [], 'name': '__PassiveSkillExceptionDecsriptionValueChange'},
                     {'args': ['self'], 'defaults': [], 'name': '__del__'},
                     {'args': ['self'], 'defaults': [], 'name': '__init__'}],
            'import': [],
            'var': [{'name': 'PET_SKILL_TOOL_TIP_WIDTH', 'type': 'int', 'value': 255}, {'name': '__doc__', 'type': 'NoneType', 'value': None}, {'name': '__module__', 'type': 'str', 'value': 'uiToolTip'}, {'name': '__qualname__', 'type': 'str', 'value': 'PetSkillToolTip'}]},
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
                     {'args': ['self', 'itemVnum', 'metinSlot', 'attrSlot', 'rare_attr_slot', 'flags', 'unbindTime', 'window_type', 'slotIndex', 'refine_element', 'apply_random_list', 'set_value'], 'defaults': [0, None, 0, 0, 1, -1, None, None, 0], 'name': 'AddItemData'},
                     {'args': ['self', 'itemVnum', 'itemDesc', 'itemSummary', 'metinSlot', 'attrSlot'], 'defaults': [], 'name': 'AddItemData_Offline'},
                     {'args': ['self', 'item_vnum', 'sockets', 'attributes', 'rare_attr_slot', 'flags', 'refine_element', 'apply_random_list', 'set_value'], 'defaults': [None, 0, None, None, 0], 'name': 'AddRefineItemData'},
                     {'args': ['self', 'coin_type', 'limit_level'], 'defaults': [], 'name': 'AppendBuyLimitLevel'},
                     {'args': ['self', 'type', 'slotIndex'], 'defaults': [], 'name': 'AppendChangeLookInfoExchangeWIndow'},
                     {'args': ['self', 'changelookvnum'], 'defaults': [], 'name': 'AppendChangeLookInfoItemVnum'},
                     {'args': ['self', 'slotIndex'], 'defaults': [], 'name': 'AppendChangeLookInfoPrivateShopWIndow'},
                     {'args': ['self', 'slotIndex'], 'defaults': [], 'name': 'AppendChangeLookInfoShopWIndow'},
                     {'args': ['self', 'window_type', 'slotIndex'], 'defaults': [], 'name': 'AppendChangeLookInformation'},
                     {'args': ['self', 'count', 'purchaseCount'], 'defaults': [], 'name': 'AppendLimitedCount'},
                     {'args': ['self', 'endTime'], 'defaults': [], 'name': 'AppendMallItemLastTime'},
                     {'args': ['self'], 'defaults': [], 'name': 'AppendMetinInformation'},
                     {'args': ['self'], 'defaults': [], 'name': 'AppendMetinWearInformation'},
                     {'args': ['self', 'endTime'], 'defaults': [], 'name': 'AppendPetItemLastTime'},
                     {'args': ['self', 'price', 'cheque'], 'defaults': [0], 'name': 'AppendPrice'},
                     {'args': ['self', 'price', 'coinType'], 'defaults': [], 'name': 'AppendPriceBySecondaryCoin'},
                     {'args': ['self', 'item', 'metinSlot', 'limitIndex'], 'defaults': [], 'name': 'AppendRealTimeStartFirstUseLastTime'},
                     {'args': ['self', 'price', 'cheque', 'isPrivateShopBuilder'], 'defaults': [0, False], 'name': 'AppendSellingPrice'},
                     {'args': ['self', 'endTime'], 'defaults': [], 'name': 'AppendSoulItemLastTime'},
                     {'args': ['self', 'text', 'color', 'centerAlign'], 'defaults': [-4079167, True], 'name': 'AppendTextLine'},
                     {'args': ['self', 'text', 'color', 'centerAlign'], 'defaults': [-4079167, True], 'name': 'AppendTextLineAcce'},
                     {'args': ['self', 'text', 'color', 'centerAlign'], 'defaults': [-4079167, True], 'name': 'AppendTextLineDontCheckColor'},
                     {'args': ['self', 'metinSlot'], 'defaults': [], 'name': 'AppendTimerBasedOnWearLastTime'},
                     {'args': ['self', 'restMin'], 'defaults': [], 'name': 'AppendUniqueItemLastTime'},
                     {'args': ['self'], 'defaults': [], 'name': 'AppendWearableInformation'},
                     {'args': ['self', 'interface'], 'defaults': [], 'name': 'BindInterface'},
                     {'args': ['self'], 'defaults': [], 'name': 'CanEquip'},
                     {'args': ['self'], 'defaults': [], 'name': 'ClearToolTip'},
                     {'args': ['self', 'affectType', 'affectValue'], 'defaults': [], 'name': 'GetAffectString'},
                     {'args': ['self', 'number'], 'defaults': [], 'name': 'GetMetinItemIndex'},
                     {'args': ['self', 'number'], 'defaults': [], 'name': 'GetMetinSocketType'},
                     {'args': ['self', 'price'], 'defaults': [], 'name': 'GetPriceColor'},
                     {'args': ['self', 'real_refine_element'], 'defaults': [], 'name': 'GetRefineElement'},
                     {'args': ['self', 'window_type', 'slot_index'], 'defaults': [], 'name': 'GetRefineElementCell'},
                     {'args': ['self'], 'defaults': [], 'name': 'RefreshShopToolTip'},
                     {'args': ['self', 'slotIndex'], 'defaults': [], 'name': 'SetAcceWindowItem'},
                     {'args': ['self', 'itemVnum'], 'defaults': [], 'name': 'SetAttendanceRewardItem'},
                     {'args': ['self', 'slotIndex'], 'defaults': [], 'name': 'SetAuraWindowItem'},
                     {'args': ['self', 'enable'], 'defaults': [], 'name': 'SetCannotUseItemForceSetDisableColor'},
                     {'args': ['self', 'slotIndex'], 'defaults': [], 'name': 'SetChangeLookWindowItem'},
                     {'args': ['self', 'slotIndex'], 'defaults': [], 'name': 'SetExchangeOwnerItem'},
                     {'args': ['self', 'slotIndex'], 'defaults': [], 'name': 'SetExchangeTargetItem'},
                     {'args': ['self', 'slotIndex'], 'defaults': [], 'name': 'SetGuildBankItem'},
                     {'args': ['self', 'slotIndex', 'window_type'], 'defaults': [1], 'name': 'SetInventoryItem'},
                     {'args': ['self', 'enable'], 'defaults': [], 'name': 'SetItemPriceTextTooltip'},
                     {'args': ['self', 'itemVnum'], 'defaults': [], 'name': 'SetItemToolTip'},
                     {'args': ['self', 'index'], 'defaults': [], 'name': 'SetMailBoxItem'},
                     {'args': ['self', 'slotIndex'], 'defaults': [], 'name': 'SetMallItem'},
                     {'args': ['self', 'slotIndex', 'new_age'], 'defaults': [], 'name': 'SetPetReviveResultItem'},
                     {'args': ['self', 'slot_index'], 'defaults': [], 'name': 'SetPremiumPrivateShopItem'},
                     {'args': ['self', 'slotIndex'], 'defaults': [], 'name': 'SetPrivateSearchItem'},
                     {'args': ['self', 'invenType', 'invenPos', 'privateShopSlotIndex'], 'defaults': [], 'name': 'SetPrivateShopBuilderItem'},
                     {'args': ['self', 'item_vnum'], 'defaults': [], 'name': 'SetQuestItemToolTip'},
                     {'args': ['self', 'baseSlotIndex', 'materialSlotIndex', 'window_type'], 'defaults': [1], 'name': 'SetResulItemAttrMove'},
                     {'args': ['self', 'item_vnum'], 'defaults': [], 'name': 'SetRouletteItem'},
                     {'args': ['self', 'slotIndex'], 'defaults': [], 'name': 'SetSafeBoxItem'},
                     {'args': ['self', 'slotIndex'], 'defaults': [], 'name': 'SetShopItem'},
                     {'args': ['self', 'slotIndex', 'cointype'], 'defaults': [], 'name': 'SetShopItemBySecondaryCoin'},
                     {'args': ['self', 'attrSlot'], 'defaults': [], 'name': '__AdjustAttrMaxWidth'},
                     {'args': ['self', 'desc'], 'defaults': [], 'name': '__AdjustDescMaxWidth'},
                     {'args': ['self', 'attrSlot', 'desc'], 'defaults': [], 'name': '__AdjustMaxWidth'},
                     {'args': ['self'], 'defaults': [], 'name': '__AppendAbilityPotionInformation'},
                     {'args': ['self', 'oriitemVnum', 'window_type', 'slotIndex', 'sockets', 'refine_element', 'apply_random_list'], 'defaults': [], 'name': '__AppendAcceItemAffectInformation'},
                     {'args': ['self', 'metin_slot', 'mtrl_vnum', 'apply_random_list'], 'defaults': [None], 'name': '__AppendAccessoryMetinSlotInfo'},
                     {'args': ['self', 'slotIndex', 'window_type', 'metinSlot'], 'defaults': [], 'name': '__AppendAffectInformationAcce'},
                     {'args': ['self', 'slotIndex', 'window_type', 'metinSlot'], 'defaults': [], 'name': '__AppendAffectInformationAura'},
                     {'args': ['self', 'sockets', 'refine_element'], 'defaults': [], 'name': '__AppendAttackPowerInfo'},
                     {'args': ['self', 'item'], 'defaults': [], 'name': '__AppendAttackSpeedInfo'},
                     {'args': ['self', 'itemVnum'], 'defaults': [], 'name': '__AppendAttendanceRewardItemicon'},
                     {'args': ['self', 'attrSlot'], 'defaults': [], 'name': '__AppendAttribute6th7thPossibility'},
                     {'args': ['self', 'attrSlot'], 'defaults': [], 'name': '__AppendAttributeInformation'},
                     {'args': ['self', 'itemVnum', 'attrSlot', 'slotIndex', 'window_type', 'metinSlot'], 'defaults': [], 'name': '__AppendAttributeInformationAcce'},
                     {'args': ['self', 'itemVnum', 'attrSlot', 'slotIndex', 'window_type', 'metinSlot'], 'defaults': [], 'name': '__AppendAttributeInformationAura'},
                     {'args': ['self', 'ori_item_vnum', 'window_type', 'slot_index', 'sockets', 'apply_random_list'], 'defaults': [], 'name': '__AppendAuraItemAffectInformation'},
                     {'args': ['self', 'apply_random_list'], 'defaults': [], 'name': '__AppendDefaultItemApplyInformation'},
                     {'args': ['self', 'attrSlot', 'dsType', 'grade'], 'defaults': [0, 0], 'name': '__AppendDragonSoulAttributeInformation'},
                     {'args': ['self', 'size'], 'defaults': [], 'name': '__AppendFishInfo'},
                     {'args': ['self', 'item_vnum', 'metin_slot', 'attr_slot'], 'defaults': [], 'name': '__AppendGemBagItemDescription'},
                     {'args': ['self', 'metin_slot'], 'defaults': [], 'name': '__AppendGloveMetinSlotInfo'},
                     {'args': ['self', 'itemVnum'], 'defaults': [], 'name': '__AppendHairIcon'},
                     {'args': ['self'], 'defaults': [], 'name': '__AppendLimitInformation'},
                     {'args': ['self', 'sockets'], 'defaults': [], 'name': '__AppendMagicAttackInfo'},
                     {'args': ['self'], 'defaults': [], 'name': '__AppendMagicDefenceInfo'},
                     {'args': ['self', 'metinSlot'], 'defaults': [], 'name': '__AppendMetinSlotInfo'},
                     {'args': ['self', 'index', 'metinSlotData', 'custumAffectString', 'custumAffectString2', 'custumAffectString3', 'leftTime'], 'defaults': ['', '', '', 0], 'name': '__AppendMetinSlotInfo_AppendMetinSocketData'},
                     {'args': ['self', 'metinSlot'], 'defaults': [], 'name': '__AppendMetinSlotInfo_IsEmptySlotList'},
                     {'args': ['self', 'mobVnum'], 'defaults': [], 'name': '__AppendMonsterCardItemIcon'},
                     {'args': ['self', 'item_vnum', 'sockets', 'attributes', 'window_type'], 'defaults': [], 'name': '__AppendPassiveJobInformation'},
                     {'args': ['self', 'metinSlot'], 'defaults': [], 'name': '__AppendPetBagItemInfomation'},
                     {'args': ['self', 'metinSlot', 'isFeedWindow'], 'defaults': [False], 'name': '__AppendPetEggItemInformation'},
                     {'args': ['self', 'metinSlot'], 'defaults': [], 'name': '__AppendPetPayItemInformation'},
                     {'args': ['self', 'curLevel', 'curEXP', 'maxEXP'], 'defaults': [], 'name': '__AppendPickInformation'},
                     {'args': ['self'], 'defaults': [], 'name': '__AppendPotionInformation'},
                     {'args': ['self', 'itemVnum'], 'defaults': [], 'name': '__AppendPrivateSearchItemicon'},
                     {'args': ['self', 'itemVnum', 'endTime'], 'defaults': [], 'name': '__AppendRealTimeToolTip'},
                     {'args': ['self', 'refine_element'], 'defaults': [], 'name': '__AppendRefineElementInformation'},
                     {'args': ['self', 'window_type', 'slotIndex', 'metinSlot', 'refine_element'], 'defaults': [], 'name': '__AppendRefineElementInformationAcce'},
                     {'args': ['self', 'refine_element'], 'defaults': [None], 'name': '__AppendRefineElementText'},
                     {'args': ['self', 'curLevel', 'curEXP', 'maxEXP'], 'defaults': [], 'name': '__AppendRodInformation'},
                     {'args': ['self', 'window_type', 'slotIndex'], 'defaults': [], 'name': '__AppendSealInformation'},
                     {'args': ['self', 'metinSlot'], 'defaults': [], 'name': '__AppendSecretDungeonScrollInfo'},
                     {'args': ['self', 'metinSlot', 'new_age'], 'defaults': [0], 'name': '__AppendUpBringingPetItemInfomation'},
                     {'args': ['self'], 'defaults': [], 'name': '__CalculateToolTipWidth'},
                     {'args': ['self', 'dwVnum'], 'defaults': [], 'name': '__DragonSoulInfoString'},
                     {'args': ['self', 'affectType', 'affectValue'], 'defaults': [], 'name': '__GetAffectString'},
                     {'args': ['self', 'index', 'value'], 'defaults': [], 'name': '__GetAttributeColor'},
                     {'args': ['self', 'index', 'value'], 'defaults': [], 'name': '__GetDragonSoulAttributeColor'},
                     {'args': ['self', 'evol_level'], 'defaults': [], 'name': '__GetEvolName'},
                     {'args': ['self', 'apply_type', 'grade'], 'defaults': [], 'name': '__GetRefineElementText'},
                     {'args': ['self', 'apply_type', 'min_value', 'max_value', 'value'], 'defaults': [], 'name': '__GetRefineElementValueText'},
                     {'args': ['self', 'index', 'metin_slot', 'sungma_data'], 'defaults': [], 'name': '__GetSungmaStoneDataByIndex'},
                     {'args': ['self', 'attrSlot'], 'defaults': [], 'name': '__IsAttr'},
                     {'args': ['self', 'itemVnum'], 'defaults': [], 'name': '__IsHair'},
                     {'args': ['self', 'itemVnum'], 'defaults': [], 'name': '__IsNewHair'},
                     {'args': ['self', 'itemVnum'], 'defaults': [], 'name': '__IsNewHair2'},
                     {'args': ['self', 'itemVnum'], 'defaults': [], 'name': '__IsNewHair3'},
                     {'args': ['self', 'itemVnum'], 'defaults': [], 'name': '__IsOldHair'},
                     {'args': ['self', 'itemVnum'], 'defaults': [], 'name': '__IsPolymorphItem'},
                     {'args': ['self', 'itemVnum', 'metinSlot', 'attrSlot', 'set_value'], 'defaults': [0], 'name': '__SetItemTitle'},
                     {'args': ['self', 'set_value'], 'defaults': [0], 'name': '__SetNormalItemTitle'},
                     {'args': ['self', 'monsterVnum'], 'defaults': [], 'name': '__SetPolymorphItemTitle'},
                     {'args': ['self', 'skillIndex', 'bookName', 'skillGrade'], 'defaults': [], 'name': '__SetSkillBookToolTip'},
                     {'args': ['self', 'set_value'], 'defaults': [0], 'name': '__SetSpecialItemTitle'},
                     {'args': ['self', 'itemVnum', 'metinSlot', 'flags'], 'defaults': [], 'name': '__SoulItemToolTip'},
                     {'args': ['self'], 'defaults': [], 'name': '__del__'},
                     {'args': ['self'], 'defaults': [], 'name': '__init__'}],
            'import': [],
            'var': [{'name': 'ANTI_FLAG_DICT', 'type': 'dict', 'value': {0: 4, 1: 8, 2: 16, 3: 32, 4: 262144}},
                    {'name': 'APPLY_RANDOM_TEXT_COLOR', 'type': 'long', 'value': 4286248660L},
                    {'name': 'ATTRIBUTE_NEED_WIDTH', 'type': 'dict', 'value': {23: 230, 24: 230, 25: 230, 26: 220, 27: 210, 35: 210, 36: 210, 37: 210, 38: 210, 39: 210, 40: 210, 41: 210, 42: 220, 43: 230, 45: 230}},
                    {'name': 'FONT_COLOR', 'type': 'int', 'value': -4079167},
                    {'name': 'REFINE_ELEMENT_BONUS_COLOR', 'type': 'int', 'value': -7751539},
                    {'name': 'REFINE_ELEMENT_COLOR_DICT', 'type': 'dict', 'value': {99: 4280530920L, 100: 4292692027L, 101: 4282215647L, 102: 4281847585L, 103: 4294232596L, 104: 4290195180L}},
                    {'name': 'REFINE_ELEMENT_INDEX_APPLY_TYPE', 'type': 'int', 'value': 0},
                    {'name': 'REFINE_ELEMENT_INDEX_BONUS', 'type': 'int', 'value': 3},
                    {'name': 'REFINE_ELEMENT_INDEX_GRADE', 'type': 'int', 'value': 1},
                    {'name': 'REFINE_ELEMENT_INDEX_MAX', 'type': 'int', 'value': 4},
                    {'name': 'REFINE_ELEMENT_INDEX_VALUE', 'type': 'int', 'value': 2},
                    {'name': 'REFINE_ELEMENT_TITLE_TEXT_GAP', 'type': 'int', 'value': 10},
                    {'name': 'SECRET_DUNGONE_SCROLL_ALPHA_COLOR', 'type': 'int', 'value': -16736026},
                    {'name': 'SECRET_DUNGONE_SCROLL_NORMAL_COLOR', 'type': 'int', 'value': -7817332},
                    {'name': '__doc__', 'type': 'NoneType', 'value': None},
                    {'name': '__module__', 'type': 'str', 'value': 'uiToolTip'},
                    {'name': '__qualname__', 'type': 'str', 'value': 'ItemToolTip'}]},
           {'class': [],
            'func': [{'args': ['self', 'skillIndex', 'skillGrade'], 'defaults': [0], 'name': 'AppendDefaultData'},
                     {'args': ['self', 'skillIndex', 'skillLevel'], 'defaults': [], 'name': 'AppendGuildSkillData'},
                     {'args': ['self', 'index', 'desc', 'color'], 'defaults': [], 'name': 'AppendMasterAffectDescription'},
                     {'args': ['self', 'skill_vnum', 'skill_level', 'color'], 'defaults': [], 'name': 'AppendMountUpgradeSkillDescription'},
                     {'args': ['self', 'needSP', 'continuationSP', 'color'], 'defaults': [], 'name': 'AppendNeedHP'},
                     {'args': ['self', 'needSP', 'continuationSP', 'color'], 'defaults': [], 'name': 'AppendNeedSP'},
                     {'args': ['self', 'index', 'desc'], 'defaults': [], 'name': 'AppendNextAffectDescription'},
                     {'args': ['self', 'skillIndex'], 'defaults': [], 'name': 'AppendSkillConditionData'},
                     {'args': ['self', 'slotIndex', 'skillIndex', 'skillGrade', 'skillLevel', 'skillCurrentPercentage', 'skillNextPercentage'], 'defaults': [], 'name': 'AppendSkillDataNew'},
                     {'args': ['self', 'skillIndex', 'skillPercentage', 'color'], 'defaults': [], 'name': 'AppendSkillLevelDescriptionNew'},
                     {'args': ['self', 'skillIndex', 'skillLevel'], 'defaults': [], 'name': 'AppendSkillRequirement'},
                     {'args': ['self', 'skillIndex', 'skillGrade', 'skillLevel', 'maxLevel'], 'defaults': [], 'name': 'AppendSupportSkillDefaultData'},
                     {'args': ['self', 'text', 'color', 'centerAlign'], 'defaults': [-4079167, True], 'name': 'AppendTextLine'},
                     {'args': ['self', 'skillIndex', 'skillLevel'], 'defaults': [], 'name': 'HasSkillLevelDescription'},
                     {'args': ['self', 'skillIndex', 'skillLevel'], 'defaults': [-1], 'name': 'SetSkill'},
                     {'args': ['self', 'slotIndex', 'skillIndex', 'skillGrade', 'skillLevel'], 'defaults': [], 'name': 'SetSkillNew'},
                     {'args': ['self', 'slotIndex', 'skillIndex', 'skillGrade'], 'defaults': [], 'name': 'SetSkillOnlyName'},
                     {'args': ['self', 'skill_grade', 'skill_level'], 'defaults': [], 'name': '__AppendInSightSkillData'},
                     {'args': ['self', 'skill_grade', 'skill_level'], 'defaults': [], 'name': '__AppendLeaderShipSkillData'},
                     {'args': ['self', 'skill_grade', 'skill_level'], 'defaults': [], 'name': '__AppendRoleProficiencySkillData'},
                     {'args': ['self', 'skillIndex', 'skillGrade'], 'defaults': [], 'name': '__AppendSkillGradeName'},
                     {'args': ['self', 'skillLevel', 'color'], 'defaults': [], 'name': '__AppendSummonDescription'},
                     {'args': ['self', 'skillIndex', 'skillGrade'], 'defaults': [], 'name': '__SetSkillTitle'},
                     {'args': ['self'], 'defaults': [], 'name': '__del__'},
                     {'args': ['self'], 'defaults': [], 'name': '__init__'}],
            'import': [],
            'var': [{'name': 'AFFECT_APPEND_TEXT_DICT', 'type': 'dict', 'value': {'DODGE': '%', 'REFLECT_MELEE': '%', 'RESIST_NORMAL': '%'}},
                    {'name': 'FONT_COLOR', 'type': 'int', 'value': -4079167},
                    {'name': 'PARTY_SKILL_ATTACKER_AFFECT_LIST', 'type': 'tuple', 'value': ((36, 3), (26, 1), (32, 2))},
                    {'name': 'PARTY_SKILL_EXPERIENCE_AFFECT_LIST', 'type': 'tuple', 'value': ((2, 2, 10), (8, 3, 20), (14, 4, 30), (22, 5, 45), (28, 6, 60), (34, 7, 80), (38, 8, 100))},
                    {'name': 'PARTY_SKILL_PLUS_GRADE_AFFECT_LIST', 'type': 'tuple', 'value': ((4, 2, 1, 0), (10, 3, 2, 0), (16, 4, 2, 1), (24, 5, 2, 2))},
                    {'name': 'PARTY_SKILL_TOOL_TIP_WIDTH', 'type': 'int', 'value': 340},
                    {'name': 'SKILL_TOOL_TIP_WIDTH', 'type': 'int', 'value': 200},
                    {'name': '__doc__', 'type': 'NoneType', 'value': None},
                    {'name': '__module__', 'type': 'str', 'value': 'uiToolTip'},
                    {'name': '__qualname__', 'type': 'str', 'value': 'SkillToolTip'}]},
           {'class': [],
            'func': [{'args': ['self'], 'defaults': [], 'name': 'AlignHorizonalCenter'},
                     {'args': ['self'], 'defaults': [], 'name': 'AlignTextLineHorizonalCenter'},
                     {'args': ['self', 'desc', 'limit', 'color'], 'defaults': [-4079167], 'name': 'AppendDescription'},
                     {'args': ['self'], 'defaults': [], 'name': 'AppendHorizontalLine'},
                     {'args': ['self', 'size'], 'defaults': [], 'name': 'AppendSpace'},
                     {'args': ['self', 'text', 'color', 'centerAlign'], 'defaults': [-4079167, True], 'name': 'AppendTextLine'},
                     {'args': ['self', 'text', 'color', 'text2', 'color2', 'centerAlign'], 'defaults': [-102, True], 'name': 'AppendTwoColorTextLine'},
                     {'args': ['self', 'left_text', 'left_text_color', 'center_text', 'center_text_color', 'left_gap', 'is_color_check'], 'defaults': [0, True], 'name': 'AppendTwoTextLineLeftCenter'},
                     {'args': ['self', 'right_text', 'right_text_color', 'center_text', 'center_text_color', 'right_gap', 'is_color_check'], 'defaults': [0, True], 'name': 'AppendTwoTextLineRightCenter'},
                     {'args': ['self', 'text', 'color', 'centerAlign'], 'defaults': [-4079167, True], 'name': 'AutoAppendTextLine'},
                     {'args': ['self'], 'defaults': [], 'name': 'ClearToolTip'},
                     {'args': ['self', 'value', 'isSpecial'], 'defaults': [False], 'name': 'GetChangeTextLineColor'},
                     {'args': ['self', 'curValue', 'limitValue'], 'defaults': [], 'name': 'GetLimitTextLineColor'},
                     {'args': ['self'], 'defaults': [], 'name': 'HideToolTip'},
                     {'args': ['self'], 'defaults': [], 'name': 'OnUpdate'},
                     {'args': ['self'], 'defaults': [], 'name': 'OptimizeTooltipWindowSize'},
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
            'var': [{'name': 'ATTR_6TH_7TH_COLOR', 'type': 'int', 'value': -102},
                    {'name': 'CANNOT_LEVEL_UP_COLOR', 'type': 'int', 'value': -1738635},
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
                    {'name': 'TEXTLINE_2ND_COLOR_DEFAULT', 'type': 'int', 'value': -102},
                    {'name': 'TEXT_LINE_HEIGHT', 'type': 'int', 'value': 17},
                    {'name': 'TITLE_COLOR', 'type': 'int', 'value': -923968},
                    {'name': 'TOOL_TIP_HEIGHT', 'type': 'int', 'value': 10},
                    {'name': 'TOOL_TIP_WIDTH', 'type': 'int', 'value': 190},
                    {'name': '__doc__', 'type': 'NoneType', 'value': None},
                    {'name': '__module__', 'type': 'str', 'value': 'uiToolTip'},
                    {'name': '__qualname__', 'type': 'str', 'value': 'ToolTip'}]}],
 'func': [{'args': ['desc', 'limit'], 'defaults': [], 'name': 'SplitDescription'}, {'args': ['n'], 'defaults': [], 'name': 'chop'}],
 'import': ['shop',
            'mail',
            'chatm2g',
            'app',
            'dbg',
            'playerm2g2',
            'uiRefine',
            'skill',
            'constInfo',
            'grp',
            'chr',
            'mouseModule',
            'safebox',
            'localeInfo',
            'exchange',
            '__builtin__',
            'background',
            'wndMgr',
            'guild',
            'uiDragonSoul',
            'mount',
            'premiumPrivateShop',
            'item',
            'uiMonsterCard',
            'ui',
            'guildbank',
            'grpText',
            'nonplayer'],
 'var': [{'name': 'DESC_DEFAULT_MAX_COLS', 'type': 'int', 'value': 26},
         {'name': 'DESC_WESTERN_MAX_COLS', 'type': 'int', 'value': 35},
         {'name': 'DESC_WESTERN_MAX_WIDTH', 'type': 'int', 'value': 220},
         {'name': 'INSIGHT_ATTACKER_ADJUSTMENT_VALUE', 'type': 'int', 'value': 9},
         {'name': 'INSIGHT_ATTACKER_BASE_VALUE', 'type': 'int', 'value': 2},
         {'name': 'INSIGHT_BERSERKER_ADJUSTMENT_VALUE', 'type': 'int', 'value': 1},
         {'name': 'INSIGHT_BERSERKER_BASE_VALUE', 'type': 'int', 'value': 1},
         {'name': 'INSIGHT_BUFFER_ADJUSTMENT_VALUE', 'type': 'int', 'value': 4},
         {'name': 'INSIGHT_BUFFER_BASE_VALUE', 'type': 'int', 'value': 1},
         {'name': 'INSIGHT_DEFENDER_ADJUSTMENT_VALUE', 'type': 'int', 'value': 2},
         {'name': 'INSIGHT_DEFENDER_BASE_VALUE', 'type': 'int', 'value': 1},
         {'name': 'INSIGHT_SKILL_MASTER_ADJUSTMENT_VALUE', 'type': 'int', 'value': 5},
         {'name': 'INSIGHT_SKILL_MASTER_BASE_VALUE', 'type': 'int', 'value': 1},
         {'name': 'INSIGHT_TANKER_ADJUSTMENT_VALUE', 'type': 'int', 'value': 520},
         {'name': 'INSIGHT_TANKER_BASE_VALUE', 'type': 'int', 'value': 10},
         {'name': 'LEADERSHIP_ATTACKER_ADJUSTMENT_VALUE', 'type': 'int', 'value': 50},
         {'name': 'LEADERSHIP_ATTACKER_BASE_VALUE', 'type': 'int', 'value': 10},
         {'name': 'LEADERSHIP_BERSERKER_ADJUSTMENT_VALUE', 'type': 'int', 'value': 3},
         {'name': 'LEADERSHIP_BERSERKER_BASE_VALUE', 'type': 'int', 'value': 1},
         {'name': 'LEADERSHIP_BUFFER_ADJUSTMENT_VALUE', 'type': 'int', 'value': 8},
         {'name': 'LEADERSHIP_BUFFER_BASE_VALUE', 'type': 'int', 'value': 5},
         {'name': 'LEADERSHIP_DEFENDER_ADJUSTMENT_VALUE', 'type': 'int', 'value': 3},
         {'name': 'LEADERSHIP_DEFENDER_BASE_VALUE', 'type': 'int', 'value': 1},
         {'name': 'LEADERSHIP_SKILL_MASTER_ADJUSTMENT_VALUE', 'type': 'int', 'value': 2},
         {'name': 'LEADERSHIP_SKILL_MASTER_BASE_VALUE', 'type': 'int', 'value': 1},
         {'name': 'LEADERSHIP_TANKER_ADJUSTMENT_VALUE', 'type': 'int', 'value': 1120},
         {'name': 'LEADERSHIP_TANKER_BASE_VALUE', 'type': 'int', 'value': 50},
         {'name': 'SUNGMA_STONE_AMPLIFICATION_MAX_LENGTH', 'type': 'int', 'value': 2},
         {'name': 'SUNGMA_STONE_DATA_MAX_LENGTH', 'type': 'int', 'value': 6},
         {'name': 'SUNGMA_STONE_REFINE_MAX_LENGTH', 'type': 'int', 'value': 4},
         {'name': 'SUNGMA_STONE_VALUE_MAX_LENGTH', 'type': 'int', 'value': 5},
         {'name': 'WARP_SCROLLS', 'type': 'list', 'value': [22011, 22000, 22010]},
         {'name': '__doc__', 'type': 'NoneType', 'value': None},
         {'name': '__name__', 'type': 'str', 'value': 'uiToolTip'},
         {'name': '__package__', 'type': 'NoneType', 'value': None},
         {'name': '__test__', 'type': 'dict', 'value': {}}]}
