#7.11
import random as rd
start1=['fee','fie','foe']
rhymes=[
    ('flop','get a mop'),
    ('fope','turn the rope'),
    ('fa','get your ma'),
    ('fudge','call the judge'),
    ('fat','pet the car'),
    ('fog','walk the dog'),
    ('fun',"say we're done")
]
start2='someone better'
rd_rhy=rd.randint(0,6)
for i in start1:
    print(f'{i.capitalize()}!',end='')
print(f'{rhymes[rd_rhy][0].capitalize()}!')
print(f'{start2} {rhymes[rd_rhy][1]}')