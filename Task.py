#8.1
e2f={'dog':'chien','cat':'chat','walrus':'morse'}
#8.2
print(e2f['walrus'])
#8.3
f2e={v:k for k,v in e2f.items()}
#8.4
print(f2e['chien'])
#8.5
for k,v in e2f.items():
    print(k,v)
