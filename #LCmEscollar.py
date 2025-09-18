#LCmEscollar

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
        return(a * b) // gcd(a, b)


try: 
    x = int (input("Enter a value for x: "))
    y = int(input("Enter a value for y: "))

    if x <= 0 or y <= 0:
        print("Error! Please enter positive integers greater than zero. :) ")
    else: print(f"The LCM of {x} and {y} is = {lcm(x, y)}")

except ValueError:
    print("Invalid input. Please enter integers values only. :)")

