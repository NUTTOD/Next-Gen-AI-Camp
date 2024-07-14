for number in range(1000, 3001):
    if ((number//1000)%2 == 0 and (number//100)%2 == 0 and (number//10)%2 == 0 and number%2 == 0):
        print(number,end=",")