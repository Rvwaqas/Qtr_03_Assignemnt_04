


def get_lst():
    user_number=[]
    while True:
        User_input=input("Enter your number")
        if User_input=='':
            break
        User_num=int(User_input)
        user_number.append(User_num)

        
    return user_number



def get_dct(user_number):
    dic={}

    for num in user_number:
        if num not in dic:
            dic[num]=1
        else:
            dic[num]+=1
        
    return dic



def get_count(dct):

    for i,c in dct.items():
        print(str(i) + " appears " + str(c) + " times.")




def main():
    user_number=get_lst()
    dct=get_dct(user_number)
    get_count(dct)


if __name__=="__main__":
    main()