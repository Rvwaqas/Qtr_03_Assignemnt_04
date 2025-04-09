



def dive(num):
    for i in range(10):
        count=i+1
        if num%count==0:
            print(count)



def main():
    val=int(input("Enter your value"))
    dive(val)

if __name__=="__main__":
    main()