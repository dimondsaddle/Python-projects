from player import Player, Character
from helpers import save_json, open_json
from random import randint
from fight import fight
from guizero import App, Text, PushButton, ButtonGroup


def new_text():
    text = ["Welcome to our adventure game.\n\n",
            "You will need to defeat\nevery other combatant\nif you want to emerge victorious",
            "Which fighter you choose could be the difference\nbetween a great victory\nand a crushing defeat",
            "choose well\n\n"]
    index = text.index(top_text.value)
    try:
        top_text.value = text[index + 1]
    except IndexError:
        app.destroy()


def player_select():
    app.destroy()


def between_battle_button():
    if response.value == "It was a hard fought battle":
        response.value = next_text
    elif response.value == next_text:
        response.value = f"You have {len(character_list)} left to defeat"
    else:
        app.destroy()


def load_json():
    save = open_json("game")


fight_time = False
pikachu = Character("pikachu", 100)
guy = Character("guy", 120)
brock = Character("brock", 140)
misty = Character("misty", 100)

# VARIABLES TO SAVE
player_pikachu = Player("pikachu", 100, ["pika", "pika pika"])
player_guy = Player("guy", 120, ["Hey how's it going", "Why am I fighting?"])
player_brock = Player("brock", 140, ["I fight dirty"])
player_misty = Player("misty", 100, ["come and fight me"])
character_list = [pikachu, guy, brock, misty]  # LIST OF ENEMIES, CHANGES
player_list = [player_pikachu, player_guy, player_brock, player_misty]
defeated = []
name = None
app = App()
top_text = Text(app, text="Welcome to our adventure game.\n\n")
# choice between 1 and 2 players is needed

next_button = PushButton(app, command=new_text, text="Next")

if name is None:
    app.display()

    app = App()

    pick_chara_button = ButtonGroup(app, options=[play.get_name() for play in player_list])
    choose = PushButton(app, command=player_select, text="Select")
    app.display()
    pick_chara = next((player for player in player_list if player.get_name() == pick_chara_button.value), None)

    name = pick_chara.get_name()
    app = App()
    hello_text = Text(app, text=f"You have chosen {pick_chara.get_name()}\n\n{pick_chara.speak()}")
    moves = pick_chara.get_moves()

    # Put in code to display the move's description by setting mid_text.Value#
    next_button = PushButton(app, command=player_select, text="next")
    app.display()
for chara in character_list:
    if chara.get_name() == name:
        character_list.remove(chara)

for play in player_list:
    if play.get_name() == name:
        current_player = play

win = True

while win:

    current_player.set_hp(current_player.get_max_hp())
    try:
        index = randint(0, len(character_list) - 1)
    except ValueError:
        break
    enemy = character_list.pop(index)
    # randomise by len then pop the value
    opponent = enemy.get_name()
    while True:  # while both player's heath > 0
        app = App()

        top_text = Text(app, text=f"{opponent}\nHP:{enemy.get_hp()}", align="top")

        mid_text = Text(app, text="")
        fight(app, current_player, enemy)
        bottom_text = Text(app, text=f"{name}\nHP:{current_player.get_hp()}\nWhat move would you like to use?",
                           align="bottom")

        app.display()
        our_hp = current_player.get_hp()
        their_hp = enemy.get_hp()

        if their_hp == 0 or our_hp == 0:
            break

    if our_hp < 1:
        win = False

    app = App()
    response = Text(app, text="It was a hard fought battle")
    defeated_2 = []
    if enemy.get_hp() == 0:
        defeated.append(enemy)
        for enemy in defeated:
            defeated_2.append(enemy.get_name())
        current_player.set_games_won(current_player.get_games_won() + 1)
    if win:
        next_text = f"{current_player.get_name()} emerged victorious"

    else:
        next_text = f"But you unfortunately fell in battle\n\nYou defeated {current_player.get_games_won()} opponents"

    next_but = PushButton(app, text="Next", command=between_battle_button)
    save_but = PushButton(app, text="Save", command=save_json, args=[player_list, defeated_2])
    app.display()

    if len(player_list) == 0:
        break

app = App()
ending_text = Text(app)
if current_player.get_games_won()==len(player_list)-1:
    ending_text.value = "You have defeated every opponent\nWell Done"
else:
    ending_text.value = "Better luck next time"
