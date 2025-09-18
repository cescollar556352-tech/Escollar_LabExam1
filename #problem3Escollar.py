#problem3Escollar

print("Network Checking")

while True:
    try:
        mobilenum = input("\nEnter a mobile number: ")
        lengthnum = input(mobilenum)

        if lengthnum != 11:
            print("Please enter 11 digit number. :)")
            continue

        elif mobilenum[0:2] != "09":
            print("Invalid Mobile Number. Please try again. :)")
            continue

        else: 
            if mobilenum [0:3] == ["0913", "0914", "0920", "0921", "0928", "0929", "0930"]:
             print("The network of your mobile number is Smart.")

    except ValueError:
            print("Please Enter a valid mobile number. :)")