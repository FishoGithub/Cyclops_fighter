import random

player_hit = 0
enemy_hit = 0

def main():
  global player_hit
  global enemy_hit

  print("Welcome to cyclops fighting simulator!\n")
  answer = input("would you like to fight the cyclops? [Y.N]  ").lower().strip()

  if answer == "y":
    print("\nyou encounter a cyclops!!\n")
    print("you have to hit the cyclops for 5 and higher to kill it, and the cyclops has to hit you for 5 and higher for you to die!\n")
    answer = input("do you fight the cyclops? [Y,N]  ")
    if answer == "y":
      player_hit = random.randint(1, 8)
      enemy_hit = random.randint(1, 8)

      print("\nyou hit the cyclops for " + str(player_hit) + " damage!\n")
      print("the cyclops hits you for " + str(enemy_hit) + " damage!")
    else:
      print("the cyclops eats you alive.")



main()