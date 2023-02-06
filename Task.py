import random
import math
import string
class Node( ):
    def __init__(self,name,x,y):
        self.name = name
        self.x = x
        self. y = y

    def get_distance(self):
        return math.sqrt(self.x**2+self.y**2)

    def get_profile(self):
        print(f'{self.name}, distance : {math.sqrt(self.x**2+self.y**2)}')

def get_store(name, x, y):
    return Node(name,x,y)

if __name__ == '__main__' :

    store =[get_store(i,random.randint(1,100),random.randint(1,100)) for i in string.ascii_lowercase[:11]]
    store_distance = [i.get_distance() for i in store]
    store_idx_distance_sort = sorted([[i,d] for i,d in enumerate(store_distance)], key = lambda x : x[1])
    for idx, d in store_idx_distance_sort :
        store[idx].get_profile()

