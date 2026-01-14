
label test:

    $ manic_pose = "armscrossed"
    show manic_model at middle

    manic "test"
    jay "holy hell" 
    manic "I know right"

    call minigame_testing
  
    return








```

    $ cont = 0 #continue variable
    $ arr_keys = ["a", "c", "e", "K_UP", "K_SPACE"] #list of keyboard inputs to be selected from. See https://www.pygame.org/docs/ref/key.html for more keys

    call qte_setup(5, 5, 0.01, renpy.random.choice(arr_keys), renpy.random.randint(1, 9) * 0.1, renpy.random.randint(1, 9) * 0.1)
    # "Function Call" - see label qte_setup for detail on "function"
    # in the above, I randomly select a key from a previously defined set of keys (arr_keys), and randomise the location

    while cont == 1:
        call qte_setup(5, 5, 0.01, renpy.random.choice(arr_keys), renpy.random.randint(1, 9) * 0.1, renpy.random.randint(1, 9) * 0.1)
        # to repeat the qte events until it is missed

    "{b}GAME OVER{/b}"

    return
```

'''
"Function"/pseudo-function
calls the qte screen
parameters are:
    - amount of time given
    - total amount of time (is usually the same as above)
    - timer decreasing interval
    - the key/keyboard input to hit in the quick time event
    - the x alignment of the bar/box
    - the y alignment of the bar/box
'''
label qte_setup(time_start, time_max, interval, trigger_key, x_align, y_align):

    $ time_start = time_start
    $ time_max = time_max
    $ interval = interval
    $ trigger_key = trigger_key
    $ x_align = x_align
    $ y_align = y_align

    call screen qte_simple
    # can change to call screen qte_button to switch to button mode

    $ cont = _return
    # 1 if key was hit in time, 0 if key not

    return


screen qte_simple:
    #key input qte

    timer interval repeat True action If(time_start > 0.0, true=SetVariable('time_start', time_start - interval), false=[Return(0), Hide('qte_simple')])
    # timer, using variables from label qte_setup
    # false is the condition if the timer runs out - and this will be reached if the user doesn't get hit the key on time

    key trigger_key action ( Return(1) )
    # the "key detector" (ends qte_event by returning 1)

    vbox:
        xalign x_align
        yalign y_align
        spacing 25
        # vbox arrangement

        text trigger_key:
            xalign 0.5
            color "#fff"
            size 36
            #outlines [ (2,"#000000",0,0) ]
            # text showing the key to press

        bar:
            value time_start
            range time_max
            xalign 0.5
            xmaximum 300
            if time_start < (time_max * 0.25):
                left_bar "#f00"
                # this is the part that changes the colour to red if the time reaches less than 25%


#########################################################################

define choice_1 = None
define choice_2 = None
define choice_3 = None
define choice_4 = None

define bar_choice_num = 0

define choice_text_1 = ""
define choice_text_2 = ""
define choice_text_3 = ""
define choice_text_4 = ""


label minigame_testing:

    $ bar_choice_num = 4
    $ choice_text_1 = "test1"
    $ choice_text_2 = "test2"
    $ choice_text_3 = "test3"
    $ choice_text_4 = "test4"

    call screen minigame

##################################################

screen minigame:
   
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




    text "test: [bar_choice_num]" align(0.5,0.1)
    
        
















        
