python early:
    class MapTile(store.object):
        def __init__(self, name = "", lock = False, locked = "", idle = "", hover = "", xpos = 0, ypos = 0, icon_pos = (), icon_t = "tile_icon_pos", unlock_tiles = [], attack_tiles = [],):
            self.name = name
            self.lock = lock
            self.locked = "map/" + locked + ".webp"
            self.idle = "map/" + idle + ".webp"
            self.hover = hover
            self.xpos = xpos
            self.ypos = ypos
            self.icon_pos = icon_pos
            self.icon_t = icon_t
            self.unlock_tiles = unlock_tiles
            self.attack_tiles = unlock_tiles + attack_tiles

default unlocked_tiles = []
default locked_tiles = []
default locked_tiles_temp = []

default map_number = 1
default number_of_tiles = 8

default number_of_players = 0
default number_of_empty_players = 0

default number_of_enemies = 0
default number_of_empty_enemies = 0

default total_number_of_players = 0

default in_combat = False

default turn_order_numb = 0
default current_player_turn = ""

default movement_turns = 0
default attack_turns = 0

default enemy_in_range = False
default attack_tiles = []

default act = False # if buttons can be pressed

default temp_tile_name = ""

###########

default tile_1 = map_1_tile_1
default tile_2 = map_1_tile_2
default tile_3 = map_1_tile_3
default tile_4 = map_1_tile_4
default tile_5 = map_1_tile_5
default tile_6 = map_1_tile_6
default tile_7 = map_1_tile_7
default tile_8 = map_1_tile_8
# default tile_9 = map_1_tile_9


default map_exits = []



image map_background:
    "images/Map/background.png"    


screen current_player():
    text "active: [current_player_turn]" xalign 0.5
    text "all [turn_order_names]" xalign 0.5 ypos 50


label pre_move:

    $ locked_tiles = []
    $ locked_tiles_temp =[]

    if active_player.history[-1] == tile_1.name:
        $ unlocked_tiles = tile_1.unlock_tiles
        $ attack_tiles = tile_1.attack_tiles
    elif active_player.history[-1] == tile_2.name:
        $ unlocked_tiles = tile_2.unlock_tiles
        $ attack_tiles = tile_2.attack_tiles
    elif active_player.history[-1] == tile_3.name:
        $ unlocked_tiles = tile_3.unlock_tiles
        $ attack_tiles = tile_3.attack_tiles
    elif active_player.history[-1] == tile_4.name:
        $ unlocked_tiles = tile_4.unlock_tiles
        $ uattack_tiles = tile_4.attack_tiles
    elif active_player.history[-1] == tile_5.name:
        $ unlocked_tiles = tile_5.unlock_tiles
        $ attack_tiles = tile_5.attack_tiles
    elif active_player.history[-1] == tile_6.name:
        $ unlocked_tiles = tile_6.unlock_tiles
        $ attack_tiles = tile_6.attack_tiles
    elif active_player.history[-1] == tile_7.name:
        $ unlocked_tiles = tile_7.unlock_tiles
        $ attack_tiles = tile_7.attack_tiles
    elif active_player.history[-1] == tile_8.name:
        $ unlocked_tiles = tile_8.unlock_tiles
        $ attack_tiles = tile_8.attack_tiles
    
    ###############################

    if active_player.history[-1] == tile_1.name: # -2
        $ active_player.icon_last_pos = tile_1.icon_pos
        
    elif active_player.history[-1] == tile_2.name:
        $ active_player.icon_last_pos = tile_2.icon_pos
        
    elif active_player.history[-1] == tile_3.name:
        $ active_player.icon_last_pos = tile_3.icon_pos
        
    elif active_player.history[-1] == tile_4.name:
        $ active_player.icon_last_pos = tile_4.icon_pos
        
    elif active_player.history[-1] == tile_5.name:
        $ active_player.icon_last_pos = tile_5.icon_pos
       
    elif active_player.history[-1] == tile_6.name:
        $ active_player.icon_last_pos = tile_6.icon_pos
        
    elif active_player.history[-1] == tile_7.name:
        $ active_player.icon_last_pos = tile_7.icon_pos
        
    elif active_player.history[-1] == tile_8.name:
        $ active_player.icon_last_pos = tile_8.icon_pos
        
    
    #####################
  
    # if active_player.
    #     $ enemy_in_range = True

    #####################
    

    $ i = 0
    while i < (total_number_of_players):
        $ locked_tiles_temp.append(turn_order[i].history[-1])
        $ i += 1


    if in_combat == True:
        $ locked_tiles += map_exits 
 
    
    $ locked_tiles += locked_tiles_temp #TODO
       

    $ unlocked_tiles = [item for item in unlocked_tiles if item not in locked_tiles]

    if active_player.hostile == True:
        jump enemy_move
    else:
        jump call_map

    
