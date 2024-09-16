def rev_dict(d):
    tmp = {}
    for i in d:
        tmp = tmp | {d[i]:i}
    return tmp

阳 = 1
阴 = 0

卦表 = [
    "坤",
    "乾",
    "兑",
    "离",
    "震",
    "巽",
    "坎",
    "艮"
]

卦象 = {  # 低位为下爻，高位为上爻，从下往上数
    "乾":(1,1,1),
    "兑":(1,1,0),
    "离":(1,0,1),
    "震":(1,0,0),
    "巽":(0,1,1),
    "坎":(0,1,0),
    "艮":(0,0,1),
    "坤":(0,0,0)
}

卦性 = {
    "乾":("金", "天"),
    "兑":("金", "泽"),
    "离":("火", "火"),
    "震":("木", "雷"),
    "巽":("木", "风"),
    "坎":("水", "水"),
    "艮":("土", "山"),
    "坤":("土", "地")
}

生 = {
    "金":"水",
    "水":"木",
    "木":"火",
    "火":"土",
    "土":"金"
}

克 = {
    "金":"木",
    "木":"土",
    "土":"水",
    "水":"火",
    "火":"金"
}

复卦名 = {
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

class 卦:
    @property
    def available(self):
        if len(self.data) != 3:
            return (False, "运行时错误：卦象格式错误")
        for i in self.data:
            if type(i) != type(int) or type(i) != type(bool):
                return (False, "运行时错误：卦象格式错误")
            if int(i) not in (0, 1):
                return (False, "运行时错误：卦象格式错误")
        return (True, "运行状态良好")

    def __init__(self, data):
        if type(data) == type(self):
            self.data = data.data
        elif type(data) == type(list) or type(data) == type(tuple):
            self.data = tuple(data)
        elif type(data) == type(int):
            self.data = rev_dict(卦象)[卦表[data%8]]
        elif type(data) == type(str) and data in 卦表:
            self.data = 卦象[data]
        else:
            raise Exception("初始化错误：不支持的卦初始化数据")
        if not self.available[0]:
            raise Exception(self.available[1])

    @property
    def name(self):
        if not self.available[0]:
            raise Exception(self.available[1])
        return(rev_dict(卦象)[self.data])

    @property
    def elements(self):
        if not self.available[0]:
            raise Exception(self.available[1])
        return(卦性[self.name])

    def __eq__(self, value):
        if not self.available[0]:
            raise Exception(self.available[1])
        return(self.data == value.data)

class 复卦:
    @property
    def available(self):
        if type(self.data) != type(list):
            return(False, "运行时错误：复卦格式错误")
        if len(self.data) != 2:
            return(False, "运行时错误：复卦格式错误")
        if type(self.data[0]) != type(卦) or type(self.data[1]) != type(卦):
            return(False, "运行时错误：复卦格式错误")
        for i in self.change:
            if type(i) != type(int):
                return (False, "运行时错误：动爻表错误")
        return (True, "运行状态良好")

    def __init__(self, gua1:卦, gua2:卦, change:list[int]):
        if map(type, [gua1, gua2, change]) != map(type, [卦, 卦, list]):
            raise Exception("初始化错误：复卦初始化失败")
        self.data = [gua1, gua2]
        self.change = change
        if not self.available[0]:
            raise Exception(self.available[1])
