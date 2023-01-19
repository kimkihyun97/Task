##9.16
def test_deco(func):
    try:
        print('start')
        print(func())
    finally:
        print('end')

@test_deco
def get_odds():
    return [i for i in range(10) if i%2!=0]

get_odds