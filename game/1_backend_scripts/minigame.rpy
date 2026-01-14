init 15 python:
    minigame_bar = 90
    minigame_score = 0
    you_press_button = 0

init:
    transform point_move(frp):
        subpixel True
        rotate_pad True
        align(0.5,1.22)
        rotate frp

screen minigameold:
    add "minigame/bar.png" align(0.5,0.5)
    add "minigame/point.png" at point_move(minigame_bar)
    text "[minigame_score]SCORE" align(0.5,0.1)
    text "[minigame_bar]bar" align(0.5,0.2)
    text "[you_press_button]button = pressed" align(0.5,0.3)

    if minigame_bar >= -14 and minigame_bar <= 14:
        key "K_SPACE":
            if you_press_button == 0:
                if minigame_score < 14:
                    action [SetVariable("minigame_score", minigame_score + 1), SetVariable("you_press_button", you_press_button + 1), Show("you_press_button_good")]
                else:
                    action Jump("end")
            elif you_press_button == 1:
                action SetVariable("minigame_score", minigame_score + 0)
        key "mousedown_1":
            if you_press_button == 0:
                if minigame_score < 14:
                    action [SetVariable("minigame_score", minigame_score + 1), SetVariable("you_press_button", you_press_button + 1), Show("you_press_button_good")]
                else:
                    action Jump("end")
            elif you_press_button == 1:
                action SetVariable("minigame_score", minigame_score + 0)
    else:
        key "K_SPACE" action [SetVariable("minigame_score", 0), Show("you_press_button_bad")]
        key "mousedown_1" action [SetVariable("minigame_score", 0), Show("you_press_button_bad")]




screen timer_left:
    timer 0.0001 repeat True action [If(minigame_bar >= -90, SetVariable("minigame_bar", minigame_bar - 1)),If(minigame_bar == -90, Hide("timer_left"), Show("timer_right")), If(minigame_bar == -90, SetVariable("you_press_button", 0))]
screen timer_right:
    timer 0.0001 repeat True action [If(minigame_bar <= 90, SetVariable("minigame_bar", minigame_bar + 1)),If(minigame_bar == 90, Hide("timer_right"), Show("timer_left")), If(minigame_bar == 90, SetVariable("you_press_button", 0))]
 
screen you_press_button_good:
    text "{color=#1e8e00}Good Work!{/color}" at move_good
    timer 1.0 action Hide("you_press_button_good")

screen you_press_button_bad:
    #hbox at move_bad:
    text "{color=#950000}Ups...\nTry Again.{/color}" at move_bad
    timer 1.0 action Hide("you_press_button_bad")

transform move_good:
    align(0.5,0.5)
    linear 0.05 zoom 1.3
    linear 0.5 zoom 1.0 alpha 0.0

transform move_bad:
    align(0.5,0.5)
    linear 0.04 xalign 0.5
    linear 0.06 xalign 0.495
    linear 0.06 xalign 0.515
    linear 0.06 xalign 0.5
    linear 0.5 alpha 0.0
################################################################################
label start_minigame:
    show screen timer_left
    call screen minigame
################################################################################
label end_minigame: #End minigame. And jump continue game
    hide screen minigame
    hide screen timer_left
    hide screen timer_right
    $ renpy.pause(0.3)
    return #continue game

############### my stuff ############################

screen minigame2(options = 2, ):
    add "minigame/bar.png" align(0.5,0.5)
    add "minigame/point.png" at point_move(minigame_bar)
    text "[minigame_score]SCORE" align(0.5,0.1)
    text "[minigame_bar]bar" align(0.5,0.2)
    text "[you_press_button]button = pressed" align(0.5,0.3)
 
    if minigame_bar >= -14 and minigame_bar <= 14:
        key "K_SPACE":
            if you_press_button == 0:
                if minigame_score < 14:
                    action [SetVariable("minigame_score", minigame_score + 1), SetVariable("you_press_button", you_press_button + 1), Show("you_press_button_good")]
                else:
                    action Jump("end")
            elif you_press_button == 1:
                action SetVariable("minigame_score", minigame_score + 0)
        key "mousedown_1":
            if you_press_button == 0:
                if minigame_score < 14:
                    action [SetVariable("minigame_score", minigame_score + 1), SetVariable("you_press_button", you_press_button + 1), Show("you_press_button_good")]
                else:
                    action Jump("end")
            elif you_press_button == 1:
                action SetVariable("minigame_score", minigame_score + 0)
    else:
        key "K_SPACE" action [SetVariable("minigame_score", 0), Show("you_press_button_bad")]
        key "mousedown_1" action [SetVariable("minigame_score", 0), Show("you_press_button_bad")]

screen minigame:
  
    $ bar_length = 0
    $ bar_choice_num = 0
   
    
    if choice_bar_1 is not None:
        $ bar_length += choice_bar_1
        $ bar_choice_num += 1

    if choice_bar_2 is not None:
        $ bar_length += choice_bar_2
        $ bar_choice_num += 1

    if choice_bar_3 is not None:
        $ bar_length += choice_bar_3
        $ bar_choice_num += 1

    if choice_bar_4 is not None:
        $ bar_length += choice_bar_4
        $ bar_choice_num += 1

    if choice_bar_5 is not None:
        $ bar_length += choice_bar_5
        $ bar_choice_num += 1

    if bar_length == None:
        text "error"
    elif bar_choice_num == 0:
        text "error"
    else:
        hbox:
            ysize 100
            xsize (bar_length * 10)
            yalign 0.5
            xalign 0.5
            if bar_choice_num >= 1:
                frame: 
                    ysize 100
                    xsize ((bar_length / bar_choice_num) * 10)
                    # background "images/test_choice_1.png"
            if bar_choice_num >= 2:
                frame:
                    ysize 100
                    xsize ((bar_length / bar_choice_num) * 10)
                    # background "images/test_choice_2.png"
            if bar_choice_num >= 3:
                frame:
                    ysize 100
                    xsize ((bar_length / bar_choice_num) * 10)
                    #background "images/test_choice_2.png"
            if bar_choice_num >= 4:
                frame:
                    ysize 100
                    xsize ((bar_length / bar_choice_num) * 10)
                    #background "images/test_choice_2.png"
            if bar_choice_num >= 5:
                frame:
                    ysize 100
                    xsize ((bar_length / bar_choice_num) * 10)
                    #background "images/test_choice_2.png"




    text "[bar_choice_num]" align(0.5,0.1)
    text "[bar_length]" align(0.5,0.2)
    text "[choice_bar_1]" align(0.5,0.3)

        







define choice_bar_1 = None
define choice_bar_2 = None
define choice_bar_3 = None
define choice_bar_4 = None
define choice_bar_5 = None

define bar_length = 10.0
define bar_choice_num = 0.0

define choice_text_1 = ""
define choice_text_2 = ""












        
