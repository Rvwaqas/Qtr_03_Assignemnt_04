

Adult_age=18

def is_adult(user_ag):
    if user_ag>= Adult_age:
        return True
    
    return False




def main():
    user_ag=int(input("Enter your age"))
    if is_adult(user_ag):
        print(f"your age is {user_ag} and you are an adult")
    else:
        print(f"your age is {user_ag} and you are not an adult")


if __name__=="__main__":
    main()