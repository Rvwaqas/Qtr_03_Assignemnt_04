import random


High_NUM=6
def die():
    val1=random.randint(1,High_NUM)
    val2=random.randint(1,High_NUM)
    print(f'Total dice {val1+val2}')


def main():
    die()
    die()
    die()
    print("These are your numbers in dice")


if __name__=="__main__":
    main()