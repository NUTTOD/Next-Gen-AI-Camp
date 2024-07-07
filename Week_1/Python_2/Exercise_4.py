x1, x2, x3, x4, x5 = [int(e) for e in (input("Type yout number : ").split())]
if (x1 > x2):
    print(False)
elif (x2 > x3):
    print(False)
elif (x3 > x4):
    print(False)
elif (x4 > x5):
    print(False)
elif (x1 < x2 < x3 < x4 < x5):
    print(True)