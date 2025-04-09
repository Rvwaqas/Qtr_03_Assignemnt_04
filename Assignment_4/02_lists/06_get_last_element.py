
def get_last_ele(lst):
    print(lst[len(lst)-1])



def get_lst():
    lst=[]
    ele=input("Enter your element or enter ")
    while ele !='':
        lst.append(ele)
        ele=input("Enter your element or enter ")
    return lst





def main():
    lst=get_lst()
    get_last_ele(lst)


if __name__=="__main__":
    main()