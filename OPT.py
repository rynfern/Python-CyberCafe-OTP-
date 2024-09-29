import random
import string
import pickle
import smtplib
# Simple Mail Transfer Protocol
# An SMTP server is an application or computer that sends,
# receives and relays email. These servers typically use TCP on port 25 or 587.
# The port number identifies specific processes when an internet or network message
# is forwarded to a server. All network-connected devices come equipped with standardized
# ports that have an assigned number. Each number is reserved for certain protocols and
# their associated functions.
#An email server uses SMTP to send a message from an email client to another email server.
#The email server uses SMTP as a relay service to send the email to the receiving email server.

def checkUser(na):
    try:
        with open("Member.bin", "rb") as fileReader:
           while True:
                rec = pickle.load(fileReader)  # extract 1 record at a time
                if rec[0]==na:
                    return True
    except:
        return False

def saveUser(info):
    with open("Member.bin", "ba") as fileWriter:
        pickle.dump(info, fileWriter)

def registerUser():
    print("""

            =======================================
            !!!!!!!!!!Register Yourself!!!!!!!!
            =======================================
                                                """)


    while True:  # to check if there are more than one same id
        username = input("Input your username!!:")
        if checkUser(username)==False:
            break
        else:
            print(" username already taken! try again")

    passw = input("Input the password :")
    while True:
        age = int(input(" Enter age: "))
        if age>17:
            break
        else:
            print("You are too young to make an account! MUST BE AN ADULT.")

    while True:
        contact = int(input(" Enter contact: "))
        if 999999999<contact<10000000000:
            break
        else:
            print("Invalid contact no. MUST BE 10 DIGITS ONLY")


    saveUser([username,passw,age,contact])
    print("""
            ============================================
              Well Done!Registration Done Successfully
            ============================================

                                                """)
    x = input("enter any key to continue:")



def validateUser(na,pa):
    try:
        with open("Member.bin", "rb") as fileReader:
           while True:
                rec = pickle.load(fileReader)  # extract 1 record at a time
                if rec[0]==na and rec[1]==pa:
                    return True
    except:
        return False

# IF USER WANTS TO LOGIN

def validate(vt):
    if "/" not in vt:
        return False

    info = vt.split("/")
    try:
        mm = int(info[0])
        if 1 <= mm <= 12:
            return True
        else:
            return False
    except:
        return False


def generate_captcha():
    cac = ''
    for i in range(6):
        cac += random.choice(string.ascii_letters + string.digits)
    return cac

def login():
    print("""
            ==================================
              !!!!!!!!  Sign In  !!!!!!!!!!
            ==================================
                                                """)
    while True:  # to check if id exists
        un = input("Enter Username!!:")
        ps = input("Enter Password!!:")
        if validateUser(un,ps)==False:
            print(" Invalid User Name / Password ")
        else:
            break

    while True:
        print("""
            1. Billing Plan
            2. Sign Out

            """)

        a = int(input("ENTER YOUR CHOICE:"))
        if a == 1:
            while True:
                email = input("Please Enter your gmail.id")
                if "@gmail.com" in email:
                    break
                else:
                    print("This Email does not match a gmail account, please enter a GMAIL id")

            print("-" * 40)
            print("Duration         Fee         Duration")
            print("(hours)        (rupees)      (minutes)")
            print("-" * 40)
            print("  1               50            60")
            print("  1.50            75            90")
            print("  2               100           120")
            print("  2.50            125           150")
            print("  4               200           240")
            print("  5               240           300")
            print("-" * 40)


            while True:
                dur = float(input("Please Enter Decided Duration(1,1.5,2,2.5,4,5,)"))
                if dur == 1:
                    c = "50rs"
                    break
                elif dur == 1.50:
                    c = "75rs"
                    break
                elif dur == 2:
                    c = "100rs"
                    break
                elif dur == 2.5:
                    c = "125rs"
                    break
                elif dur == 4:
                    c = "200rs"
                    break
                elif dur == 5:
                    c = "250rs"
                    break
                else:
                    print("Sorry, your entry doesnt match the options, please type again correctly!")


            cn = input("Please Enter Card No.")
            nc = input("Please Enter Name Of Owner Of Card.")
            while True:
                vt = input("Card Valid Thruough mm/yy : (09/27)")
                if validate(vt) == True:
                    break

            cv = int(input("Please Enter Card CVV :"))
            print("a capcha code has been sent to this device, please type the code correctly to verify that youre not a robot.")
            while True:
                cac = generate_captcha()
                print(cac)
                cc = input("Please Enter Capcha-Code: ")
                if cc == cac:
                    while True:
                        otp = random.randint(100000, 999999)
                        otp = str(otp)
                        mail = smtplib.SMTP('smtp.gmail.com', 587)
                        mail.ehlo()
                        mail.starttls()
                        content = otp
                        sender = 'podarcybercafe@gmail.com'
                        receiver = email
                        password = 'mjoq mpyl odmb xhcb'
                        header = 'To:' + receiver + '\n' + 'From:' \
                                 + sender + '\n' + 'subject:OTP VERIFICATON!\n'
                        content = header + content
                        mail.login('podarcybercafe@gmail.com', 'mjoq mpyl odmb xhcb')
                        mail.sendmail(sender, receiver, content)
                        mail.close()

                        print("An OTP has been sent to your Gmail ID, Please enter the OTP TO confirm identity and complete the payment procedure.")
                        o = int(input("Please Enter OTP: "))
                        if str(o) == otp:
                            print("\n\n\nOTP has been verified!\n")
                            print("\nTRANSACTION COMPLETE. HERE IS YOUR BILL.\n\n")
                            print("-------------- BILL ---------------")
                            print("NAME : ",nc, "  EMAIL ID: ",email)
                            print("--------------------------------------")
                            print("HOURS: ",dur, "  NET BILL: ",c)
                            print("--------------------------------------")
                            print("\n\n\nWelcome to Cyber Cafe. Enjoy your time!")

                            break
                        else:
                            print("Wrong Entry please try again with a new otp")
                    break #to termiate the capch loop if everything is fine
                else:
                    print("Wrong Entry please try again with a new Capcha-code")

        elif a == 2:
            print("Signed Out Successfully")
            break
            # SIGN OUT

def mainMenu():
    print("""
            ================================
            Welcome To Python Cyber Cafe!
            ================================
        """)
    while True:
        print("""
                    1. New User
                    2. Login
                    3. Exit
              """)

        r = int(input("enter your choice:"))
        if r == 1:
            registerUser()
        elif r == 2:
            login()
        elif r==3:
            print("Thank You. Visit Again")
            break
        else:
            print("Invalid Choice")


mainMenu()
