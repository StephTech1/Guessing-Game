print("Guessing Game")
guess = 0

number = int(input("Please choose a number between 1 and 10:"))

if (number == 6):
  print("You guessed correctly!")
if (number != 6):
  print("You have 5 more chances")

number = int(input("Please choose a number between 1 and 10:"))

while number >6 :
  guess = guess +1
  print("You guessed too high!")
  break
while number <6 :
  guess = guess -1
  print("You guessed too low!")
  break