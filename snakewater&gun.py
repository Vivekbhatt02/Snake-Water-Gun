#gun beats the snake,water beats the gun,snake beats the water
import random

computer_wins=0
user_wins=0
options=["snake","water","gun"]

while True:

  user_input=input("Choose between Snake/Water/Gun and q for exit").lower()
  if user_input=="q":
    break
  if user_input not in options:
   continue
  
  computer_guess=random.randint(0,2)
  computer_input=options[computer_guess]
  print("Computer picked",computer_input)

  if user_input=="gun" and computer_input=="snake":
    print("User Wins")
    user_wins+=1

  elif user_input=="water" and computer_input=="gun":
    print("User Wins")
    user_wins+=1

  elif user_input=="snake" and computer_input=="water":
    print("User Wins")
    user_wins+=1

  else:
    print("Computer Wins")
    computer_wins+=1

print("User Win",user_wins,"times.")
print("Computer Win",computer_wins,"times.")
print("Thankyou for Playing")