#Set a variable to be a random number between 1 and 10. Ask user to guess the number. Print an output if guessed correctly.  
# Extend the guessing game. Give the user 6 chances to guess the number using a while loop. Let them know if it is too high or too low

print("Guessing Game")
guess = 0

number = int(input("Please choose a number between 1 and 10:"))

if (number == 6):
  print("You guessed correctly!")

while number >6 :
  guess = guess +1
  print("You guessed too high!")
  break

while number <6 :
  guess = guess -1
  print("You guessed too low!")
  break