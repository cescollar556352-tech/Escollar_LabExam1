#towerofhanoiEscollar
def toh(n, source, target, aux):
    if n == 1:
        print(f"Move values 1 from {source} to {target}")
        return
    toh(n - 1, source, aux, target)
    print(f"Move values {n} from {source} to {target}")
    toh(n - 1, aux, target, source)

try: 
    n = int(input("Input number of values: "))

    if n <= 0:
        print("Error! Please enter positive integers greather than zero. :) ")
    else:
        print(f"\nThe number of sequence moves for {n} values: ")
        toh(n, 'A', 'C', 'B')

except ValueError:
    print("Error! Invalid input. Please enter an integer.")       



