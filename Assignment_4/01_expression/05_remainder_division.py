

def main():
    num1=int(input("Enter your First_Number"))
    num2=int(input("Enter your Second Number"))

    quotient=num1//num2
    remainder=num1%num2

    print(f'The result of division is {str(quotient)} and remainder is {str(remainder)}')


if __name__ == '__main__':
    main()