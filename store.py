import pandas as pd
class graph():

    def __init__(self,datas):
        self.datas = datas
        self.df = None
        self.index = []

    def refine_data(self):
        for start, end in self.datas:
            if start not in self.index: self.index.append(start)
            if end not in self.index : self.index.append(end)
        store = {f'{store}': [0 for _ in range(len(self.index))] for store in self.index}
        self.df = pd.DataFrame(store,index = self.index)

    def input_data(self):
        for start, end in self.datas :
            self.df.loc[start,end] = 1

        return self.df

    def get_store(self):
        chip_num = []
        for start in self.index :
            visited = [0 for _ in range(len(self.index))]
            visited[self.index.index(start)] = 1
            if not chip_num :
                chip_num.append([start.split('/')[0],int(start.split('/')[1])])
            elif chip_num[0][1] < int(start.split('/')[1]):
                chip_num.pop()
                chip_num.append([start.split('/')[0], int(start.split('/')[1])])
            self.bfs(start,visited,chip_num)

        print(f"허니버터 최대 보유 편의점 - >{chip_num[0][0]}, {chip_num[0][1]}개")

    def bfs(self,start,visited,chip_num):
        que = [start]

        while que :
            now = que.pop()

            for next in self.index :
                if self.df.loc[now,next] == 1 and visited[self.index.index(next)] != 1:
                    visited[self.index.index(next)] = 1
                    que.append(next)
                    if int(next.split('/')[1]) > chip_num[0][1] :
                        chip_num.pop()
                        chip_num.append([next.split('/')[0],int(next.split('/')[1])])

        return chip_num


if __name__ == "__main__" :
    data = [['gs25/30', 'seven/10'], ['거북슈퍼/99','gs25/30'],['거북슈퍼/99','ministop/90'],['gs25/30', 'cu/60'], ['seven/10', 'cu/60'],
            ['seven/10', 'ministop/90'], ['바둑슈퍼/20','cu/60'],['cu/60', 'ministop/90'], ['바둑슈퍼/20','거북슈퍼/99'],['ministop/90', 'emart24/40']]
    store_graph = graph(data)
    store_graph.refine_data()
    print("## Map of Store ##")
    print(store_graph.input_data())
    store_graph.get_store()
