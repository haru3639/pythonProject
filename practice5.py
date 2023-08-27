n=input("Enter a number")
n=int(n)
if n%2==0:
    print("Number is even")
else:
    print("Number is odd")

indian=["samosa","kachori","dal","naan"]
pakistani=["nihari","paya","karahi"]
bangladesi=["panta bhat","chorchori","fuchka"]

dish=input("Enter a dish name:")
if dish in indian:
    print(f"{dish} is indian")
elif dish in pakistani:
    print(f"{dish} is pakistani")
elif dish in bangladesi:
    print(f"{dish} is bangladesi")
else:
    print(f"Based on my limited knowledge, I don`t lnow which cuisine is {dish}")

print("Ternary operator demo")
n=input("Enter a number")
n=int(n)
messeage="Number is even" if n%2==0 else "Number is odd"
print(messeage)
