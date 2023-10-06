'''
梅花易数
简单命令行版

by: DashBing
'''

num_to_gua = [
    "坤",
    "乾",
    "兑",
    "离",
    "震",
    "巽",
    "坎",
    "艮"
]

gua_to_num = {}
for i in range(len(num_to_gua)):
    gua_to_num = gua_to_num | {num_to_gua[i]:i}

guas_to_gua = {
    "乾":[1,1,1],
    "兑":[0,1,1],
    "离":[1,0,1],
    "震":[0,0,1],
    "巽":[1,1,0],
    "坎":[0,1,0],
    "艮":[1,0,0],
    "坤":[0,0,0]
}

gua_to_guas = {}
for i in guas_to_gua:
    gua_to_guas = gua_to_guas | {tuple(guas_to_gua[i]):i}

gua_xps = {
    "乾":["金", "天"],
    "兑":["金", "泽"],
    "离":["火", "火"],
    "震":["木", "雷"],
    "巽":["木", "风"],
    "坎":["水", "水"],
    "艮":["土", "山"],
    "坤":["土", "地"]
}

item_s = {
    "金":"水",
    "水":"木",
    "木":"火",
    "火":"土",
    "土":"金"
}

item_k = {
    "金":"木",
    "木":"土",
    "土":"水",
    "水":"火",
    "火":"金"
}

gua64 = {
    ("乾", "乾"):"乾卦",
    ("乾", "兑"):"天泽履",
    ("乾", "离"):"天火同人",
    ("乾", "震"):"天雷无妄",
    ("乾", "巽"):"天风垢",
    ("乾", "坎"):"天水讼",
    ("乾", "艮"):"天山遁",
    ("乾", "坤"):"天地否",
    ("兑", "乾"):"泽天央",
    ("兑", "兑"):"泽卦",
    ("兑", "离"):"泽火革",
    ("兑", "震"):"泽雷随",
    ("兑", "巽"):"泽风大过",
    ("兑", "坎"):"泽水困",
    ("兑", "艮"):"泽山咸",
    ("兑", "坤"):"泽地萃",
    ("离", "乾"):"火天大有",
    ("离", "兑"):"火泽暌",
    ("离", "离"):"离卦",
    ("离", "震"):"火雷噬嗑",
    ("离", "巽"):"火风鼎",
    ("离", "坎"):"火水未济",
    ("离", "艮"):"火山旅",
    ("离", "坤"):"火地晋",
    ("震", "乾"):"雷天大壮",
    ("震", "兑"):"雷泽归妹",
    ("震", "离"):"雷火丰",
    ("震", "震"):"震卦",
    ("震", "巽"):"雷风恒",
    ("震", "坎"):"雷水解",
    ("震", "艮"):"雷山小过",
    ("震", "坤"):"雷地豫",
    ("巽", "乾"):"风天小畜",
    ("巽", "兑"):"风泽中孚",
    ("巽", "离"):"风火家人",
    ("巽", "震"):"风雷益",
    ("巽", "巽"):"巽卦",
    ("巽", "坎"):"风水涣",
    ("巽", "艮"):"风山渐",
    ("巽", "坤"):"风地观",
    ("坎", "乾"):"水天需",
    ("坎", "兑"):"水泽节",
    ("坎", "离"):"水火既济",
    ("坎", "震"):"水雷屯",
    ("坎", "巽"):"水风井",
    ("坎", "坎"):"坎卦",
    ("坎", "艮"):"水山蹇",
    ("坎", "坤"):"水地比",
    ("艮", "乾"):"山天大畜",
    ("艮", "兑"):"山泽损",
    ("艮", "离"):"山火贲",
    ("艮", "震"):"山雷颐",
    ("艮", "巽"):"山风蛊",
    ("艮", "坎"):"山水蒙",
    ("艮", "艮"):"艮卦",
    ("艮", "坤"):"山地剥",
    ("坤", "乾"):"地天泰",
    ("坤", "兑"):"地泽临",
    ("坤", "离"):"地火明夷",
    ("坤", "震"):"地雷复",
    ("坤", "巽"):"地风升",
    ("坤", "坎"):"地水师",
    ("坤", "艮"):"地山谦",
    ("坤", "坤"):"坤卦",
}

def numn(a):
    if a == 0:
        return(1)
    else:
        return(0)

