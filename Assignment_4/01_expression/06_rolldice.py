import random

NUM_SIDES:int=6

def main():
    dice1=random.randint(1,NUM_SIDES)
    dice2=random.randint(1,NUM_SIDES)

    Total_Number=dice1+dice2

    print(f'Dice 1: {str(dice1)} Dice 2: {str(dice2)} Total: {str(Total_Number)}')



if __name__ == '__main__':
    main()
    
