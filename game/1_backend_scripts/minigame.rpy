
label test:

    $ manic_pose = "armscrossed"
    show manic_model at middle

    manic "test"
    jay "holy hell" 
    manic "I know right"


    #############################
    $ difficulty = 1


    $ bar_choice_num = 3
   
    $ choice_1 = "walk_out_of_the_room"
    $ choice_text_1 = "walk"

    $ choice_2 = "walk_out_of_the_room"
    $ choice_text_2 = "walk"

    $ choice_3 = "wait_for_vida"
    $ choice_text_3 = "wait"

    $ choice_4 = None
    $ choice_text_4 = "test4"


    jump minigame_start


#########################################################################

define choice_1 = ""
define choice_2 = ""
define choice_3 = ""
define choice_4 = ""

define choice_text_1 = ""
define choice_text_2 = ""
define choice_text_3 = ""
define choice_text_4 = ""


define bar_choice_num = 0

define minigame_point_pos = 360
define minigame_point_end_pos = 0

define minigame_speed = 3      # can only be whole numbers?

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

image minigame_pointer_selection:
    "minigame/point2.png" with Dissolve(1.5) # do not change number


label minigame_start:
    $ random_text = renpy.random.randint(1, 7)

    $ minigame_point_pos = renpy.random.randint(360, 1560)



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
    $ renpy.pause(1.0)                  # do not change number
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
    
    text "test: [bar_choice_num]" align(0.5,0.1)
    text "test: [minigame_speed]" align(0.5, 0.2)


    
    
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
    timer 0.0001 repeat True action [If(minigame_point_pos >= 360, SetVariable("minigame_point_pos", minigame_point_pos - minigame_speed)),If(minigame_point_pos == 360, Hide("timer_left"), Show("timer_right"))]
screen timer_right:
    timer 0.0001 repeat True action [If(minigame_point_pos <= 1560, SetVariable("minigame_point_pos", minigame_point_pos + minigame_speed)),If(minigame_point_pos == 1560, Hide("timer_right"), Show("timer_left"))]

screen minigame_pointer:
    add "minigame/point.png" at minigame_point_move(minigame_point_pos)

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


        
















        
