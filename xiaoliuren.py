'''
小六壬
简单命令行版

by: DashBing
'''

rens = ["空亡","大安","留连","速喜","赤口","小吉"]
def xiaoliuren(a, b, c):
    ga = a%6
    return(rens[ga], rens[abs((b + ga)%6)], rens[c%6])
out_str = "天宫: %s\n地宫: %s\n人宫: %s"
xiaoliuren_text = lambda a, b, c:out_str%(xiaoliuren(a, b, c))
if __name__ == "__main__":
    a, b, c = int(input("天宫:")), int(input("地宫:")), int(input("人宫:"))
    print(xiaoliuren_text(a, b, c))
    while True:
        pass
