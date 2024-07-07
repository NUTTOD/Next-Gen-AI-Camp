choice = int(input("Select 1. (Rectangle) or 2. (Triangle): "))
if (choice == 1):
    width, length = [float(e) for e in (input("Type width, length : ").split(","))]
    print(f"Rectangle Area = {width*length}")
elif (choice == 2):
    base, height = [float(e) for e in (input("Type base, height : ").split(","))]
    print(f"Triangle Area = {0.5*base*height}")
else:
    print("Please Select a choise 1 or 2")