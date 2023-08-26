food='samosa'
print(food[0])
print(food[-1])
print(food[0:2])
print(food[:2])
print(food[-3:-1])
print(food[-3:])
print(len(food))
myfood='samosa,jalebi'
print('samosa' in myfood)
print('biryani' in myfood)
print('biriyani' not in myfood)
myfood.replace('samosa','biryani')
print(myfood)
print(myfood.upper())
print('ABC'.lower())
print(dir(myfood))
s='145'
print(s.isdigit())
print('145a'.isdigit())
print(myfood)
print(myfood.index('jalebi'))
states=29
text='total states in india:'
print(text+str(states))
text="let's learn python"
print(text)
dialog='''kitne aadami the?
sardar:do'''
print(dialog)
s='hey\nbro'
print(s)
s='hey\tbro'
print(s)
first='sachin'
last='tendulkar'
print('The best cricket player:',first+''+last)
print(f'The best cricket player{first} {last}')