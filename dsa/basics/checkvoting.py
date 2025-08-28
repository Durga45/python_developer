def votingEligibility(age):
    if age==0:
        return 1
    if age<18:
        print("not eligible")
    elif age>=18:
        print("eligible")
    else:
        print("age should be above 18 or equal to 18")

votingEligibility(45)