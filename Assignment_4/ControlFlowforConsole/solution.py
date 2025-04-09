import random

Num=5

def main():
    score=0

    for i in range(Num):
        print("Round",i+1)
        computer_number=random.randint(1,100)
        user_number=random.randint(1,100)
        user_input=input("Enter your guest its higher or lower")
        higher_and_correct=user_input=="higher" and user_number>computer_number
        lower_and_correct=user_input=="lower" and user_number<computer_number
        if higher_and_correct or lower_and_correct:
            print(f"your guess is correct and computer guess is  {computer_number}")
            score+=1
        else:
            print(f"Your are incorrect and computer guest is {computer_number}")
        
        print(f'your score is {score}')


main()

