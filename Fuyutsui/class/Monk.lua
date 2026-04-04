local _, fu = ...
if fu.classId ~= 10 then return end

fu.HarmfulSpellId, fu.HelpfulSpellId = 100780, 116670

fu.heroSpell = {
    [450508] = 1, -- 祥和宗师
    [450615] = 2, -- 影踪派
    [443028] = 3, -- 天神御师
    [123904] = 3, -- 天神御师
}

function fu.updateSpecInfo()
    local specIndex = C_SpecializationInfo.GetSpecialization()
    fu.powerType = nil
    fu.blocks = nil
    fu.group_blocks = nil
    fu.assistant_spells = nil
    if specIndex == 1 then
        fu.HarmfulSpellId = 121253
        fu.blocks = {
            stagger = 11,
            assistant = 12,
            target_valid = 13,
            target_health = 14,
            enemy_count = 15,
            hero_talent = 16,
            failedSpell = 17,
            auras = {
                ["疗伤珠"] = {
                    index = 20,
                    auraRef = fu.auras["疗伤珠"],
                    showKey = "count",
                },
                ["活力苏醒"] = {
                    index = 21,
                    auraRef = fu.auras["活力苏醒"],
                    showKey = "remaining",
                },
                ["清空地窖"] = {
                    index = 22,
                    auraRef = fu.auras["清空地窖"],
                    showKey = "remaining",
                },
            },
            spell_cd = {
                [121253] = { index = 31, name = "醉酿投" },
                [119582] = { index = 33, name = "活血酒" },
                [322507] = { index = 35, name = "天神酒" },
                [1241059] = { index = 37, name = "天神灌注" },

                [322109] = { index = 39, name = "轮回之触" },
                [119381] = { index = 40, name = "扫堂腿" },
                [322101] = { index = 41, name = "移花接木" },
                [101643] = { index = 42, name = "魂体双分" },
                [119996] = { index = 43, name = "魂体双分：转移" },
                [116705] = { index = 44, name = "切喉手" },
                [115181] = { index = 45, name = "火焰之息" },
                [123986] = { index = 46, name = "真气爆裂" },
                [325153] = { index = 47, name = "爆炸酒桶" },
                [198898] = { index = 48, name = "赤精之歌" },
                [115399] = { index = 49, name = "玄牛酒" },
            },
            spell_charge = {
                [121253] = { index = 32, name = "醉酿投" },
                [119582] = { index = 34, name = "活血酒" },
                [322507] = { index = 36, name = "天神酒" },
                [1241059] = { index = 38, name = "天神灌注" },
            },
        }
    elseif specIndex == 2 then
    elseif specIndex == 3 then
    end
end

function fu.CreateClassMacro()
    local dynamicSpells = { "氤氲之雾", "活血术", "清创生血", "抚慰之雾", "复苏之雾" }
    local staticSpells = {
        [1] = "扫堂腿",
        [2] = "神鹤引项踢",
        [3] = "壮胆酒",
        [4] = "[known:116844,@cursor]平心之环;[known:198898]赤精之歌",
        [5] = "猛虎掌",
        [6] = "轮回之触",
        [7] = "幻灭踢",
        [8] = "碎玉闪电",
        [9] = "切喉手",
        [10] = "天神灌注",
        [11] = "火焰之息",
        [12] = "活血酒",
        [13] = "[@player]爆炸酒桶",
        [14] = "玄牛下凡",
        [15] = "醉酿投",
        [16] = "真气爆裂",
        [17] = "天神酒",
        [18] = "移花接木",
        [19] = "魂体双分",
        [20] = "魂体双分：转移",


    }
    fu.CreateMacro(dynamicSpells, staticSpells, _)
end
