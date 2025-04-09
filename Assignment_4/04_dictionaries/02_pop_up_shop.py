
def main():
    fruits={'apple':1.5,'durian': 50, 'jackfruit': 80, 'kiwi': 1, 'rambutan': 1.5, 'mango': 5}
    total_cost=0
    for fruit_Name in fruits:
        price=fruits[fruit_Name]
        amount=int(input(f'How many {fruit_Name} do you want to buy! '))
        total_cost+=(price*amount)
    
    print(f'Your total is ${str(total_cost)}')


if __name__=='__main__':
    main()