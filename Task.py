#10.3
class Thing3():
    def __init__(self,letter):
        self.letter = letter
    def __str__(self):
        return self.letter
print(Thing3('xyz')) #객체 필요 없음