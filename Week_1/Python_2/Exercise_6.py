size = input("Select your size S,M,L : ")
cheese_edge = input("Want cheese edge Y/N : ")
extra = input("Want Extra Y/N : ")
psize1, psize2, psize3 = [99, 199, 299]

if (size == "S"):
    if (cheese_edge == "Y"):
        psize1 += 20
    if (extra == "Y"):
        psize1 += 20
    print(f"Total Price is {psize1}")

if (size == "M"):
    if (cheese_edge == "Y"):
        psize2 += 30
    if (extra == "Y"):
        psize2 += 20
    print(f"Total Price is {psize2}")

if (size == "L"):
    if (cheese_edge == "Y"):
        psize3 += 40
    if (extra == "Y"):
        psize3 += 20
    print(f"Total Price is {psize3}")