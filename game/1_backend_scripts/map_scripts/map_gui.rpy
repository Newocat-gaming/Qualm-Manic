label display_icons:
    
    show screen player_icons onlayer screens
    
    jump turn
     

    
    

screen player_icons:
    zorder 100
  
    add active_player.icon at player_tile_icon_pos()

    for x in [y for y in turn_order if y != active_player]:
        add x.icon pos x.icon_pos

transform player_tile_icon_pos():
    pos active_player.icon_last_pos

    block:
        linear 0.2 pos active_player.icon_pos
        repeat 



screen move_or_attack():
    hbox:
        align (0.0, 1.0)
        frame:
            background None
            xsize 350
            ysize 300
        vbox:
            xsize 350
            ysize 300
            textbutton "Move, [(active_player.stanima - movement_turns)] action(s) left":
                action [Hide("move_or_attack"), Jump("pre_move")]
            textbutton "Attack, [(active_player.strength - attack_turns)] action(s) left":
                action [Hide("move_or_attack"), Jump("attack")]
# Function(renpy.block_rollback),
# image map_background