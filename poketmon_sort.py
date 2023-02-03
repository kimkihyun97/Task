class PoketmonList():
    def __init__(self, poketmon_dic):
        self.poketmon_dic = poketmon_dic

    def sort_poketmon(self):
        return sorted(self.poketmon_dic.items(), key=lambda x: -x[1])

    def add_poketmon(self, poketmon):
        for k, v in poketmon.items():
            self.poketmon_dic[k] = v

poketmon_dict = {"피카츄":50,"리자몽":500,"거북왕":600,"피존투":200,"루기아":550,"마자용":300}
add_poket = {'아르세우스' : 1000,'기라티나' : 900, '디아루가' : 850}

my_poketmon_dic = PoketmonList(poketmon_dict)
my_poketmon_dic.add_poketmon(add_poket)
print(my_poketmon_dic.sort_poketmon())
