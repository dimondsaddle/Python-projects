class Player(object):
    def __init__(self, name, max_hp, moves):
      self.name = name
      self.max_hp = max_hp
      self.hp = max_hp
      self.moves = moves
# getters
    def get_name(self):
      return self.name

    def get_max_hp(self):
      return self.max_hp
      
    def get_hp(self):
      return self.hp
      
    def get_moves(self):
      return self.moves
# setters
    def set_name(self,new_name):
      self.name = new_name
      
    def set_max_hp(self,new_max_hp):
      self.max_hp = new_max_hp 
    
    def set_hp(self,new_hp):
      self.hp = new_hp
    
    def set_moves(self,new_moves):
      self.moves = new_moves

    def change_hp(self,points):
      self.hp -= points  # make sure it doesn't go above max_hp
    
    
    