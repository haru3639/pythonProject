bharat_expenses=[20,30,45]
bilal_expenses=[45,67,34]

total=0
for item in bilal_expenses:
    total+=item
print("Bilal`s total:",total)

total=0
for item in bilal_expenses:
    total+=item
print("Bilal`s total:",total)

def find_total(exp):
    '''
    This function takes list of numbers as input and returns sum of that list
    :param exp: input list
    :return: total sum
    '''
    total=0
    for item in exp:
        total+=item
    return total

bharat_total=find_total(bharat_expenses)
print("Bharat`s total:",bharat_total)

print(help(find_total))
def cylinder_volume(radius,height=1):
    print("radius is:",radius)
    print("height is:",height)
    area=3.14*(radius**2)*height
    return area

r=5
h=10
print(cylinder_volume(height=h,radius=r))

r=5
h=10
print(cylinder_volume(radius=r))
