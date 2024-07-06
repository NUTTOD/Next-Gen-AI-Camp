a = int(input("Type your a : "))
b = int(input("Type your b : "))
c = int(input("Type your c : "))

x1 = (-b-((b*b-(4*a*c))**0.5))/2*a
x2 = (-b+((b*b-(4*a*c))**0.5))/2*a
print(x1, x2, sep=", ")