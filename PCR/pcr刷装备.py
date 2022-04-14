# 命令行版本，已停止维护
addr = "D:/Download/规划结果 2110100044.csv"  # 从 pcr.satroki.tech 获得csv文件


class CheckPoint:
    def __init__(self, name, times, rtimes, drops, _id):
        self.name = name
        self.times = int(times)
        self.rtimes = int(rtimes)
        self.drops = drops
        self._id = int(_id)

    def fight(self, bat):
        self.times -= bat
        self.rtimes -= bat

    def show(self):
        print("{}\t{}\t{}\t{}".format(self.name, self.times, self.rtimes, self._id))


def strcut(s):
    return s[:s.index(' +')]


def brush(a):
    for k, v in d.items():
        if a in k:
            print(k)
            print("{}\t{}\t{}\t{}".format("地图", "次数", "推荐", "ID"))
            for i in v:
                i.show()
    print("输入地图id 次数(输入0退出)")
    while True:
        try:
            _id, ti = map(int, input().split())
            l[_id].fight(ti)
            l[_id].show()
        except BaseException:
            break


l = []
d = {}
j = 0
with open(addr, 'r', encoding='utf-8') as f:
    f.readline()
    for s in f:
        s = s.split(',')
        l.append(CheckPoint(s[0], s[1], s[2], s[3:], j))
        for i in s[3:]:
            st = strcut(i)
            if st in d:
                d[st].append(l[j])
            else:
                d[st] = [l[j]]
        j += 1
while True:
    a = input("输入装备名(输入0退出):",)
    if a != '0':
        brush(a)
    else:
        break

with open(addr, 'w', encoding='utf-8') as f:
    f.write("关卡,次数,推荐,掉落期望\n")
    for i in l:
        if i.times > 0:
            f.write("{},{},{},{}".format(i.name, i.times, i.rtimes, ','.join(i.drops)))
