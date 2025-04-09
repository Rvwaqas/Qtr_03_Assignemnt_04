



def in_range(n,low,high):
    if n>=low and n<=high:
        return True
    
    return False


def main():
    n=int(input("Enter a number"))
    low=int(input("Enter a low number"))
    high=int(input("Enter a high number"))

    if in_range(n,low,high):
        print(f"Your number {n} is in between low {low} and high {high}")
    else:
        print(f"Your number {n} is not in between low {low} to hight")



if __name__=="__main__":
    main()