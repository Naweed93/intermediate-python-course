import random
def main():
    rolldice = int(input("how many times do you need to roll a dice? "))
    diceSide = int(input("and how many side that dice has? "))
    sum = 0
    for i in range(0,rolldice):
        rnd = random.randint(1,diceSide)
        if rnd == 1:
            print(f'you rolled {rnd}, better luck next time')
        elif rnd == diceSide:
            print(f'BINGO, you rolled {rnd}')
        else:
            print(f'You rolled a {rnd}')
        sum += rnd
    print(f'total dice number is {sum}')

if __name__== "__main__":
  main()
