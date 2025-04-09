


def main():
    name=input("Enter your name!")
    gree=greeting(name)
    print(gree)

def greeting(name):
    return (f"Hello {name} & nice to meet you!")


if __name__=="__main__":
    main()