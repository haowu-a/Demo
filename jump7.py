for i in range(1,101):
    jump=i
    one=jump%10
    ten=jump//10
    million=jump//100
    if one!=7 and ten!=7 and million!=7:
            if jump % 7 != 0:
                print(jump)
