# #Task 5.4
# letter="""Dear {} {},
#
# Thank you for your letter. we are sorry that our {} {} in your
# {}. please note that it should never be used in a {}, especially near any
# {}.
# send us your receipt and {} for shipping and handling. We will send you another
# {} that, in our tests, is {}% less likely to have {}.
#
# Thank you for your support.
# sincerely
# {}
# {}"""
# print(letter.format('Mr','kim','electric light','explode','room','room','cats','amount of damage',"electric light",'100','explode',
#                     'Hans','manger'))

#Task 5.6~5.8
# % formatting
print('%sy Mc%sface' %('Duck','Duck') )
print('%sy Mc%sfae' %('gourd','gourd'))
print('%sy Mc%sfae' %('Spitz','Spitz'))
#format()
print('{}y Mc{}face'.format('Duck','Duck') )
print('{}y Mc{}fae' .format('gourd','gourd'))
print('{}y Mc{}fae'.format('Spitz','Spitz'))
#f-formating
for i in ['Ducky','Gourd','Spitz']:
    print(f'{i}y Mc{i}face')

