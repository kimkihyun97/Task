#8.10
square={i:i**2 for i in range(10)}
print(square)
#8.11
set_odd=set([i for i in range(10) if i%2!=0])
print(set_odd)
#8.12
gen_word=(i for i in 'Got')
gen_num=(i for i in range(10))
def for_rotate(s):
    for i in list(s):
        print(i,end=' ')
for_rotate(gen_word)
for_rotate(gen_num)
