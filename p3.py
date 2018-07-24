import itertools
import random


def gen_rndtup(n):
    while True:
        yield(random.randint(1,n-1), random.randint(1,n-1))
        
def main():
    n = 7
    dice_roll = itertools.islice(gen_rndtup(7), 10)
    print(list(dice_roll))
    return

if __name__=='__main__':
    main()

