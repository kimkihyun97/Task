import random
import time

dataAry = [random.randint(0, 999999) for _ in range(1000000)]
dataAry_sorted = sorted(dataAry)
target = random.randint(0,999999)

##sequential
cnt_se = 0
s=time.time()
for i in range(len(dataAry)):
    cnt_se += 1
    if dataAry[i] == target:
        break
e = time.time()
time_se = e-s
##binary
cnt_bi = 0
start, end = 0, len(dataAry_sorted) - 1
s=time.time()
while (start <= end):
    cnt_bi += 1
    if dataAry_sorted[start]==target or dataAry_sorted[end]==target : break

    mid = (start + end) // 2
    if dataAry_sorted[mid] == target: break
    if dataAry_sorted[mid] > target:
        start, end = start, mid - 1
    else:
        start, end = mid + 1, end
e = time.time()
time_bi = e-s

print("#비정렬 배열(100만개)-->",dataAry[:5],"~~~~",dataAry[-5:-1])
print("#정렬 배열(100만개)-->",dataAry_sorted[:5],"~~~~",dataAry_sorted[-5:-1])
print("찾을 값 : ",target)
print("순차검색(비정렬 데이터)-->",cnt_se,"회"," 시간 : ",time_se,"초")
print("이진검색(정렬 데이터)-->",cnt_bi,"회"," 시간 : ",time_bi,"초")