label call_map:
    $ current_player_turn = active_player.name
    show screen current_player

    if active_player.hostile == True:
        jump moved
    else:
        call screen map_tiles(act = True)

screen map_tiles(act): 
    text "first H[turn_order[0].history]" 
    text "second H[turn_order[1].history]"ypos 100
    text "locked[locked_tiles]" ypos 200
    text "unlocked[unlocked_tiles]" ypos 300
    text "turn #[movement_turns]" ypos 400
   


    if number_of_tiles >= 1:
        # tile 1
        imagebutton:
            pos (tile_1.xpos, tile_1.ypos)
            if act == True:
                if tile_1.name in unlocked_tiles:
                    idle tile_1.idle
                    hover tile_1.hover
                    action [SetField(active_player, "icon_pos", tile_1.icon_pos), SetVariable("temp_tile_name", tile_1.name), Jump("moved")]
                else:
                    idle tile_1.locked
                    action NullAction()
            else:
                idle tile_1.locked
                action NullAction()

    if number_of_tiles >= 2:
        # tile 2
        imagebutton:
            pos (tile_2.xpos, tile_2.ypos)
            if act == True:
                if tile_2.name in unlocked_tiles:
                    idle tile_2.idle
                    hover tile_2.hover
                    action [SetField(active_player, "icon_pos", tile_2.icon_pos), SetVariable("temp_tile_name", tile_2.name), Jump("moved")]
                else:
                    idle tile_2.locked
                    action NullAction()
            else:
                idle tile_2.locked
                action NullAction()

    if number_of_tiles >= 3:
        # tile 3
        imagebutton:
            pos (tile_3.xpos, tile_3.ypos)
            if act == True:
                if tile_3.name in unlocked_tiles:
                    idle tile_3.idle
                    hover tile_3.hover
                    action [SetField(active_player, "icon_pos", tile_3.icon_pos), SetVariable("temp_tile_name", tile_3.name), Jump("moved")]
                else:
                    idle tile_3.locked
                    action NullAction()
            else:
                idle tile_3.locked
                action NullAction()
           
    if number_of_tiles >= 4:
        # tile 4
        imagebutton:
            pos (tile_4.xpos, tile_4.ypos)
            if act == True:
                if tile_4.name in unlocked_tiles:
                    idle tile_4.idle
                    hover tile_4.hover
                    action [SetField(active_player, "icon_pos", tile_4.icon_pos), SetVariable("temp_tile_name", tile_4.name), Jump("moved")]
                else:
                    idle tile_4.locked
                    action NullAction()
            else:
                idle tile_4.locked
                action NullAction()

    if number_of_tiles >= 5:
        # tile 5
        imagebutton:
            pos (tile_5.xpos, tile_5.ypos)
            if act == True:
                if tile_5.name in unlocked_tiles:
                    idle tile_5.idle
                    hover tile_5.hover
                    action [SetField(active_player, "icon_pos", tile_5.icon_pos), SetVariable("temp_tile_name", tile_5.name), Jump("moved")]
                else:
                    idle tile_5.locked
                    action NullAction()
            else:
                idle tile_5.locked
                action NullAction()
    
    if number_of_tiles >= 6:
        # tile 6
        imagebutton:
            pos (tile_6.xpos, tile_6.ypos)
            if act == True:
                if tile_6.name in unlocked_tiles:
                    idle tile_6.idle
                    hover tile_6.hover
                    action [SetField(active_player, "icon_pos", tile_6.icon_pos), SetVariable("temp_tile_name", tile_6.name), Jump("moved")]
                else:
                    idle tile_6.locked
                    action NullAction()
            else:
                idle tile_6.locked
                action NullAction()

    if number_of_tiles >= 7:
        # tile 7
        imagebutton:
            pos (tile_7.xpos, tile_7.ypos)
            if act == True:
                if tile_7.name in unlocked_tiles:
                    idle tile_7.idle
                    hover tile_7.hover
                    action [SetField(active_player, "icon_pos", tile_7.icon_pos), SetVariable("temp_tile_name", tile_7.name), Jump("moved")]
                else:
                    idle tile_7.locked
                    action NullAction()
            else:
                idle tile_7.locked
                action NullAction()

    if number_of_tiles >= 8:
        # tile 8
        imagebutton:
            pos (tile_8.xpos, tile_8.ypos)
            if act == True:
                if tile_8.name in unlocked_tiles:
                    idle tile_8.idle
                    hover tile_8.hover
                    action [SetField(active_player, "icon_pos", tile_8.icon_pos), SetVariable("temp_tile_name", tile_8.name), Jump("moved")] 
                else:
                    idle tile_8.locked
                    action NullAction()
            else:
                idle tile_8.locked
                action NullAction()


