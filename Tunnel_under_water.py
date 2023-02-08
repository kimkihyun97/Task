import pandas as pd
from collections import deque
class Tunnel():

    def __init__(self, datas):
        self.datas = datas
        self.df = None
        self.index = []
        self.index_num = []


    def refine_data (self):
        for start, end,num in self.datas:
            if num not in self.index_num :
                self.index_num.append(num)
            if start not in self.index: self.index.append(start)
            if end not in self.index : self.index.append(end)
        city = {f'{city}': [0 for _ in range(len(self.index))] for city in self.index}
        self.dfcity = pd.DataFrame(city, index=self.index)
        self.df = pd.DataFrame(city,index=self.index)

        for start, end, num in self.datas:
            self.dfcity.loc[start,end] = num

        print(self.dfcity)

    def list_must(self):
        num = max(self.index_num)
        lst_must = self.find_city(num)
        return [lst_must, lst_must.sort(reverse=True)]

    def get_tunnel(self):
        info = []
        for edge in self.index_num :

            visited_edge = [0 for _ in self.index_num]
            visited_edge[self.index_num.index(edge)] = 1
            self.bfs(edge,visited_edge,info)
        ans = sorted(info, key = lambda x:x[1])[0]
        for start,end in ans[0] :
            self.df.loc[start,end] = self.dfcity.loc[start, end]
            self.df.loc[end, start] = self.dfcity.loc[start, end]

        print('## 가장 효율적인 해저 케이블 연결도 ##')
        print(self.df)
        print(f"최소 비용 : {ans[1]}")


    def bfs(self,edge,visited_edge,info):
        que = deque([edge])
        length = edge
        map = []

        map.append(self.find_city(edge))

        while que:
            current = que.popleft()

            for city in self.find_city(current):
                for way in self.dfcity.loc[city,:] :
                    if way != 0 :
                        if visited_edge[self.index_num.index(way)] == 0:
                            visited_edge[self.index_num.index(way)] = 1
                            map.append(self.find_city(way))
                            length += way
                            if self.IsFull(map) :
                                if self.list_must()[0] in map or self.list_must()[1] in map :
                                    info.append([map,length])
                                return
                            que.append(way)

    def find_city(self,edge):
        city=set()
        for start in self.index :
            for end in self.index :
                if self.dfcity.loc[start,end] == edge :
                    city.update([start,end])

        return list(city)

    def IsFull(self,map):
        lst =[]
        for start,end in map :
            lst.append(start)
            lst.append(end)
        for city in self. index :
            if city not in lst : return False

        return True



if __name__ == '__main__' :
    data = [['서울','뉴욕',80],['서울','북경',10],['뉴욕','서울',80],['뉴욕','북경',40],['뉴욕','방콕',70],
            ['런던','방콕',30],['런던','파리',60],['북경','서울',10],['북경','뉴욕',40],['북경','방콕',50],
            ['방콕','뉴욕',70],['방콕','북경',50],['방콕','런던',30],['방콕','파리',20],['파리','방콕',20],['파리','런던',60]]
    find_shortest_way = Tunnel(data)
    find_shortest_way.refine_data()
    find_shortest_way.get_tunnel()

