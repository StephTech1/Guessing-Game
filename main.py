print("Guessing The Number Game")
guess = 0

number = int(input("Please choose a number between 1 and 10:"))
if (number == 6):
  print("You guessed correctly!")
if (number != 6):
  print("You have 5 more chances.....")
while number >6:
  guess = guess +1
  print("You guessed too high!")
  break
while number <6:
  guess = guess -1
  print("You guessed too low!")
  break

number = int(input("Please choose a number between 1 and 10:"))
if (number == 6):
  print("You guessed correctly!")
if (number != 6):
  print("You have 4 more chances....")
while number >6 :
  guess = guess +1
  print("You guessed too high!")
  break
while number <6 :
  guess = guess -1
  print("You guessed too low!")
  break

number = int(input("Please choose a number between 1 and 10:"))
if (number == 6):
  print("You guessed correctly!")
if (number != 6):
  print("You have 3 more chances...")
while number >6 :
  guess = guess +1
  print("You guessed too high!")
  break
while number <6 :
  guess = guess -1
  print("You guessed too low!")
  break
  
number = int(input("Please choose a number between 1 and 10:"))
if (number == 6):
  print("You guessed correctly!")
if (number != 6):
  print("You have 2 more chances..")
while number >6 :
  guess = guess +1
  print("You guessed too high!")
  break
while number <6 :
  guess = guess -1
  print("You guessed too low!")
  break

number = int(input("Please choose a number between 1 and 10:"))
if (number ==  6):
  print("You have 1 more chance.")
while number >6 :
  guess = guess -1
  print("You guessed too high!")
  break
while number <6 :
    print("You guessed too low")
    break

number = int(input("Please choose a number between 1 and 10"))
if (number == 6):
  print("You guessed correctly!")
if (number != 6):
  print("This is your last chance!!")
while number >6:
  guess = guess +1
  print("You guessed too high!")
  break
while number <6 :
  print("You guessed too low")
  break