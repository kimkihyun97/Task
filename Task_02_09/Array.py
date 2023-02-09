from collections import deque
class Classify():
    def __init__(self,ary):
        self.ary = ary

    def Sort(self):
        if len(self.ary) <=1 :
            print("Can't make group")
            return
        group =[]
        self.ary = sorted(self.ary , key= lambda x:x[1])
        queue = deque(self.ary)
        while queue :
            group.append([queue.popleft(),queue.pop()])
            if len(queue) ==1 :
                return group
        return group

class FindMeanValue():
    def __init__(self,ary):
        self.ary = ary

    def Sort(self):
        return sorted(self.ary,key=lambda x:x)

    def Mean(self):
        if len(self.ary) == 0 :
            print('Wrong array')
            return
        if len(self.ary) == 1 :
            return self.ary[0]

        ary = self.Sort()
        if len(ary)%2==0 :
            idx = len(ary)/2
            return ary[int(idx)]
        else :
            idx = len(ary)//2
            return ary[int(idx)]




if __name__ == "__main__" :
    score_ary = [['선미',88],['초아',99],['화사',71],['영탁',78],['영웅',67],['민호',92]]
    group= Classify(score_ary)
    print("11.1")
    print("## Group ##")
    for students in group.Sort() :
        print(f'{students[0][0]} : {students[1][0]}')
    print()
    print("11.2")
    nums = [55, 33, 250, 44, 88, 1, 67, 23, 199, 222, 38, 47, 155, 145, 20, 99]
    ary = FindMeanValue(nums)
    print('Unrefined array : ', nums)
    print("Refined array : ", ary.Sort())
    print("Mean value : ", ary.Mean())


