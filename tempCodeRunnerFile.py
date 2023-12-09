import re

def emailTest(email):


    valid = re.compile(r"^[a-zA-Z]+[0-9]*@gmail.[a-z]{2,3}$")

    if valid.match(email):
        print("Valid email")
    else:
        print("Invalid email")

        return 


email = input("Enter your email :\t")
emailTest(email)