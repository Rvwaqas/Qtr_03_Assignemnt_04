

Peturksbouipo_age=16
Stanlau_age=25
Mayengua_age=48


def main():
    age=int(input('Enter your age !'))

    if age<=15:
        print("You are not allowed to vote.")

    if age>=Peturksbouipo_age:
        print("You can vote in Peturksbouipo where the voting age is " + str(Peturksbouipo_age) + ".")
    else:
        print("You cannot vote in Peturksbouipo where the voting age is " + str(Peturksbouipo_age) + ".")


    if age>=Stanlau_age:
        print("You can vote in Stanlau where the voting age is " + str(Stanlau_age) + ".")
    else:
        print("You cannot vote in Stanlau where the voting age is " + str(Stanlau_age) + ".")


    if age>=Mayengua_age:
        print("You can vote in Mayengua where the voting age is " + str(Mayengua_age) + ".")
    else:
        print("You cannot vote in Mayengua where the voting age is " + str(Mayengua_age) + ".")


if __name__ == "__main__":
    main()