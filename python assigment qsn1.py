distance=int(input("enter the distance that is to be travelled: "))
if(distance<3):
    print("Use bicycle")
elif(distance>=3 and distance<300):
    print("Use motorcycle")
else:
    print("Use super car")
