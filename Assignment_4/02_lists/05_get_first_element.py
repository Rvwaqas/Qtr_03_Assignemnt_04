


def get_first_ele(lst):
    print(lst[0])
    



def get_lst():
    lst=[]
    ele=input("Enter the element of list or press enter")
    while ele !='':
        lst.append(ele)
        ele=input("Enter the element of list or press enter")
    return lst




def main():
    lst=get_lst()
    get_first_ele(lst)


if __name__=="__main__":
    main()