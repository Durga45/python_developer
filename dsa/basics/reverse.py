def reverse(num):
    reverse=0
    while num>0:
        lastDigit=num%10
        reverse=reverse*10+lastDigit
        num=num//10
    return reverse

mynum=4567
print(reverse(mynum))