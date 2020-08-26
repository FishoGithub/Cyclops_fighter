import random

player_hit = 0
enemy_hit = 0



def game_over():
  print("\n\n G A M E   O V E R.")

def game_win():
  print("\n\n Y O U   W I N!")

def main():
  global player_hit
  global enemy_hit

  print("Welcome to cyclops fighting simulator!\n")
  answer = input("would you like to fight the cyclops? [Y.N]  ").lower().strip()

  if answer == "y":
    print("\nyou encounter a cyclops!!\n")
    print("if you hit the cyclops for higher damage then you can kill it!\n")
    answer = input("do you fight the cyclops? [Y,N]  ")
    if answer == "y":
      player_hit = random.randint(1, 8)
      enemy_hit = random.randint(1, 8)

      print("\nyou hit the cyclops for " + str(player_hit) + " damage!\n")
      print("the cyclops hits you for " + str(enemy_hit) + " damage!")
      if player_hit > enemy_hit:
        print("\n you beat the cyclops!")
        game_win()
      elif player_hit < enemy_hit:
        print("the cyclops hits you for more damage!")
        game_over()



main()