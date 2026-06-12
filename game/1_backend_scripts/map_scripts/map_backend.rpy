python early:
    class MapTile:
        def __init__(self, name = "", lock = False, locked = "", idle = "", hover = "", xpos = 0, ypos = 0, icon_pos = (), icon_t = "tile_icon_pos", unlock_tiles = []):
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

default unlocked_tiles = []
default locked_tiles = []

define number_of_tiles = 8

default in_combat = False

default map_number = 1

label turn_zero:
    if map_number == 1:
        $ number_of_tiles = 8

        $ player_1.icon_pos = tile_1.icon_pos
        $ player_2.icon_pos = tile_1.icon_pos
        # $ player_3.icon_pos = tile_1_icon_pos
        # $ player_4.icon_pos = tile_1_icon_pos
        # $ player_5.icon_pos = tile_1_icon_pos

        $ player_1.history.append(tile_1.name)
        $ player_1.history.append(tile_1.name)
    #elif map_number == 2:
        

    jump call_map_1


image map_background:
    "images/Map/background.png"    
