
C:int=299792458

def main():
    kilogram:float=float(input("Enter your mass in kg"))
    energy_in_joules:float=kilogram*(C**2)
    print(str(energy_in_joules)+"Joules of energy")


if __name__=="__main__":
    main()