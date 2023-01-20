#10.4
class Element():
    def __init__(self,name,symbol,number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def __str__(self):
        return f'{self.name}, {self.symbol}, {self.number}'

    def dump(self):
        print(f'{self.name}, {self.symbol}, {self.number}')
obj=Element('hydrogen','h',1)

#10.5
el_dict={'name':'Hydrogen','symbol':'H','number':1}
print(Element(el_dict['name'],el_dict['symbol'],el_dict['number']))

#10.6
hydrogen=Element('hydrogen','h',1)
hydrogen.dump()

#10.7
print(hydrogen)
