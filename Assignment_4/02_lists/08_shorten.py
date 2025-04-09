

MAX_NUM=3

def shorten(lst):
    while len(lst)>MAX_NUM:
        last_ele=lst.pop()
        print(last_ele)
    
    print('No more you remove elements')

def get_lst():
    lst=[]
    ele=input('Enter your value')
    while ele !='':
        lst.append(ele)
        ele=input('Enter your value and for stop press enter')
    return lst



def main():
    lst=get_lst()
    shorten(lst)

if __name__ == '__main__':
    main()