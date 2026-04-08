# -*- coding: utf-8 -*-
"""战士职业的基础逻辑（未实现）。"""

from utils import *

action_map = {
    1: ("英勇投掷", "英勇投掷"),
    2: ("战斗怒吼", "战斗怒吼"),
    3: ("猛击", "猛击"),
    4: ("撕裂", "撕裂"),
    5: ("斩杀", "斩杀"),
    6: ("剑刃风暴", "剑刃风暴"),
    7: ("崩摧", "崩摧"),
    8: ("致死打击", "致死打击"),
    9: ("巨人打击", "巨人打击"),
    10: ("顺劈斩", "顺劈斩"),
    11: ("压制", "压制"),
    12: ("横扫攻击", "横扫攻击"),
    13: ("天神下凡", "天神下凡"),
    14: ("旋风斩", "旋风斩"),
    15: ("斩杀", "斩杀"),
    16: ("嗜血", "嗜血"),
    17: ("暴怒", "暴怒"),
    18: ("奥丁之怒", "奥丁之怒"),
    19: ("怒击", "怒击"),
    20: ("雷霆一击", "雷霆一击"),
    21: ("雷霆轰击", "雷霆一击"),
    22: ("复仇", "复仇"),
    23: ("盾牌猛击", "盾牌猛击"),
    24: ("斩杀", "斩杀"),
}


def run_warrior_logic(state_dict, spec_name):
    spells = state_dict.get("spells") or {}
    战斗 = state_dict.get("战斗")
    移动 = state_dict.get("移动")
    施法 = state_dict.get("施法")
    引导 = state_dict.get("引导")
    生命值 = state_dict.get("生命值")
    能量值 = state_dict.get("能量值")
    一键辅助 = state_dict.get("一键辅助")
    法术失败 = state_dict.get("法术失败", 0)
    目标有效 = state_dict.get("目标有效")
    队伍类型 = int(state_dict.get("队伍类型", 0) or 0)
    队伍人数 = int(state_dict.get("队伍人数", 0) or 0)
    首领战 = int(state_dict.get("首领战", 0) or 0)
    难度 = int(state_dict.get("难度", 0) or 0)
    英雄天赋 = int(state_dict.get("英雄天赋", 0) or 0)
    目标生命值 = state_dict.get("目标生命值", 0)
    敌人人数 = state_dict.get("敌人人数", 0)
    tup = action_map.get(一键辅助)

    def _failed_spell_logic():
        spell_map = {
            1: "胜利在望",
            2: "勇士之矛",
            3: "英勇飞跃",
            4: "集结呐喊",
            5: "震荡波",
            6: "风暴之锤",
            7: "破裂投掷",
            8: "碎裂投掷",
            9: "破胆怒吼",
            10: "盾牌冲锋",
        }
        spell_name = spell_map.get(法术失败)

        if spell_name and spells.get(spell_name, -1) == 0:
            current_step = f"施放 {spell_name}"
            action_hotkey = get_hotkey(0, spell_name)
            return current_step, action_hotkey

        return None, None


    action_hotkey = None
    current_step = "无匹配技能"
    unit_info = {}

    if spec_name == "防护":
        盾牌格挡 = state_dict.get("盾牌格挡", 0)

        if 法术失败 != 0:
            current_step, action_hotkey = _failed_spell_logic()
        elif 战斗 and 目标有效:
            if 盾牌格挡 == 0 and spells.get("盾牌格挡") == 0 and 能量值 >= 25:
                current_step = "施放 盾牌格挡"
                action_hotkey = get_hotkey(0, "盾牌格挡")
            elif 生命值 < 70 and spells.get("胜利在望") == 0:
                current_step = "施放 胜利在望"
                action_hotkey = get_hotkey(0, "胜利在望")
            elif 能量值 >= 60:
                current_step = "施放 无视苦痛"
                action_hotkey = get_hotkey(0, "无视苦痛")
            elif tup:
                current_step = f"施放 {tup[0]}"
                action_hotkey = get_hotkey(0, tup[1])
        else:
            current_step = "无匹配技能"

    return action_hotkey, current_step, unit_info
