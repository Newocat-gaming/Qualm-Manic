label call_mapUI:
    call screen MapUI

screen MapUI:
    add "map_background"
    text "[player_pos]" pos(400, 400) # test
    
    # block 1
    imagebutton:
        at block_1_location
        if block_1_lock == True:
            idle "map/block_lock.png"
            action NullAction()
        elif player_pos == block_1:
            idle "map/block_lock.png"
            action NullAction()
        else:
            idle "map/block_unlock_idle.png"
            hover "map/block_unlock_hover.png"
            action [SetVariable("player_pos", block_1), Jump("block_1_pressed")]

    # block 2  
    imagebutton:
        at block_2_location
        if block_2_lock == True:
            idle "map/block_lock.png"
            action NullAction()
        elif player_pos == block_2:
            idle "map/block_lock.png"
            action NullAction()
        else:
            idle "map/block_unlock_idle.png"
            hover "map/block_unlock_hover.png"
            action [SetVariable("player_pos", block_2), Jump("block_2_pressed")]
    
    # block 3
    imagebutton:
        at block_3_location
        if block_3_lock == True:
            idle "map/block_lock.png"
            action NullAction()
        elif player_pos == block_3:
            idle "map/block_lock.png"
            action NullAction()
        else:
            idle "map/block_unlock_idle.png"
            hover "map/block_unlock_hover.png"
            action [SetVariable("player_pos", block_3), Jump("block_3_pressed")]

    if player_pos == block_1:
        add "player_ind" at block_1_location
    elif player_pos == block_2:
        add "player_ind" at block_2_location
    elif player_pos == block_3:
        add "player_ind" at block_3_location
    
define player_pos = "block_1"

default block_1 = "block_1"
define block_1_lock = False
transform block_1_location:
    pos (600, 600)

define block_2 = "block_2"
define block_2_lock = False
transform block_2_location:
    pos (500, 600)

define block_3 = "block_3"
define block_3_lock = False
transform block_3_location:
    pos (400, 600)

image map_background:
    "images/Map/background.png"

image player_ind:
    "images/Map/player_dot.png"


#########################################
label test:
    jump call_mapUI

label test_2:
    call screen MapUI

label block_1_pressed:
    jump test_2
   
label block_2_pressed:
    jump test_2

label block_3_pressed:
    jump test_2
    
    
