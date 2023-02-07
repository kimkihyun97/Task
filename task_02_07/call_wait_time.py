import queue
import re
def time_table(time) :

    du = int(re.findall('[0-9]+' ,time.split('/')[0])[0])
    return du

if __name__=="__main__" :
    times = ['9min/사용','3min/고장','4min/환불','3min/고장']
    que_time = queue.Queue([None])
    q = que_time.queue
    total = 0
    print(f'귀하의 예상 대기 시간은 {total}분 입니다. ')
    print(f'현재 대기 콜 --> {q} ')
    for time in times :
        q += [time]
        total +=time_table(time)
        print(f'귀하의 예상 대기 시간은 {total}분 입니다. ')
        print(f'현재 대기 콜 --> {q} ')
