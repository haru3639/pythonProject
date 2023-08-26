rent=8000
petrol=500.5
groceries=2050.5
print(rent)
total=rent+petrol+groceries

gabbar="amjad khan"
jay="amitabh"
thakur="sanjivkumar"

print("actors in sholeys:",gabbar,jay,thakur)

print(type(rent))
print(type(groceries))
print(type(gabbar))

#boolean
learn_python=True
learn_fortran=False

# variable naming rules
# no keywords: example True, for
# no special characters: foo+bar
# they must begin with a letter or _
# other characters can be letters (a to z, A to Z) or numbers (0 to 9)
# names are case sensitive

bade_bhai=10
bade_Bhai=5
print(bade_bhai)
print(bade_Bhai)

# above naming convention is called snake_case

# in python you can assign variable any value, not like strict typed language where
# you have to declare data type of a variable in advance

foo=5
foo="jalebi"
bar=foo
print("bar id",id(bar))
print("foo id",id(foo))
bar="samosa"
foo="kachodi" # at this point nothing is point to jalebi object and it will be garbage collected