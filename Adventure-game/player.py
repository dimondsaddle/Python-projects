from random import randint, choice
from helpers import open_json


class Character(object):
    def __init__(self, name, max_hp):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.moves = open_json(self.name + ".json")

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
    def set_name(self, new_name):
        self.name = new_name

    def set_max_hp(self, new_max_hp):
        self.max_hp = new_max_hp

    def set_hp(self, new_hp):
        self.hp = new_hp
        if self.hp < 1:
            self.hp = 0
        elif self.hp > self.max_hp:
            self.hp = self.max_hp

    def set_moves(self, new_moves):
        self.moves = new_moves

    def change_hp(self, points, opponent):
        if points > 0:
            opponent.set_hp(opponent.get_hp() - points)
        else:
            self.set_hp(self.get_hp() - points)

    def pick_move(self):
        moves = self.get_moves()
        move_list = list(moves.keys())
        chosen_move = choice(move_list)  # choice from random
        pick = moves[chosen_move]
        base_dmg = pick["dmg_value"]
        deviation = pick["deviation"]
        dmg = base_dmg + randint(-1*deviation, deviation)
        return dmg


class Player(Character):
    def __init__(self, name, max_hp, voice_line):
        super().__init__(name, max_hp)
        self.voice_lines = voice_line
        self.games_won = 0

    # getters
    def get_voice_lines(self):
        return self.voice_lines

    def get_games_won(self):
        return self.games_won

    # setters
    def set_voice_lines(self, new_voice_lines):
        self.voice_lines = new_voice_lines

    def set_games_won(self, new_games_won):
        self.games_won = new_games_won

    def pick_move(self):
        moves = self.get_moves()
        return moves

    def speak(self):
        pick = randint(0, len(self.voice_lines)-1)
        return self.voice_lines[pick]
