mithai=['halva','kheer','jalebi','gulab jamun']
print(mithai)
print(type(mithai))
print(mithai[0])
print(mithai[1])
print(mithai[-1])
print(mithai[1:3])
print(mithai[:2])
print(mithai[2:])
print(mithai[-4:])
print(len(mithai))
print('halva' in mithai)
print('samosa' in mithai)
mithai.append('laddu')
print(mithai)
tikha=['samosa','sev']
print(tikha)
food=mithai+tikha
print(food)
mithai[0]='peda'
print(mithai)
mithai[0:2]=['samosa']
print(mithai)
mithai[0:2]=[3,5,6,7,8,9]
print(mithai)
print(dir(mithai))