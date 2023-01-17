#8.13
key_candid=('optimist','pessiist','troll')
value_candid=('The glass is half full','The glass is half empty','How did you get a glass')
dic_zip={x:y for x,y in zip(key_candid,value_candid)}
#8.14
title=['Creature of Habit','Crewel Fate']
plots=['A num turns into a monster','A haunted yarn shop']
movies={x:y for x,y in zip(title,plots)}
print(movies)