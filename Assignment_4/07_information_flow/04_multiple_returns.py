


def get_data():
    first_name=input("Enter your first name: ")
    last_name=input("Enter your last name: ")
    email=input("Enter your email")
    return first_name,last_name,email


def main():
    data=get_data()
    print(data)


if __name__=="__main__":
    main()