
label test:

    $ manic_pose = "armscrossed"
    show manic_model at middle

    manic "test"
    jay "holy hell" 
    manic "I know right"

    hide manic_model


    #############################

    $ minigame_difficulty = 3

    $ bar_choice_num = 3
   
    $ choice_1 = "walk_out_of_the_room"
    $ choice_text_1 = "Hear what Kit has to say."

    $ choice_2 = "walk_out_of_the_room"
    $ choice_text_2 = "Hear what Kit has to say."

    $ choice_3 = "wait_for_vida"
    $ choice_text_3 = "Hear what Kit has to say."

    $ choice_4 = None
    $ choice_text_4 = "test4"


    jump minigame_start


#########################################################################
define test_text = 0




define choice_1 = ""
define choice_2 = ""
define choice_3 = ""
define choice_4 = ""

define choice_text_1 = ""
define choice_text_2 = ""
define choice_text_3 = ""
define choice_text_4 = ""

define minigame_difficulty = 1

define bar_choice_num = 0

define minigame_point_pos = 360
define minigame_point_end_pos = 0

define minigame_grace_period = True
define minigame_speed = 3      # can only be whole numbers?

define minigame_speed_text = minigame_speed - 2
define minigame_outcome = "test"
define random_text = "test"

    
transform minigame_point_move(frp):
    xpos frp
    subpixel True
    anchor(0.5, 1.0)
    ypos 500 
              
transform minigame_result_text:
    xalign 0.75
    ypos 750

image minigame_pointer:
    "minigame/point.png"
image minigame_pointer_selection:
    "minigame/point2.png" 

init python:
    import random # DO NOT REMOVE


label minigame_start:
    $ random_text = random.randint(1, 7) 

    $ minigame_point_pos = random.randint(360, 1560)

    $ minigame_grace_period = True

    show screen timer_right
    show screen minigame_choice_bar
    show screen minigame_pointer
    call screen minigame_control


label minigame_end:
    $ minigame_point_end_pos = minigame_point_pos
    hide screen timer_left
    hide screen timer_right
    hide screen minigame_control
    show minigame_pointer_selection onlayer overlay at minigame_point_move(minigame_point_pos) 
    $ renpy.pause(1.0)
    hide screen minigame_pointer
    hide screen minigame_choice_bar 

    if minigame_outcome == choice_1:
        jump expression choice_1
    elif minigame_outcome == choice_2:
        jump expression choice_2
    elif minigame_outcome == choice_3:
        jump expression choice_3
    elif minigame_outcome == choice_4:
        jump expression choice_4
    else:
        show screen minigame_error


screen minigame_control:
    
    text "test: length [bar_choice_num]" align(0.5, 0.1)
    text "test: speed [minigame_speed_text]" align(0.5, 0.2)
    text "test: timer [test_text]" align(0.5, 0.3)
    timer 1.0 repeat True action IncrementVariable("test_text")


    if minigame_difficulty == 1:
        timer 7.0 action [SetVariable("minigame_grace_period", False), IncrementVariable("minigame_speed"), IncrementVariable("minigame_speed_text")]
        if minigame_grace_period == False:
            timer 4.0 repeat True action [IncrementVariable("minigame_speed"), IncrementVariable("minigame_speed_text")]
    if minigame_difficulty == 2:
        timer 6.0 action [SetVariable("minigame_grace_period", False), IncrementVariable("minigame_speed"), IncrementVariable("minigame_speed_text")]
        if minigame_grace_period == False:
            timer 3.0 repeat True action [IncrementVariable("minigame_speed"), IncrementVariable("minigame_speed_text")]
    if minigame_difficulty == 3:
        timer 5.0 action [SetVariable("minigame_grace_period", False), IncrementVariable("minigame_speed"), IncrementVariable("minigame_speed_text")]
        if minigame_grace_period == False:
            timer 2.0 repeat True action [IncrementVariable("minigame_speed"), IncrementVariable("minigame_speed_text")]


    if bar_choice_num == 1:
        if minigame_point_pos >= 360 and minigame_point_pos <= 1560:
            key "K_SPACE":
                action [SetVariable("minigame_outcome", choice_1), Show("minigame_result"), Jump("minigame_end")]
        else:
            key "K_SPACE":
                action Show("minigame_error")

    elif bar_choice_num == 2:
        if minigame_point_pos >= 360 and minigame_point_pos < 920:
            key "K_SPACE":
                action [SetVariable("minigame_outcome", choice_1), Show("minigame_result"), Jump("minigame_end")]
        elif minigame_point_pos > 920 and minigame_point_pos <= 1560:
            key "K_SPACE":
                action [SetVariable("minigame_outcome", choice_2), Show("minigame_result"), Jump("minigame_end")]
        else:
            key "K_SPACE":
                action Show("minigame_error")
        
    elif bar_choice_num == 3:
        if minigame_point_pos >= 360 and minigame_point_pos < 760:
            key "K_SPACE":
                action [SetVariable("minigame_outcome", choice_1), Show("minigame_result"), Jump("minigame_end")]
        elif minigame_point_pos > 760 and minigame_point_pos < 1160:
            key "K_SPACE":
                action [SetVariable("minigame_outcome", choice_2), Show("minigame_result"), Jump("minigame_end")]
        elif minigame_point_pos > 1160 and minigame_point_pos <= 1560:
            key "K_SPACE":
                action [SetVariable("minigame_outcome", choice_3), Show("minigame_result"), Jump("minigame_end")]
        else:
            key "K_SPACE":
                action Show("minigame_error")

    elif bar_choice_num == 4:
        if minigame_point_pos >= 360 and minigame_point_pos < 660:
            key "K_SPACE":
                action [SetVariable("minigame_outcome", choice_1), Show("minigame_result"), Jump("minigame_end")]
        elif minigame_point_pos > 660 and minigame_point_pos < 960:
            key "K_SPACE":
                action [SetVariable("minigame_outcome", choice_2), Show("minigame_result"), Jump("minigame_end")]
        elif minigame_point_pos > 960 and minigame_point_pos < 1260:
            key "K_SPACE":
                action [SetVariable("minigame_outcome", choice_3), Show("minigame_result"), Jump("minigame_end")]
        elif minigame_point_pos > 1260 and minigame_point_pos <= 1560:
            key "K_SPACE":
                action [SetVariable("minigame_outcome", choice_4), Show("minigame_result"), Jump("minigame_end")]
        else:
            key "K_SPACE":
                action Show("minigame_error")
   