label moved:

    $ movement_turns += 1

    if active_player.hostile == False:
        $ active_player.history.extend([temp_tile_name, temp_tile_name])
        $ temp_tile_name = ""
    else:
        pause(0.5)

    jump map_display_1

label map_display_1:
    show screen map_tiles(act = False)

    jump display_icons

label turn:    
    
    if number_of_enemies >= 1: 
        $ in_combat = True

        if active_player.hostile == True: #enemy turn 
            jump enemy_turn

        else:
            jump player_turn
               
    else:
        call battle_end
        return

label player_turn:
    
    if (movement_turns < active_player.stanima) and (attack_turns < active_player.strength):# if both actions are avilable
        call screen move_or_attack
        $ renpy.pause(hard=True)

    elif (movement_turns < active_player.stanima) and (attack_turns >= active_player.strength): #if only movment is available
        jump pre_move
        
    elif(movement_turns >= active_player.stanima) and (attack_turns < active_player.strength): # if only attack avail
        if enemy_in_range == True:
            jump attack
        else:
            jump end_turn
    else:
        jump end_turn

label enemy_turn:
    
    if (movement_turns < active_player.stanima) and (attack_turns < active_player.strength): #both options
        $ y = random.randint(1, 2)
        
        if y == 2:
            jump pre_move

        else:
            if enemy_in_range == True:
                call attack
            else:
                jump enemy_turn

    elif (movement_turns >= active_player.stanima) and (attack_turns < active_player.strength): #attack only
        if enemy_in_range == True:
            jump attack
        else:
            jump end_turn

    elif (movement_turns < active_player.stanima) and (attack_turns >= active_player.strength): #move only
        jump pre_move
    else:    
        jump end_turn

label enemy_move:
    
    if unlocked_tiles != []: #enemy tries to move

        $ x = random.randint(0, (len(unlocked_tiles) - 1))
        
        $ z = unlocked_tiles[x]

        if z == tile_1.name:
            $ active_player.icon_pos = tile_1.icon_pos  
        elif z == tile_2.name:
            $ active_player.icon_pos = tile_2.icon_pos  
        elif z == tile_3.name:
            $ active_player.icon_pos = tile_3.icon_pos 
        elif z == tile_4.name:
            $ active_player.icon_pos = tile_4.icon_pos   
        elif z == tile_5.name:
            $ active_player.icon_pos = tile_5.icon_pos    
        elif z == tile_6.name:
            $ active_player.icon_pos = tile_6.icon_pos
        elif z == tile_7.name:
            $ active_player.icon_pos = tile_7.icon_pos
        elif z == tile_8.name:
            $ active_player.icon_pos = tile_8.icon_pos 

        $ active_player.history.append(z)
        
        jump call_map

    else:
        jump enemy_turn
  
label end_turn:
    
    $ turn_order_numb += 1
    
    if turn_order_numb >= total_number_of_players:
        $ turn_order_numb = 0

    $ active_player = turn_order[turn_order_numb]

    $ movement_turns = 0
    $ attack_turns = 0

    jump turn


