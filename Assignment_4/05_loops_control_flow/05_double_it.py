

def main():
    user_input=int(input("Enter your number"))

    while user_input<=100:
        print(user_input*2)
        user_input=int(input("Enter your number"))
    print("You excess the value greater then 100")

if __name__ == "__main__":
    main()