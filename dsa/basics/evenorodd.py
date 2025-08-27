def evenOrOdd(num):
    if num==0:
        return "please provide num > 0"
    if num%2==0:
        return "even"
    else:
        return "odd"
       


mynum=45
print(evenOrOdd(mynum))