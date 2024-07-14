str = str(input("Type your str : "))
lst = list(str)
upper = 0
lower = 0

for i in lst:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1
print(lower)
print(upper)