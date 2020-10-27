"""
Ezra Goldner, October 2020

It's impossible to create truly recursive functions in programming, so I had to create a repeating series of rounds, instead of a single round recursive like what you have in the problem.
"""

# Whether or not to write every elimination (can be painful to look at)
SHOW_ELIMINATIONS = False

# How many players are participating
n = 524

# How many seats are skipped each time
k = 1

# -- # -- # -- # -- # -- # -- #

# player object
class Player:
  def __init__(self, chair_number):
    self.eliminated = False
    self.chair_number = chair_number
  def elim(self):
    self.eliminated = True
  def is_alive(self):
    return not self.eliminated

# main function
def begin():
  player_array = []
  last = 0
  for chair_number in range(0, n):
    player_array.append(Player(chair_number + 1))
  while players_alive(player_array) > 1:
    (players, elim) = filter(player_array, last)
    player_array = players
    last = elim
  print("< final result >\n" + str(last_player(player_array).chair_number))

# process each round
def filter(player_array, last):
  last_elim = 0
  index = 0
  rearranged = rearrange(player_array, last)
  while index < len(rearranged):
    player = rearranged[index]
    if player.is_alive():
      chair = player.chair_number
      next_player = next_alive_player(player_array, chair)
      skips = 1
      while skips < k:
        skips += 1
        index += 1
        next_player = next_alive_player(player_array, next_player.chair_number)
      if next_player:
        if SHOW_ELIMINATIONS:
          print(player.chair_number, "eliminates", next_player.chair_number)
        player_array[next_player.chair_number - 1].elim()
        last_elim = next_player.chair_number - 1
    index += 1
  return (player_array, last_elim)

# count players that are still alive
def players_alive(player_array):
  players_alive = 0
  for player in player_array:
    if player.is_alive():
      players_alive += 1
  return players_alive

# collect last player alive
def last_player(player_array):
  for player in player_array:
    if player.is_alive():
      return player

# get the next player
def next_alive_player(player_array, chair_number):
  for player in player_array[chair_number - 1:] + player_array[:chair_number]:
    if player.is_alive() and player.chair_number != chair_number:
      return player

# rearrange players to start on the last chair
def rearrange(player_array, last):
  return player_array[last:] + player_array[:last]

begin()
