


label call_map_1:

    if active_player.history[-1] == tile_1.name:
        $ unlocked_tiles = tile_1.unlock_tiles
    elif active_player.history[-1] == tile_2.name:
        $ unlocked_tiles = tile_2.unlock_tiles
    elif active_player.history[-1] == tile_3.name:
        $ unlocked_tiles = tile_3.unlock_tiles
    elif active_player.history[-1] == tile_4.name:
        $ unlocked_tiles = tile_4.unlock_tiles
    elif active_player.history[-1] == tile_5.name:
        $ unlocked_tiles = tile_5.unlock_tiles
    elif active_player.history[-1] == tile_6.name:
        $ unlocked_tiles = tile_6.unlock_tiles
    elif active_player.history[-1] == tile_7.name:
        $ unlocked_tiles = tile_7.unlock_tiles
    elif active_player.history[-1] == tile_8.name:
        $ unlocked_tiles = tile_8.unlock_tiles
    
    #############

    if active_player.history[-2] == tile_1.name:
        $ active_player.icon_last_pos = tile_1.icon_pos
    elif active_player.history[-2] == tile_2.name:
        $ active_player.icon_last_pos = tile_2.icon_pos
    elif active_player.history[-2] == tile_3.name:
        $ active_player.icon_last_pos = tile_3.icon_pos
    elif active_player.history[-2] == tile_4.name:
        $ active_player.icon_last_pos = tile_4.icon_pos
    elif active_player.history[-2] == tile_5.name:
        $ active_player.icon_last_pos = tile_5.icon_pos
    elif active_player.history[-2] == tile_6.name:
        $ active_player.icon_last_pos = tile_6.icon_pos
    elif active_player.history[-2] == tile_7.name:
        $ active_player.icon_last_pos = tile_7.icon_pos
    elif active_player.history[-2] == tile_8.name:
        $ active_player.icon_last_pos = tile_8.icon_pos
    
    #####################


    if in_combat == True:
        $ locked_tiles = map_1_exits

    $ unlocked_tiles = [x for x in unlocked_tiles if x != player_1.history[-1] ] #or player_2.history[-1]

    show screen testing
    call screen map_1

screen testing:
    text "[unlocked_tiles]"
    text "[active_player.history]" ypos 100

screen map_1:
    add "map_background"
    
    # tile 1
    imagebutton:
        pos (tile_1.xpos, tile_1.ypos)
        if tile_1.name in unlocked_tiles:
            idle tile_1.idle
            hover tile_1.hover
            action [SetField(active_player, "icon_pos", tile_1.icon_pos), Function(active_player.history.append, tile_1.name), Jump("tile_1_pressed")]
        else:
            idle tile_1.locked
            action NullAction()
    
    # tile 2
    imagebutton:
        pos (tile_2.xpos, tile_2.ypos)
        if tile_2.name in unlocked_tiles:
            idle tile_2.idle
            hover tile_2.hover
            action [SetField(active_player, "icon_pos", tile_2.icon_pos), Function(active_player.history.append, tile_2.name), Jump("tile_2_pressed")]
        else:
            idle tile_2.locked
            action NullAction()

    # tile 3
    imagebutton:
        pos (tile_3.xpos, tile_3.ypos)
        if tile_3.name in unlocked_tiles:
            idle tile_3.idle
            hover tile_3.hover
            action [SetField(active_player, "icon_pos", tile_3.icon_pos), Function(active_player.history.append, tile_3.name), Jump("tile_3_pressed")]
        else:
            idle tile_3.locked
            action NullAction()

    # tile 4
    imagebutton:
        pos (tile_4.xpos, tile_4.ypos)
        if tile_4.name in unlocked_tiles:
            idle tile_4.idle
            hover tile_4.hover
            action [SetField(active_player, "icon_pos", tile_4.icon_pos), Function(active_player.history.append, tile_4.name), Jump("tile_4_pressed")]
        else:
            idle tile_3.locked
            action NullAction()

    # tile 5
    imagebutton:
        pos (tile_5.xpos, tile_5.ypos)
        if tile_5.name in unlocked_tiles:
            idle tile_5.idle
            hover tile_5.hover
            action [SetField(active_player, "icon_pos", tile_5.icon_pos), Function(active_player.history.append, tile_5.name), Jump("tile_5_pressed")]
        else:
            idle tile_5.locked
            action NullAction()
    
    # tile 6
    imagebutton:
        pos (tile_6.xpos, tile_6.ypos)
        if tile_6.name in unlocked_tiles:
            idle tile_6.idle
            hover tile_6.hover
            action [SetField(active_player, "icon_pos", tile_6.icon_pos), Function(active_player.history.append, tile_6.name), Jump("tile_6_pressed")]
        else:
            idle tile_6.locked
            action NullAction()

    # tile 7
    imagebutton:
        pos (tile_7.xpos, tile_7.ypos)
        if tile_7.name in unlocked_tiles:
            idle tile_7.idle
            hover tile_7.hover
            action [SetField(active_player, "icon_pos", tile_7.icon_pos), Function(active_player.history.append, tile_7.name), Jump("tile_7_pressed")]
        else:
            idle tile_7.locked
            action NullAction()

    # tile 8
    imagebutton:
        pos (tile_8.xpos, tile_8.ypos)
        if tile_8.name in unlocked_tiles:
            idle tile_8.idle
            hover tile_8.hover
            action [SetField(active_player, "icon_pos", tile_8.icon_pos), Function(active_player.history.append, tile_8.name), Jump("tile_8_pressed")] 
        else:
            idle tile_8.locked
            action NullAction()

    add player_1.icon at tile_icon_pos


