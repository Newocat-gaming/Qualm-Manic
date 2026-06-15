python early:
    import renpy.store as store
    class Player(store.object):
        def __init__(self, name = "", image = "", hp = 0, stanima = 0, strength = 0, mana = 0, hostile = False, icon_pos = (), icon_last_pos = (), icon = "", icon_show = True, history = []):
            self.name = name
            self.image = "profiles/" + image + ".webp"
            self.hp = hp
            self.stanima = stanima
            self.strength = strength
            self.mana = mana
            self.hostile = hostile
            self.icon_pos = icon_pos
            self.icon_last_pos = icon_last_pos
            self.icon = "map/" + icon + ".webp"
            self.icon_show = icon_show
            self.history = history


# main character, does not change in game
default player_1 = Player(name = "Jay", image = "", hp = 100, stanima = 2, strength = 1, mana = 10,  hostile = False, icon_pos = (), icon_last_pos = (), icon = "player_dot", icon_show = True, history = [])


# blank party members, chnages in game
default player_2 = Player(name = "", image = "", hp = 100, stanima = 1, strength = 1, mana = 10,  hostile = False, icon_pos = (), icon_last_pos = (), icon = "player_dot", icon_show = True, history = [])
default player_3 = Player(name = "", image = "", hp = 100, stanima = 2, strength = 1, mana = 10,  hostile = False, icon_pos = (), icon_last_pos = (), icon = "player_dot", icon_show = True, history = [])
default player_4 = Player(name = "", image = "", hp = 100, stanima = 2, strength = 1, mana = 10,  hostile = False, icon_pos = (), icon_last_pos = (), icon = "player_dot", icon_show = True, history = [])
default player_5 = Player(name = "", image = "", hp = 100, stanima = 2, strength = 1, mana = 10,  hostile = False, icon_pos = (), icon_last_pos = (), icon = "player_dot", icon_show = True, history = [])


# all potential party members
default player_kit = Player(name = "Kit", image = "", hp = 100, stanima = 2, strength = 1, mana = 10,  hostile = False, icon_pos = (), icon_last_pos = (), icon = "player_dot", icon_show = True, history = [])
default player_vida = Player(name = "Vida", image = "", hp = 100, stanima = 2, strength = 1, mana = 10,  hostile = False, icon_pos = (), icon_last_pos = (), icon = "player_dot", icon_show = True, history = [])
default player_andrea = Player(name = "Andrea", image = "", hp = 100, stanima = 2, strength = 1, mana = 10,  hostile = False, icon_pos = (), icon_last_pos =(), icon = "player_dot", icon_show = True, history = [])


###########################
default active_player = player_1
###########################


default party_list = [player_1, player_2, player_3, player_4, player_5]
default party_list_names = [player_1.name, player_2.name, player_3.name, player_4.name, player_5.name]

default party_list_temp = []

default empty_players = []

default player_slot_1 = party_list[0]
default player_slot_2 = party_list[1]
default player_slot_3 = party_list[2]
default player_slot_4 = party_list[3]
default player_slot_5 = party_list[4] 

default turn_order = []
default turn_order_names = ["", "", "", "", "", "", "", "", "", "",]


label turn_order_start():
    $ number_of_empty_players = party_list_names.count("")
    $ number_of_enemies = len(enemies_list)
    $ number_of_players = (5 - number_of_empty_players)
    $ total_number_of_players = (number_of_players + number_of_enemies)
    $ empty_players = [x for x in party_list if x.name == ""]
    
    if number_of_enemies >= 1: # combat so all players are seprate
        call battle_start

        $ party_list_temp = [item for item in party_list if item not in empty_players]
        $ turn_order = (party_list_temp + enemies_list)  
        $ turn_order.sort(key=lambda player: player.stanima) #TODO

        $ i = 0
        while i < len(turn_order):
            $ turn_order_names[i] = turn_order[i].name
            $ turn_order[i].icon_show = True
            $ i += 1
        
        $ turn_order_names = [item for item in turn_order_names if item != ""]

        $ active_player = turn_order[0]

        $ turn_order_numb = 0
        $ movement_turns = 0
        $ attack_turns = 0


        #############################
        $ i = 0
        while i < number_of_players:
            $ temp = turn_order[i].icon
            $ i += 1

    else: # no combat, so only need 1 player moving
        call battle_end
        $ player_1.icon_show = True
        $ player_2.icon_show = False
        $ player_3.icon_show = False
        $ player_4.icon_show = False
        $ player_5.icon_show = False
        $ active_player = player_1



    jump map_display_1

    default temp = ""