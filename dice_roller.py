import random
def main():
    rolldice = 2
    sum = 0
    for i in range(0,rolldice):
        rnd = random.randint(1,6)
        print(f'You rolled a {rnd}')
        sum += rnd
    print(f'total dice number is {sum}')

if __name__== "__main__":
  main()
