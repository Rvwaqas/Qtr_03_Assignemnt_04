
import random
def chaotic_counting():
    for i in range(10):
        curr_num = i + 1
        if done():
            return # this ends the function execution, so we'll get back to the main() function!
        print(curr_num)



def done():
    DONE_LIKELIHOOD=0.5
    if random.random() < DONE_LIKELIHOOD:
        return True
    return False

def main():
    
    chaotic_counting()
    print("I'm done")

if __name__ == "__main__":
    main()