'''
小六壬 (压缩版)
简单命令行版

by: DashBing
'''

rens, out_str, xiaoliuren_text = ["空亡","大安","留连","速喜","赤口","小吉"], "天宫: %s\n地宫: %s\n人宫: %s", lambda a, b, c:out_str%(rens[a%6], rens[abs((b + a%6)%6)], rens[c%6])
print(xiaoliuren_text(int(input("天宫:")), int(input("地宫:")), int(input("人宫:"))))
