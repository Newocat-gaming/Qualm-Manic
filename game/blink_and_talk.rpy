
##
## Explanatory comments have been added all throughout this file.
##
## If you use this code in your projects, credit me as Feniks @ feniksdev.com
##



define manic_pose = "armscrossed"
define kit_pose = " "
define andrea_pose = "armscrossed"
define vida_pose = "armscrossed"

define neda_pose = " "

init -50 python:
    def talking_callback(event, interact=True, image_talking = " ", ** kwargs): 
        
        if event == "begin":
            renpy.show(image_talking + " talking")
        elif event == "end":
            renpy.show(image_talking + " shut")


## kit ##


image kit_armscrossed_animation_talk:
    "images/characters/kit/kit_armscrossed/kit_armscrossed_mouth_open.png" with dissolve
    0.2
    "images/characters/kit/kit_armscrossed/kit_armscrossed_mouth_shut.png" with dissolve 
    0.2
    repeat 

image kit_explaining_animation_talk:
    "images/characters/kit/kit_explaining/kit_explaining_mouth_open.png" with dissolve
    0.2
    "images/characters/kit/kit_explaining/kit_explaining_mouth_shut.png" with dissolve 
    0.2
    repeat 


layeredimage kit_model:

    group pose:
        xanchor 0.5
        attribute armscrossed default:
            "kit_[kit_pose]"
            
    group mouth:
        xanchor 0.5
        attribute shut default:
            "kit_[kit_pose]_mouth_shut"
        attribute open:
            "kit_[kit_pose]_mouth_open"
        attribute talking:
            "kit_[kit_pose]_animation_talk"

    group eyes:
        xanchor 0.5
       
        attribute normal default EasyBlink(
            path="kit_[kit_pose]_eyes_{img}", img="normal",
            reverse=True, mid_eye_frames=["semi", "closed"],
        )
        attribute semi EasyBlink(
            path="kit_[kit_pose]_eyes_{img}", img="semi",
            mid_eye_frames=["closed"],
        )
        attribute lookleft EasyBlink(
            path="kit_[kit_pose]_eyes_{img}", img="lookleft_normal",
            reverse=True, mid_eye_frames=["lookleft_semi", "closed"],
        )
        attribute lookleft_semi EasyBlink(
            path="kit_[kit_pose]_eyes_{img}", img="lookleft_semi",
            mid_eye_frames=["closed"],
        )
        attribute lookright EasyBlink(
            path="kit_[kit_pose]_eyes_{img}", img="lookright_normal",
            reverse=True, mid_eye_frames=["lookright_semi", "closed"],
        )
        attribute lookright_semi EasyBlink(
            path="kit_[kit_pose]_eyes_{img}", img="lookright_semi",
            mid_eye_frames=["closed"],
        )

        attribute closed "kit_[kit_pose]_eyes_closed"


        attribute normal_dissolve EasyBlink(
            path="kit_[kit_pose]_eyes_{img}", img="normal",
            reverse=True, mid_eye_frames=["semi", "closed"],
            transitions=Dissolve(0.4),
            blink_framerate=0.1,
        )

    group hair:
        xanchor 0.5
        attribute hair default:
            "kit_[kit_pose]_hair_base"
 


## neda ##

image neda_armhug_animation_talk:
    "images/characters/neda/neda_armhug/neda_armhug_mouth_open.png" with dissolve
    0.2
    "images/characters/neda/neda_armhug/neda_armhug_mouth_shut.png" with dissolve 
    0.2
    repeat 

layeredimage neda_model:

    group pose:
        xanchor 0.5
        attribute armscrossed default:
            "neda_[neda_pose]"
            
    group mouth:
        xanchor 0.5
        attribute shut default:
            "neda_[neda_pose]_mouth_shut"
        attribute open:
            "neda_[neda_pose]_mouth_open"
        attribute talking:
            "neda_[neda_pose]_animation_talk"

    group eyes:
        xanchor 0.5
       
        attribute normal default EasyBlink(
            path="neda_[neda_pose]_eyes_{img}", img="normal",
            reverse=True, mid_eye_frames=["semi", "closed"],
        )
        attribute semi EasyBlink(
            path="neda_[neda_pose]_eyes_{img}", img="semi",
            mid_eye_frames=["closed"],
        )
        attribute lookleft EasyBlink(
            path="neda_[neda_pose]_eyes_{img}", img="lookleft_normal",
            reverse=True, mid_eye_frames=["lookleft_semi", "closed"],
        )
        attribute lookleft_semi EasyBlink(
            path="neda_[neda_pose]_eyes_{img}", img="lookleft_semi",
            mid_eye_frames=["closed"],
        )
        attribute lookright EasyBlink(
            path="neda_[neda_pose]_eyes_{img}", img="lookright_normal",
            reverse=True, mid_eye_frames=["lookright_semi", "closed"],
        )
        attribute lookright_semi EasyBlink(
            path="neda_[neda_pose]_eyes_{img}", img="lookright_semi",
            mid_eye_frames=["closed"],
        )

        attribute closed "neda_[neda_pose]_eyes_closed"


        attribute normal_dissolve EasyBlink(
            path="neda_[neda_pose]_eyes_{img}", img="normal",
            reverse=True, mid_eye_frames=["semi", "closed"],
            transitions=Dissolve(0.4),
            blink_framerate=0.1,
        )

    group hair:
        xanchor 0.5
        attribute hair default:
            "neda_[neda_pose]_hair_base"










## This is a short screen that shows how you can make a preference toggle
## to turn blinking on/off on a global basis.
screen toggle_blinking():
    textbutton "Turn blinking {}".format("off" if persistent.blinking_on else "on"):
        background "#000" text_color "#fff" text_hover_color "#bbb"
        align (0.5, 0.0)
        action ToggleField(persistent, "blinking_on")

label test_blinks():
    scene expression "#21212d"
    ## This screen has a button to toggle blinking on and off. It's for
    ## demonstration purposes; usually you'd have this in your settings screen.
    show screen toggle_blinking()
    "Blink test, normal expression."
    show kit_model head_only at right
    "test"
    show kit_model gestureright at right
    "test"
    show kit_model shrug at right
    "test"
    ## Jump to the examples for the extra files, if present.
    if renpy.has_label("test_blinks_auto"):
        call test_blinks_auto()

    jump test_blinks
