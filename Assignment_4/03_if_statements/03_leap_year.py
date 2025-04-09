


def main():
    year =int(input("Enter a year: "))

    if(year % 4==0 and(year % 100 !=0 or year % 400 ==0)):
        print(f"This is leap year! {year}")
            
    else:
        print(f"This is not leap year! {year}")


if __name__ == "__main__":
    main()