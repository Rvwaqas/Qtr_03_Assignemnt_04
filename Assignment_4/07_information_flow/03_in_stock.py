


def fruit_in_stock(fruit):
    if fruit=='apple':
        return 2
    elif fruit=='mango':
        return 20
    elif fruit=='graps':
        return 300
    else:
        return 0


def main():
    fruit=input("Enter your fruits: ")
    stock=fruit_in_stock(fruit)
    if stock==0:
        print(f'{fruit} stock is empty')
    else:
        print(f'{fruit} stock is {stock}')


if __name__=="__main__":
    main()