out_str = '''上卦:{up_gua}
下挂:{down_gua}
动变爻{dy}
{gua_flag}

本卦:{this} (上卦:{this_a}卦 属{this_a_xp}, 下卦:{this_b}卦 属{this_b_xp})
互见:{rand} (上卦:{rand_a}卦 属{rand_a_xp}, 下卦:{rand_b}卦 属{rand_b_xp})
变卦:{change} (上卦:{change_a}卦 属{change_a_xp}, 下卦:{change_b}卦 属{change_b_xp})

初步评估:
开始:{begin_flag} {begin}
过程中:{middle_flag} {middle}
结果:{result_flag} {result}

想要得到更准确的结果, 请把本消息复制粘贴给专业人士作进一步分析!'''

results = {
    "体克用":"小吉",
    "体生用":"小凶",
    "用克体":"大凶",
    "用生体":"大吉",
    "体合用":"大吉"
}

def item_pk(a, b):
    flag = None
    a, b = gua_xps[a][0], gua_xps[b][0]
    if a == b:
        flag = "体合用"
    elif item_k[a] == b:
        flag = "体克用"
    elif item_s[a] == b:
        flag = "体生用"
    elif a == item_k[b]:
        flag = "用克体"
    elif a == item_s[b]:
        flag = "用生体"
    result = results[flag]
    return(flag, result)

def pre_solve(a, b):
    dy = (a + b)%6
    """
    if dy in [1, 2, 3]:
        beg = guas_to_gua[num_to_gua[a%8]] + guas_to_gua[num_to_gua[b%8]]
    else:
        beg = guas_to_gua[num_to_gua[b%8]] + guas_to_gua[num_to_gua[a%8]]
    """
    beg = guas_to_gua[num_to_gua[a%8]] + guas_to_gua[num_to_gua[b%8]]
    hug = beg[1:4] + beg[2:5]
    big = beg
    big = list(reversed(big))
    big[dy] = numn(big[dy])
    big = list(reversed(big))
    beg = [gua_to_guas[tuple(beg[0:3])], gua_to_guas[tuple(beg[3:6])]]
    hug = [gua_to_guas[tuple(hug[0:3])], gua_to_guas[tuple(hug[3:6])]]
    big = [gua_to_guas[tuple(big[0:3])], gua_to_guas[tuple(big[3:6])]]
    return(dy, beg, hug, big)

def meihua(a, b):
    tmp = pre_solve(a, b)
    dy = tmp[0]
    beg = tmp[1]
    hug = tmp[2]
    big = tmp[3]
    del tmp

    d = {}
    d["up_gua"] = a
    d["down_gua"] = b
    d["dy"] = dy
    if dy in [1, 2, 3]:
        d["gua_flag"] = "上体下用"
    else:
        d["gua_flag"] = "上用下体"
    d["this"] = gua64[tuple(beg)]
    d["rand"] = gua64[tuple(hug)]
    d["change"] = gua64[tuple(big)]

    d["this_a"] = beg[0]
    d["this_a_xp"] = gua_xps[beg[0]][0]
    d["this_b"] = beg[1]
    d["this_b_xp"] = gua_xps[beg[1]][0]
    d["rand_a"] = hug[0]
    d["rand_a_xp"] = gua_xps[hug[0]][0]
    d["rand_b"] = hug[1]
    d["rand_b_xp"] = gua_xps[hug[1]][0]
    d["change_a"] = big[0]
    d["change_a_xp"] = gua_xps[big[0]][0]
    d["change_b"] = big[1]
    d["change_b_xp"] = gua_xps[big[1]][0]

    if not(dy in [1, 2, 3]):
        beg = list(reversed(beg))
        hug = list(reversed(hug))
        big = list(reversed(big))
    tmp = item_pk(*(tuple(beg)))
    d["begin_flag"] = tmp[0]
    d["begin"] = tmp[1]
    tmp = item_pk(*(tuple(hug)))
    d["middle_flag"] = tmp[0]
    d["middle"] = tmp[1]
    tmp = item_pk(*(tuple(big)))
    d["result_flag"] = tmp[0]
    d["result"] = tmp[1]

    return(d)

def meihua_text(a, b):
    d = meihua(a, b)
    return(out_str.format(**d))

if __name__ == "__main__":
    a = int(input("数字A:"))
    b = int(input("数字B:"))
    print(meihua_text(a, b))
    while True:
        pass