# tile 1
default tile_1 = MapTile(name = "tile_1", lock = False, locked = "tile_lock", idle = "tile_unlock_idle", hover = "tile_1_hover", xpos = 500, ypos = 500, icon_pos = (500, 500), unlock_tiles = ["tile_2", "tile_4"])
image tile_1_hover:
    "images/map/tile_unlock_idle.webp"
    0.3
    "images/map/tile_unlock_hover.webp"
    0.3
    repeat

# tile 2
default tile_2 = MapTile(name = "tile_2", lock = False, locked = "tile_lock", idle = "tile_unlock_idle", hover = "tile_2_hover", xpos = 700, ypos = 500, icon_pos = (700, 500), unlock_tiles = ["tile_1", "tile_3", "tile_5"])
image tile_2_hover:
    "images/map/tile_unlock_idle.webp"
    0.3
    "images/map/tile_unlock_hover.webp"
    0.3
    repeat

# tile 3
default tile_3 = MapTile(name = "tile_3", lock = False, locked = "tile_lock", idle = "tile_unlock_idle", hover = "tile_3_hover", xpos = 900, ypos = 500, icon_pos = (900, 500), unlock_tiles = ["tile_2", "tile_6", "tile_8"])
image tile_3_hover:
    "images/map/tile_unlock_idle.webp"
    0.3
    "images/map/tile_unlock_hover.webp"
    0.3
    repeat

# tile 4
default tile_4 = MapTile(name = "tile_4", lock = False, locked = "tile_lock", idle = "tile_unlock_idle", hover = "tile_4_hover", xpos = 500, ypos = 300, icon_pos = (500, 300), unlock_tiles = ["tile_1", "tile_5"])
image tile_4_hover:
    "images/map/tile_unlock_idle.webp"
    0.3
    "images/map/tile_unlock_hover.webp"
    0.3
    repeat

# tile 5
default tile_5 = MapTile(name = "tile_5", lock = False, locked = "tile_lock", idle = "tile_unlock_idle", hover = "tile_5_hover", xpos = 700, ypos = 300, icon_pos = (700, 300), unlock_tiles = ["tile_2", "tile_4", "tile_6"])
image tile_5_hover:
    "images/map/tile_unlock_idle.webp"
    0.3
    "images/map/tile_unlock_hover.webp"
    0.3
    repeat

# tile 6
default tile_6 = MapTile(name = "tile_6", lock = False, locked = "tile_lock", idle = "tile_unlock_idle", hover = "tile_6_hover", xpos = 900, ypos = 300, icon_pos = (900, 300), unlock_tiles = ["tile_5", "tile_3", "tile_7"])
image tile_6_hover:
    "images/map/tile_unlock_idle.webp"
    0.3
    "images/map/tile_unlock_hover.webp"
    0.3
    repeat

# tile 7
default tile_7 = MapTile(name = "tile_7", lock = False, locked = "tile_lock", idle = "tile_unlock_idle", hover = "tile_7_hover", xpos = 1100, ypos = 300, icon_pos = (1100, 300), unlock_tiles = ["tile_6", "tile_8"])
image tile_7_hover:
    "images/map/tile_unlock_idle.webp"
    0.3
    "images/map/tile_unlock_hover.webp"
    0.3
    repeat

# tile 8
default tile_8 = MapTile(name = "tile_8", lock = False, locked = "tile_lock", idle = "tile_unlock_idle", hover = "tile_8_hover", xpos = 1100, ypos = 500, icon_pos = (1100, 500), unlock_tiles = ["tile_3", "tile_7"])
image tile_8_hover:
    "images/map/tile_unlock_idle.webp"
    0.3
    "images/map/tile_unlock_hover.webp"
    0.3
    repeat

transform tile_icon_pos:
    pos active_player.icon_last_pos
    linear 0.2 pos active_player.icon_pos



default map_1_exits = [tile_8.name]


#########################################
label test:
    jump turn_zero

label tile_1_pressed:
    jump call_map_1
   
label tile_2_pressed:
    jump call_map_1

label tile_3_pressed:
    jump call_map_1

label tile_4_pressed:
    jump call_map_1

label tile_5_pressed:
    jump call_map_1
   
label tile_6_pressed:
    jump call_map_1

label tile_7_pressed:
    jump call_map_1
    
label tile_8_pressed:
    jump call_map_1