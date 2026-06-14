# tile 1
default map_1_tile_1 = MapTile(name = "tile_1", lock = False, locked = "tile_lock", idle = "tile_unlock_idle", hover = "tile_1_hover", xpos = 500, ypos = 500, icon_pos = (500, 500), unlock_tiles = ["tile_2", "tile_4"], attack_tiles = ["tile_5"])
image tile_1_hover:
    "images/map/tile_unlock_idle.webp"
    0.3
    "images/map/tile_unlock_hover.webp"
    0.3
    repeat

# tile 2
default map_1_tile_2 = MapTile(name = "tile_2", lock = False, locked = "tile_lock", idle = "tile_unlock_idle", hover = "tile_2_hover", xpos = 700, ypos = 500, icon_pos = (700, 500), unlock_tiles = ["tile_1", "tile_3", "tile_5"], attack_tiles = ["tile_4", "tile_6"])
image tile_2_hover:
    "images/map/tile_unlock_idle.webp"
    0.3
    "images/map/tile_unlock_hover.webp"
    0.3
    repeat

# tile 3
default map_1_tile_3 = MapTile(name = "tile_3", lock = False, locked = "tile_lock", idle = "tile_unlock_idle", hover = "tile_3_hover", xpos = 900, ypos = 500, icon_pos = (900, 500), unlock_tiles = ["tile_2", "tile_6", "tile_8"], attack_tiles = ["tile_5", "tile_7"])
image tile_3_hover:
    "images/map/tile_unlock_idle.webp"
    0.3
    "images/map/tile_unlock_hover.webp"
    0.3
    repeat

# tile 4
default map_1_tile_4 = MapTile(name = "tile_4", lock = False, locked = "tile_lock", idle = "tile_unlock_idle", hover = "tile_4_hover", xpos = 500, ypos = 300, icon_pos = (500, 300), unlock_tiles = ["tile_1", "tile_5"], attack_tiles = ["tile_2"])
image tile_4_hover:
    "images/map/tile_unlock_idle.webp"
    0.3
    "images/map/tile_unlock_hover.webp"
    0.3
    repeat

# tile 5
default map_1_tile_5 = MapTile(name = "tile_5", lock = False, locked = "tile_lock", idle = "tile_unlock_idle", hover = "tile_5_hover", xpos = 700, ypos = 300, icon_pos = (700, 300), unlock_tiles = ["tile_2", "tile_4", "tile_6"], attack_tiles = ["tile_1", "tile_3"])
image tile_5_hover:
    "images/map/tile_unlock_idle.webp"
    0.3
    "images/map/tile_unlock_hover.webp"
    0.3
    repeat

# tile 6
default map_1_tile_6 = MapTile(name = "tile_6", lock = False, locked = "tile_lock", idle = "tile_unlock_idle", hover = "tile_6_hover", xpos = 900, ypos = 300, icon_pos = (900, 300), unlock_tiles = ["tile_5", "tile_3", "tile_7"], attack_tiles = ["tile_2", "tile_8"])
image tile_6_hover:
    "images/map/tile_unlock_idle.webp"
    0.3
    "images/map/tile_unlock_hover.webp"
    0.3
    repeat

# tile 7
default map_1_tile_7 = MapTile(name = "tile_7", lock = False, locked = "tile_lock", idle = "tile_unlock_idle", hover = "tile_7_hover", xpos = 1100, ypos = 300, icon_pos = (1100, 300), unlock_tiles = ["tile_6", "tile_8"], attack_tiles = ["tile_3"])
image tile_7_hover:
    "images/map/tile_unlock_idle.webp"
    0.3
    "images/map/tile_unlock_hover.webp"
    0.3
    repeat

# tile 8
default map_1_tile_8 = MapTile(name = "tile_8", lock = False, locked = "tile_lock", idle = "tile_unlock_idle", hover = "tile_8_hover", xpos = 1100, ypos = 500, icon_pos = (1100, 500), unlock_tiles = ["tile_3", "tile_7"], attack_tiles = ["tile_6"])
image tile_8_hover:
    "images/map/tile_unlock_idle.webp"
    0.3
    "images/map/tile_unlock_hover.webp"
    0.3
    repeat









#########################################

label tile_1_pressed:
    if map_number == 1:
        jump call_map
   
label tile_2_pressed:
    jump call_map

label tile_3_pressed:
    jump call_map

label tile_4_pressed:
    jump call_map

label tile_5_pressed:
    jump call_map
   
label tile_6_pressed:
    jump call_map

label tile_7_pressed:
    jump call_map
    
label tile_8_pressed:
    jump call_map