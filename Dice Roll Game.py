#Code made by Luke, Leonardo and Chibuikem

# defining the entire calculation 5
def main():
  #importing time sleep and random number maker
  import time
  import random
  num_players = int(input("How many people are rolling?: "))

  #insert into a list for easy recall
  numbers = []

  #Loop for a random interger between 1-6
  for player in range(1, num_players + 1):
    random_number = random.randint(1,6)
    numbers.append((player, random_number))
    print(f"\nPlayer {player} rolled: {random_number}")

    #give a bit of waiting time for rolls, easy to read and makes tension
    time.sleep(1)

  #Finding the winner
  max_score = 0
  winner = []

  for player, score in numbers:
    if score > max_score:
      max_score = score
      winner = [player]
    elif score == max_score:
      winner.append(player)

  if len(winner) == 1:
    print(f"\nPlayer {winner[0]} wins with a score of {max_score}!")
  else:
    print(f"\nIt's a tie with a score of {max_score}!")

#Calling main function
if __name__ == "__main__":
  main()