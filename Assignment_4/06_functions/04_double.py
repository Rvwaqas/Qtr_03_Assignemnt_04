


def get_val(user_val):
    return user_val*2


def main():
    user_val=int(input("Enter your value"))
    val=get_val(user_val)
    print(f'your number after multiply is {val}')


if __name__=="__main__":
    main()