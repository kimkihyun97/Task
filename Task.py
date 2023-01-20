#10.2
class Thing2():
    def __init__(self,letter):
        self.letter = letter
    def __str__(self):
        return self.letter

ex=Thing2('abc')
print(ex)