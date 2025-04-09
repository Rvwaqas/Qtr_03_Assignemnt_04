import random

def main():
    secret_guess=random.randint(1,99)

    guess=int(input("Enter your guess number"))

    while guess != secret_guess:
        if guess < secret_guess:
            print("Your guess is too low!")
        else:
            print("Your guess is too high!")
        guess=int(input("Again enter your guess number"))
    
    print(f"Congrats! The number was: {secret_guess}")

if __name__ == "__main__":
    main()