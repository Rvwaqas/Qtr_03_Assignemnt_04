

MIN_HEIGHT:int=50

def main():
    Height=float(input("Enter your height "))

    if(Height>=MIN_HEIGHT):
        print("""You're tall "enough" to ride!""")
    else:
        print("You're not tall enough to ride, but maybe next year!")



if __name__ == "__main__":
    main()