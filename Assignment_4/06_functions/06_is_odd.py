



def main():
    for i in range(10):
        if is_old(i):
            print(f"Its old {i}")
        else:
            print(f"its even {i}")
        
    
def is_old(num):
    remainder=num%2
    return remainder==1



if __name__=="__main__":
    main()