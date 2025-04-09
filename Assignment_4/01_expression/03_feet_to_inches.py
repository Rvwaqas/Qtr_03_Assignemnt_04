

INCHES_IN_foot:int=12

def main():
    feet:float=float(input('Enter your feet'))
    inches=(feet*INCHES_IN_foot)
    print(f'This is {inches} in inches')


if __name__=='__main__':
    main()