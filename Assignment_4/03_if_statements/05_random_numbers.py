
import random


N_NUMBER=10
MIN_VALUE=1
MAX_VALUE=100

def main():
    for i in range(N_NUMBER):
        randomValue=random.randint(MIN_VALUE,MAX_VALUE)
        print(randomValue)
        
    

if __name__ == '__main__':
    main()