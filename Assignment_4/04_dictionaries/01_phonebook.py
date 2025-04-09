


def get_PhoneBook():
    phonebook={}
    while True:
        name =input('Enter the name' )
        if name=='':
            break
        number=input('Enter the number')
        phonebook[name]=number
    
    return phonebook


def print_phoneBook(phone_book):
    for name,number in phone_book.items():
        print(f'name is {name} and number is {phone_book[name]}')


def loop_numbers(phone_book):
    while True:
        name=input("Enter your name")
        if name=='':
            break
        if name in phone_book:
            print(f'{name}: {phone_book[name]}')

def main():
    phone_book=get_PhoneBook()
    print_phoneBook(phone_book)
    loop_numbers(phone_book)


if __name__=="__main__":
    main()