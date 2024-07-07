score = int(input("Type your score : "))

if (90 <= score <= 100):
    print("Your grade is A")
elif (85 <= score < 90):
    print("Your grade is B+")
elif (80 <= score < 85):
    print("Your grade is B")
elif (70 <= score < 85):
    print("Your grade is C+")
elif (60 <= score < 70):
    print("Your grade is C")
elif (55 <= score < 60):
    print("Your grade is D+")
elif (50 <= score < 55):
    print("Your grade is D")
elif (score < 50):
    print("Your grade is F")