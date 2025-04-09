
def get_int_list():
    lst=[]
    user_int=input("Enter your integer value")
    while user_int !="":
        lst.append(int(user_int))
        user_int=input("Enter your integer")
    return lst

def counter(lst):
    count=0
    for i in lst:
        if i%2==0:
            count+=1
    
    print(lst)
    print(count)


def main():
    lst=get_int_list()
    counter(lst)



if __name__=="__main__":
    main()