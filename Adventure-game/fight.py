from guizero import Box, PushButton
from random import randint


def executeMove(app, movename, player, opponent):
    moves = player.get_moves()
    dmg = moves[movename]["dmg_value"]
    dev = moves[movename]["deviation"]
    dmg += randint(-1 * dev, dev)
    player.change_hp(dmg, opponent)
    
    if opponent.get_hp() > 0:
        return execute_opponent_move(app, player, opponent)
    else:
        app.destroy()


def execute_opponent_move(app, player, opponent):
    damage = opponent.pick_move()
    opponent.change_hp(damage, player)
    return app.destroy()


def fight(app, player, opponent):
    moves = player.get_moves()
    move_names = [keys for keys in moves.keys()]

    # Set up GUI for player to select move
    master_box = Box(app, align="bottom", width="fill")
    button_box1 = Box(master_box, width="fill")
    button_box2 = Box(master_box, width="fill")
    for i in range(len(move_names)):
        args = [app, move_names[i], player, opponent]
        # First two buttons go in their own box for correct ordering in the GUI
        if i < 2:
            PushButton(button_box1, text=move_names[i], command=executeMove, args=args, width="28", align="left")
        else:
            PushButton(button_box2, text=move_names[i], command=executeMove, args=args, width="28", align="left")


# def fight(app, player, opponent):
#     moves = player.get_moves()
#     move_names = [keys for keys in moves.keys()]

#     # Set up GUI for player to select move
#     master_box = Box(app, align="bottom")
#     player_box = Box(master_box, align="bottom")
#     buttons = []
#     for i in range(len(move_names)):
#         button = PushButton(player_box, text=move_names[i], command=executeMove, args=[app,move_names[i],player,opponent])
#         buttons.append(button)
