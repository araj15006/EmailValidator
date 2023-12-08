def emailTest(email):
    special = 0
    valid = 0
    if (
        (len(email) >= 6)
        and (email[0].isalpha())
        and ("@" in email)
        and (email.count("@") == 1) 
        and (email.find(' ') == -1)
        and (email[-3] == "." or email[-4] == ".")
        and ((" .in" in email) or (".com" in email))
    ):
        for item in email:
            if not item.isalnum():
                special += 1
                if special > 2:
                    valid = 1
                    break
            else:
                valid = 0
        if valid == 1 :
            print("invalid")
        else:
            id,domain = email.split('@')
            for i in domain:
                if i.isupper():
                    valid = 1
                else :
                    valid = 0 
        print("valid email" if valid ==0 else "invalid email")
    else:
        print("Invalid email")


email = input("Enter the email: ")
emailTest(email)
