class Queue():

    def __init__(self,data):
        self.data = data
        self.size = len(data)
        self.queue = [None for _ in range(self.size)]
        self.front = -1
        self.rear = -1

    def IsQueueFull(self):
        if self.rear == self.size-1 : return True
        else : return False

    def IsQueueEmpty(self):
        if self.front == self.rear : return True
        else : return False

    def enQueue(self):
        if self.IsQueueFull() :
            print('queue is full')
            return
        for i in self.data :
            self.rear+=1
            self.queue[self.rear] = i

    def deQueue(self):
        if self.IsQueueEmpty() :
            print("queue is empty")
            return
        self.front += 1
        data = self.queue[self.front]
        self.queue[self.front] = None

        for i in range(self.front, self.rear+1) :
            self.queue[i-1] = self.queue[i]
            self.queue[i] = None
        self.front = -1
        self.rear-=1

        return data

    def peek(self):
        if self.IsQueueEmpty() :
            print('queue is empty')
            return
        return self.queue[self.front+1:]

if __name__ == "__main__" :
    data = ['정국','뷔','지민','진','슈가']
    que = Queue(data)
    que.enQueue()
    print("대기 줄 상태 : ",end='')
    print(que.peek())

    for _ in range(que.rear) :

        print(f'{que.deQueue()}님이 식당에서 나갔습니다. ')
        print(f'대기 줄 상태 : {que.peek()}')
    print('영업 종료')