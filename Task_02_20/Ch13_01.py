import random
dataAry = ["바나나맛우유","레쓰비","츄파춥스","도시락","삼다수","코카콜라","삼각김밥"]
sellAry = [random.choice(dataAry) for _ in range(20)]
sellAry1=sorted(sellAry,key = lambda x:x)
sellAry3 = sorted(list(set(sellAry)),key = lambda x:x)
sellAry4 = list({item:sellAry.count(item) for item in sellAry3}.items())
print("#오늘 판매된 전체 물건(중복O,정렬X)-->",sellAry)
print("#오늘 판매된 전체 물건(중복O,정렬O)-->",sellAry1)
print("#오늘 판매된 전체 물건(중복X)-->",sellAry3)
print("#결산 결과==>",sellAry4)