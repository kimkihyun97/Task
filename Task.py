import random
import string
def stoneAry():
    stones = [i for i in string.ascii_lowercase[:5]]
    go_to_sanckhouse = []
    for _ in range(len(stones)) :
        stone= stones[random.randint(0,4)]
        while stone in go_to_sanckhouse :
            stone = stones[random.randint(0,4)]
        go_to_sanckhouse.append(stone)
    return go_to_sanckhouse



if __name__ == "__main__" :
    go_to_sanckhouse = stoneAry()
    print("go to snack house :", end = ' ')
    for i in go_to_sanckhouse :
        if i == go_to_sanckhouse[-1] : print(i)
        else : print(i+" ->", end =' ')
    print("go to my home :",end =' ')
    for i in go_to_sanckhouse[::-1] :
        if i == go_to_sanckhouse[0] : print(i)
        else : print(i+" ->", end =' ')

