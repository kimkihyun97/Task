##9.16
##9.4
class OopsException(Exception):
    def __init__(self,msg):
        self.msg=msg
    def __str__(self):
        return self.msg

def putName():
    name=input('이름을 입력해주세요: ')
    if len(name)<3:
        raise OopsException('Caught an oops')
    print(name)

try:
    putName()
except OopsException as oop:
    print(oop)