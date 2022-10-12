from RPSLS_player import RPSLS_player
import random

class P14498(RPSLS_player):

  def __init__(self):
    self.shoot_list = ['rock', 'paper', 'scissors', 'lizard', 'spock']
    self.how_to_win = {'rock' : 'paper', 'paper' : 'scissors', 'scissors' : 'spock', 'spock' : 'lizard', 'lizard' : 'rock'}
    self.competitor_shot_list = []

  def shoot(self):
    if random.random() < 0.6 or len(self.competitor_shot_list) < 3 :
      return random.choice(self.shoot_list)
    else :
      self.expected_competitor_shot = random.choice(self.competitor_shot_list)
      return self.how_to_win[self.expected_competitor_shot]
  
  def update(self, result: str, competitor_shot: str):
    self.competitor_shot_list.append(competitor_shot)
    if len(self.competitor_shot_list) == 6 :
      self.competitor_shot_list.pop(0)