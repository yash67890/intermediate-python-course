import random

def main():
  dice_rolls =int(input(' dice would you like to roll?  '))
  dice_size= int(input('how many sides are the dice?  ')) 
  dice_sum=0
  for i in range(0,dice_rolls):
    roll = random.randint(1,dice_size)
    dice_sum += roll
    if roll == 1:
      print(f'U rolled a {roll}!Critical Fail')
    elif roll == dice_size :
      print(f"U rolled a {roll}!! Critical SUCCESS!")
    else:  
      print(f'You rolled a {roll}')
  print(f'You rolled {dice_sum}')

if __name__== "__main__":
  main()
