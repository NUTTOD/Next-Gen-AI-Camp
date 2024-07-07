a, b, c = [float(e) for e in input("Type your number : ").split()]
if (a > b and a < c) or (a > c and a < b):
    print(f"Middle Number is {a}")
elif (b > a and b < c) or (b > c and b < a):
    print(f"Middle Number is {b}")
elif (c > a and c < b) or (c > b and c < a):
    print(f"Middle Number is {c}")