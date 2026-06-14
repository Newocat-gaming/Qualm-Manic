
default enemy_void = Player(name = "Void", image = "", hp = 100, stanima = 2, strength = 1, mana = 10, hostile = True, icon_pos = (), icon_last_pos = (), icon = "enemy_dot", icon_show = True, icon_move = True, history = [])
default enemy_empty = Player(name = "", image = "", hp = 100, stanima = 2, strength = 1, mana = 10, hostile = True, icon_pos = (), icon_last_pos = (), icon = "enemy_dot", icon_show = True, icon_move = True, history = [])

default enemy_void3 = Player(name = "Void3", image = "", hp = 100, stanima = 2, strength = 1, mana = 10, hostile = True, icon_pos = (), icon_last_pos = (), icon = "enemy_dot", icon_show = True, icon_move = True, history = [])
default enemy_void2 = Player(name = "Void2", image = "", hp = 100, stanima = 2, strength = 1, mana = 10, hostile = True, icon_pos = (), icon_last_pos = (), icon = "enemy_dot", icon_show = True, icon_move = True, history = [])
default enemy_1 = Player(name = "", image = "", hp = 100, stanima = 2, strength = 1, mana = 10, hostile = True,  icon_pos = (), icon_last_pos = (), icon = "enemy_dot", icon_show = True, icon_move = True, history = [])
default enemy_2 = Player(name = "", image = "", hp = 100, stanima = 2, strength = 1, mana = 10, hostile = True,  icon_pos = (), icon_last_pos = (), icon = "enemy_dot", icon_show = True, icon_move = True, history = [])
default enemy_3 = Player(name = "", image = "", hp = 100, stanima = 2, strength = 1, mana = 10, hostile = True,  icon_pos = (), icon_last_pos = (), icon = "enemy_dot", icon_show = True, icon_move = True, history = [])
default enemy_4 = Player(name = "", image = "", hp = 100, stanima = 2, strength = 1, mana = 10, hostile = True,  icon_pos = (), icon_last_pos = (), icon = "enemy_dot", icon_show = True, icon_move = True, history = [])
default enemy_5 = Player(name = "", image = "", hp = 100, stanima = 2, strength = 1, mana = 10, hostile = True,  icon_pos = (), icon_last_pos = (), icon = "enemy_dot", icon_show = True, icon_move = True, history = [])
default enemy_6 = Player(name = "", image = "", hp = 100, stanima = 2, strength = 1, mana = 10, hostile = True,  icon_pos = (), icon_last_pos = (), icon = "enemy_dot", icon_show = True, icon_move = True, history = [])





init python:
    import random

default enemies_spawn = 0

default enemies_list = []
default enemies_list_names = []

default empty_enemies = []

label enemies_start:

    if map_number == 1:
        $ enemies_spawn = random.randint(1,3)
        if enemies_spawn == 1:
            $ enemies_list = [
                enemy_void,
                # enemy_empty,
                # enemy_empty,
                # enemy_empty,
                # enemy_empty,
                # enemy_empty,
                # enemy_empty,
                # enemy_empty,
                # enemy_empty,
                # enemy_empty,
            ]
            
        elif enemies_spawn == 2:
            $ enemies_list = [
                enemy_void,
                enemy_void2,
                # enemy_empty,
                # enemy_empty,
                # enemy_empty,
                # enemy_empty,
                # enemy_empty,
                # enemy_empty,
                # enemy_empty,
                # enemy_empty,
            ]
            
        elif enemies_spawn == 3:
            $ enemies_list = [
                enemy_void,
                enemy_void2,
                enemy_void3,
                # enemy_empty,
                # enemy_empty,
                # enemy_empty,
                # enemy_empty,
                # enemy_empty,
                # enemy_empty,
                # enemy_empty, 
            ]

        ###
        $ enemy_void.icon_pos = tile_1.icon_pos
        $ enemy_void2.icon_pos = tile_1.icon_pos
        $ enemy_void3.icon_pos = tile_1.icon_pos

        ###
        $ enemy_void.icon_last_pos = tile_1.icon_pos
        $ enemy_void2.icon_last_pos = tile_1.icon_pos
        $ enemy_void3.icon_last_pos = tile_1.icon_pos

        ###
        $ enemy_void.history.extend([tile_1.name, tile_1.name])
        $ enemy_void2.history.extend([tile_1.name, tile_1.name])
        $ enemy_void3.history.extend([tile_1.name, tile_1.name])


    $ x = 0
    while x < enemies_spawn:

        $ enemies_list_names.append(enemies_list[x].name)

        $ x += 1
    


    jump turn_order_start

