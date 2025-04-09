

def add_number(numbers):

    total_number=0

    for number in numbers:
        total_number+=number
    
    return total_number


def main():
        numbers=[1,2,3,4,5]
        sum1=add_number(numbers)
        print(sum1)


if __name__=="__main__":
    main()