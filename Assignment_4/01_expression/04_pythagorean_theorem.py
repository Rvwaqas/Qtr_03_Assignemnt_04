import math


def main():
    AB:float=float(input("Enter the length of AB"))
    AC:float=float(input("Enter the length of AC"))
    BC:float=float(math.sqrt(AB)+ math.sqrt(AC))
    print(BC)


if __name__ == '__main__':
    main()