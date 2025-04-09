

def main():
    curr_val=int(input("Enter your number"))
    while curr_val<=100:
        update_val=curr_val*2
        print(update_val)
        curr_val=int(input('Enter your number'))
        
    print('Excess the given number limit')

main()