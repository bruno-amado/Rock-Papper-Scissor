#Rock Papper or Scissor Game
#Rock wins Scissor, Scissor wins Papper and Papper wins Rock
i = False

while (not i ):
   a = str(input("Enter Rock, Papper or Scissor: "))
   b = str(input("Enter Rock, Papper or Scissor: "))
   if a == b:
      print("Is a draw")
      if str(input("Do you want to play again?(Yes/No): ")) == "Yes":
         continue
      else:
         break
   elif a == "Papper" and b == "Rock":
      print("Player 1 wins")
      if str(input("Do you want to play again?(Yes/No): ")) == "Yes":
         continue
      else:
         break
   elif a == "Rock" and b == "Papper": 
      print("Player 2 Wins")
      if str(input("Do you want to play again?(Yes/No): ")) == "Yes":
         continue 
      else:
         break
   elif a == "Rock" and b == "Scissor": 
      print("Player 1 wins")
      if str(input("Do you want to play again?(Yes/No): ")) == "Yes":
         continue
      else:
         break
   elif a == "Scissor" and b == "Rock":
      print("Player 2 Wins")
      if str(input("Do you want to play again?(Yes/No): ")) == "Yes":
         continue  
      else:
         break
   elif a == "Papper" and b == "Scissor":
      print ("Player 2 wins")
      if str(input("Do you want to play again?(Yes/No): ")) == "Yes":
         continue
      else:
         break
   elif a == "Scissor" and b == "Papper":
      print("Player 1 wins")
      if str(input("DO you want to play again?(Yes/No): ")) == "Yes":
         continue 
      else:
         break
   else:
      print("Rock, Papper or Scissor")
      break


