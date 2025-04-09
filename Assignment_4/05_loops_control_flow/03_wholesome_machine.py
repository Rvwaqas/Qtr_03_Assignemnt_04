

affirmation:str="I am capable of doing anything I put my mind to"

def main():
    print(f"Please enter the following affirmation {affirmation}")
    user_feedback=input()
    while user_feedback != affirmation:
        print("That was not the affirmation.")
        print("Please type the following affirmation: " + affirmation)
        user_feedback = input()
    
    print("That is correct! :)")

if __name__ == "__main__":
    main()