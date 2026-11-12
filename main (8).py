correct_otp = "1234"
attempts = 0

while attempts < 3:
    otp = input("Enter OTP: ")

    if otp == "":
        continue

    if otp == correct_otp:
        print("OTP Verified")
        break

    attempts += 1
    print("Wrong OTP")

else:
    print("Account Locked for 30 Minutes")


for attempt in range(3):
    otp = input("Enter OTP: ")

    if otp == "":
        pass
    elif otp == correct_otp:
        print("OTP Verified")
        break
    else:
        print("Wrong OTP")

else:
    print("Account Locked for 30 Minutes")


security_answer = "chennai"
attempts = 0

while attempts < 5:
    otp = input("Enter OTP: ")

    if otp == "":
        continue

    if otp == correct_otp:
        print("OTP Verified")
        break

    attempts += 1

    if attempts == 3:
        answer = input("Security Question Answer: ")

        if answer.lower() == security_answer:
            print("Two Extra Attempts Allowed")
            attempts = 3

else:
    print("Account Locked for 30 Minutes")