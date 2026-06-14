label test:
    jump turn_zero

label turn_zero:
    if map_number == 1:
        $ number_of_tiles = 8

        $ tile_1 = map_1_tile_1
        $ tile_2 = map_1_tile_2
        $ tile_3 = map_1_tile_3
        $ tile_4 = map_1_tile_4
        $ tile_5 = map_1_tile_5
        $ tile_6 = map_1_tile_6
        $ tile_7 = map_1_tile_7
        $ tile_8 = map_1_tile_8

        ######################################
        $ map_1_exits = [tile_8]
        ######################################

        $ player_1.icon_pos = tile_1.icon_pos
        $ player_2.icon_pos = tile_1.icon_pos
        $ player_3.icon_pos = tile_1.icon_pos
        $ player_4.icon_pos = tile_1.icon_pos
        $ player_5.icon_pos = tile_1.icon_pos

        ###
        $ player_1.icon_last_pos = tile_1.icon_pos
        $ player_2.icon_last_pos = tile_1.icon_pos
        $ player_3.icon_last_pos = tile_1.icon_pos
        $ player_4.icon_last_pos = tile_1.icon_pos
        $ player_5.icon_last_pos = tile_1.icon_pos

        ###
        $ player_1.history.extend([tile_1.name, tile_1.name])
        $ player_2.history.extend([tile_1.name, tile_1.name])
        $ player_3.history.extend([tile_1.name, tile_1.name])
        $ player_4.history.extend([tile_1.name, tile_1.name])
        $ player_5.history.extend([tile_1.name, tile_1.name])

    elif map_number == 2:
        $ number_of_tiles = 10

        $ player_1.icon_pos = tile_1.icon_pos
        $ player_2.icon_pos = tile_1.icon_pos
        #$ player_3.icon_pos = tile_1.icon_pos
        #$ player_4.icon_pos = tile_1.icon_pos
        #$ player_5.icon_pos = tile_1.icon_pos

    jump enemies_start
   