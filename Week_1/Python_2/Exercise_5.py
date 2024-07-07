x1, x2, x3, x4 = [int(e) for e in (input("Type yout number : ").split())]
number = [x1,x2,x3,x4]
print(sum(number)-min(number)-max(number))