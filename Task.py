#10.4
class Element():
    def __init__(self,name,symbol,number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number
    def __str__(self):
        return f'{self.name}, {self.symbol}, {self.number}'

    def dump(self):
        print(f'{self.name}, {self.symbol}, {self.number}')

    def get_pro(self):
        return f'{self.__name}, {self.__symbol}, {self.__number}'
# obj=Element('hydrogen','h',1)
#
# #10.5
# el_dict={'name':'Hydrogen','symbol':'H','number':1}
# print(Element(el_dict['name'],el_dict['symbol'],el_dict['number']))
#
# #10.6
hydrogen=Element('hydrogen','h',1)
# hydrogen.dump()
#
# #10.7
# print(hydrogen)

#10.8
print(hydrogen.get_pro())