screen timer_left:
    timer 0.0001 repeat True action [If(minigame_point_pos >= 360, SetVariable("minigame_point_pos", minigame_point_pos - minigame_speed)),If(minigame_point_pos <= 360, Hide("timer_left"), Show("timer_right"))]
screen timer_right:
    timer 0.0001 repeat True action [If(minigame_point_pos <= 1560, SetVariable("minigame_point_pos", minigame_point_pos + minigame_speed)),If(minigame_point_pos >= 1560, Hide("timer_right"), Show("timer_left"))]

screen minigame_pointer:
    add "minigame_pointer" at minigame_point_move(minigame_point_pos)

screen minigame_choice_bar:
    if bar_choice_num == 0:
        text "error"
    else:
        hbox:
            xysize(1200, 100)
            yalign 0.5
            xalign 0.5

            if bar_choice_num >= 1:
                frame: 
                    ysize 100
                    xfill True
                    

                    if bar_choice_num == 1:
                        xmaximum 1200
                    elif bar_choice_num == 2:
                        xmaximum 600
                    elif bar_choice_num == 3:
                        xmaximum 400
                    else:
                        xmaximum 300   
                    
                    size_group "minigame_option"
                    text choice_text_1:
                        align(0.5, 0.5)
                    background "#ff3535"
            if bar_choice_num >= 2:
                frame:
                    ysize 100
                    xfill True

                    if bar_choice_num == 2:
                        xmaximum 600
                    elif bar_choice_num == 3:
                        xmaximum 400
                    else:
                        xmaximum 300

                    size_group "minigame_option"
                    text choice_text_2:
                        align(0.5, 0.5)  
                    background "#35ff46" 
            if bar_choice_num >= 3:
                frame:
                    ysize 100 
                    xfill True

                    if bar_choice_num == 3:
                        xmaximum 400
                    else:
                        xmaximum 300

                    size_group "minigame_option"
                    text choice_text_3:
                        align(0.5, 0.5)  
                    background "#7235ff" 
            if bar_choice_num >= 4:
                frame:
                    ysize 100 
                    xfill True

                    xmaximum 300

                    size_group "minigame_option"
                    text choice_text_4:
                        align(0.5, 0.5)  
                    background "#358dff" 

screen minigame_error:
    text "{color=#e66a6a}ERROR!{/color}" at minigame_result_text
    timer 0.5 action Hide("minigame_error")

screen minigame_result:
    if random_text == 1:
        text "{color=#e66a6a}You did this to yourself...{/color}" at minigame_result_text
    elif random_text == 2:
        text "{color=#e66a6a}Good choice?{/color}" at minigame_result_text
    elif random_text == 3:
        text "{color=#e66a6a}{/color}" at minigame_result_text
    elif random_text == 4:
        text "{color=#e66a6a}{/color}" at minigame_result_text
    elif random_text == 5:
        text "{color=#e66a6a}{/color}" at minigame_result_text
    elif random_text == 6:
        text "{color=#e66a6a}{/color}" at minigame_result_text
    else:
        text "{color=#e66a6a}{/color}" at minigame_result_text
      
    timer 1.0 action Hide("minigame_result")


        
















        
