
##
## If you use this code in your projects, credit me as Feniks @ feniksdev.com
##


define jay_pose = "armonhip"
define manic_pose = "armscrossed"
define kit_pose = "armscrossed"
define andrea_pose = "peacesign"
define vida_pose = "shush"

define neda_pose = "armhug"

init -50 python:
    def talking_callback(event, interact=True, image_talking = " ", ** kwargs): 
        
        if event == "begin":
            renpy.show(image_talking + " talking")
        elif event == "end":
            renpy.show(image_talking + " shut")

## jay ##

layeredimage jay_model:

    group pose:
        xanchor 0.5
        attribute pose default:
            "jay_[jay_pose]"
           
    group mouth:
        xanchor 0.5
        attribute shut default:
            "jay_[jay_pose]_mouth_shut"

    group eyes:
        xanchor 0.5
        attribute normal default EasyBlink(
            path="jay_[jay_pose]_eyes_{img}", img="normal",
            reverse=True, mid_eye_frames=["semi", "closed"],
        )
        attribute semi EasyBlink(
            path="jay_[jay_pose]_eyes_{img}", img="semi",
            mid_eye_frames=["closed"],
        )

        attribute closed "jay_[jay_pose]_eyes_closed"

        attribute normal_dissolve EasyBlink(
            path="jay_[jay_pose]_eyes_{img}", img="normal",
            reverse=True, mid_eye_frames=["semi", "closed"],
            transitions=Dissolve(0.4),
            blink_framerate=0.1,
        )

    group hair:
        xanchor 0.5
        attribute hair default:
            "jay_[jay_pose]_hair_base"

## manic ##

image manic_animation_talk:
    "images/characters/manic/manic_[manic_pose]/manic_[manic_pose]_mouth_open.png" with dissolve
    0.2
    "images/characters/manic/manic_[manic_pose]/manic_[manic_pose]_mouth_shut.png" with dissolve
    0.2
    repeat

layeredimage manic_model:

    group pose:
        xanchor 0.5
        attribute pose default:
            "manic_[manic_pose]"
           
    group mouth:
        xanchor 0.5
        attribute shut default:
            "manic_[manic_pose]_mouth_shut"
        attribute open:
            "manic_[manic_pose]_mouth_open"
        attribute talking:
            "manic_animation_talk"

    group eyes:
        xanchor 0.5
       
        attribute normal default EasyBlink(
            path="manic_[manic_pose]_eyes_{img}", img="normal",
            reverse=True, mid_eye_frames=["semi", "closed"],
        )
        attribute semi EasyBlink(
            path="manic_[manic_pose]_eyes_{img}", img="semi",
            mid_eye_frames=["closed"],
        )
        attribute lookleft EasyBlink(
            path="manic_[manic_pose]_eyes_{img}", img="lookleft_normal",
            reverse=True, mid_eye_frames=["lookleft_semi", "closed"],
        )
        attribute lookleft_semi EasyBlink(
            path="manic_[manic_pose]_eyes_{img}", img="lookleft_semi",
            mid_eye_frames=["closed"],
        )
        attribute lookright EasyBlink(
            path="manic_[manic_pose]_eyes_{img}", img="lookright_normal",
            reverse=True, mid_eye_frames=["lookright_semi", "closed"],
        )
        attribute lookright_semi EasyBlink(
            path="manic_[manic_pose]_eyes_{img}", img="lookright_semi",
            mid_eye_frames=["closed"],
        )

        attribute closed "manic_[manic_pose]_eyes_closed"

        attribute normal_dissolve EasyBlink(
            path="manic_[manic_pose]_eyes_{img}", img="normal",
            reverse=True, mid_eye_frames=["semi", "closed"],
            transitions=Dissolve(0.4),
            blink_framerate=0.1,
        )

    group hair:
        xanchor 0.5
        attribute hair default:
            "manic_[manic_pose]_hair_base"

layeredimage manic_model_profile:
    
    group pose:
        xanchor 0.5
        attribute pose default:
            "manic_armscrossed"
            
    group mouth:
        xanchor 0.5
        attribute shut default:
            "manic_armscrossed_mouth_shut"

    group eyes:
        xanchor 0.5
        attribute normal default EasyBlink(
            path="manic_armscrossed_eyes_{img}", img="normal",
            reverse=True, mid_eye_frames=["semi", "closed"],
        )
        
    group hair:
        xanchor 0.5
        attribute hair default:
            "manic_armscrossed_hair_base"

## kit ##

image kit_animation_talk:
    "images/characters/kit/kit_[kit_pose]/kit_[kit_pose]_mouth_open.png" with dissolve
    0.2
    "images/characters/kit/kit_[kit_pose]/kit_[kit_pose]_mouth_shut.png" with dissolve 
    0.2
    repeat 

layeredimage kit_model:

    group pose:
        xanchor 0.5
        attribute pose default:
            "kit_[kit_pose]"
            
    group mouth:
        xanchor 0.5
        attribute shut default:
            "kit_[kit_pose]_mouth_shut"
        attribute open:
            "kit_[kit_pose]_mouth_open"
        attribute grin:
            "kit_[kit_pose]_mouth_grin"
        attribute talking:
            "kit_animation_talk"

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

layeredimage kit_model_profile:
    
    group pose:
        xanchor 0.5
        attribute pose default:
            "kit_armscrossed"
            
    group mouth:
        xanchor 0.5
        attribute shut default:
            "kit_armscrossed_mouth_shut"

    group eyes:
        xanchor 0.5
        attribute normal default EasyBlink(
            path="kit_armscrossed_eyes_{img}", img="normal",
            reverse=True, mid_eye_frames=["semi", "closed"],
        )
        
    group hair:
        xanchor 0.5
        attribute hair default:
            "kit_armscrossed_hair_base"


## vida ##

image vida_animation_talk:
    "images/characters/vida/vida_[vida_pose]/vida_[vida_pose]_mouth_open.png" with dissolve
    0.2
    "images/characters/vida/vida_[vida_pose]/vida_[vida_pose]_mouth_shut.png" with dissolve
    0.2
    repeat

layeredimage vida_model:

    group pose:
        xanchor 0.5
        attribute pose default:
            "vida_[vida_pose]"
           
    group mouth:
        xanchor 0.5
        attribute shut default:
            "vida_[vida_pose]_mouth_shut"
        attribute open:
            "vida_[vida_pose]_mouth_open"
        attribute frown:
            "vida_[vida_pose]_mouth_frown"
        attribute talking:
            "vida_animation_talk"

    group eyes:
        xanchor 0.5
       
        attribute normal default EasyBlink(
            path="vida_[vida_pose]_eyes_{img}", img="normal",
            reverse=True, mid_eye_frames=["semi", "closed"],
        )
        attribute semi EasyBlink(
            path="vida_[vida_pose]_eyes_{img}", img="semi",
            mid_eye_frames=["closed"],
        )
        attribute lookleft EasyBlink(
            path="vida_[vida_pose]_eyes_{img}", img="lookleft_normal",
            reverse=True, mid_eye_frames=["lookleft_semi", "closed"],
        )
        attribute lookleft_semi EasyBlink(
            path="vida_[vida_pose]_eyes_{img}", img="lookleft_semi",
            mid_eye_frames=["closed"],
        )
        attribute lookright EasyBlink(
            path="vida_[vida_pose]_eyes_{img}", img="lookright_normal",
            reverse=True, mid_eye_frames=["lookright_semi", "closed"],
        )
        attribute lookright_semi EasyBlink(
            path="vida_[vida_pose]_eyes_{img}", img="lookright_semi",
            mid_eye_frames=["closed"],
        )
        attribute lookleftdown EasyBlink(
            path="vida_[vida_pose]_eyes_{img}", img="lookleftdown_normal",
            reverse=True, mid_eye_frames=["lookleftdown_semi", "closed"],
        )
        attribute lookleftdown_semi EasyBlink(
            path="vida_[vida_pose]_eyes_{img}", img="lookleftdown_semi",
            mid_eye_frames=["closed"],
        )

        attribute closed "vida_[vida_pose]_eyes_closed"

        attribute normal_dissolve EasyBlink(
            path="vida_[vida_pose]_eyes_{img}", img="normal",
            reverse=True, mid_eye_frames=["semi", "closed"],
            transitions=Dissolve(0.4),
            blink_framerate=0.1,
        )

    group glasses:
        xanchor 0.5
        attribute glasses default:
            "vida_[vida_pose]_glasses"
        attribute none:
            None

    group hair:
        xanchor 0.5
        attribute hair default:
            "vida_[vida_pose]_hair_base"

layeredimage vida_model_profile:
    
    group pose:
        xanchor 0.5
        attribute pose default:
            "vida_shush"
            
    group mouth:
        xanchor 0.5
        attribute shut default:
            "vida_shush_mouth_shut"

    group eyes:
        xanchor 0.5
        attribute normal default EasyBlink(
            path="vida_shush_eyes_{img}", img="normal",
            reverse=True, mid_eye_frames=["semi", "closed"],
        )
        
    group hair:
        xanchor 0.5
        attribute hair default:
            "vida_shush_hair_base"

## andrea ##

image andrea_animation_talk:
    "images/characters/andrea/andrea_[andrea_pose]/andrea_[andrea_pose]_mouth_open.png" with dissolve
    0.2
    "images/characters/andrea/andrea_[andrea_pose]/andrea_[andrea_pose]_mouth_shut.png" with dissolve
    0.2
    repeat

layeredimage andrea_model:

    group pose:
        xanchor 0.5
        attribute pose default:
            "andrea_[andrea_pose]"
           
    group mouth:
        xanchor 0.5
        attribute shut default:
            "andrea_[andrea_pose]_mouth_shut"
        attribute open:
            "andrea_[andrea_pose]_mouth_open"
        attribute smile:
            "andrea_[andrea_pose]_mouth_smile"
        attribute frown:
            "andrea_[andrea_pose]_mouth_frown"
        attribute talking:
            "andrea_animation_talk"

    group eyes:
        xanchor 0.5
       
        attribute normal default EasyBlink(
            path="andrea_[andrea_pose]_eyes_{img}", img="normal",
            reverse=True, mid_eye_frames=["semi", "closed"],
        )
        attribute semi EasyBlink(
            path="andrea_[andrea_pose]_eyes_{img}", img="semi",
            mid_eye_frames=["closed"],
        )
        attribute lookleft EasyBlink(
            path="andrea_[andrea_pose]_eyes_{img}", img="lookleft_normal",
            reverse=True, mid_eye_frames=["lookleft_semi", "closed"],
        )
        attribute lookleft_semi EasyBlink(
            path="andrea_[andrea_pose]_eyes_{img}", img="lookleft_semi",
            mid_eye_frames=["closed"],
        )
        attribute lookright EasyBlink(
            path="andrea_[andrea_pose]_eyes_{img}", img="lookright_normal",
            reverse=True, mid_eye_frames=["lookright_semi", "closed"],
        )
        attribute lookright_semi EasyBlink(
            path="andrea_[andrea_pose]_eyes_{img}", img="lookright_semi",
            mid_eye_frames=["closed"],
        )
        attribute lookleftdown EasyBlink(
            path="andrea_[andrea_pose]_eyes_{img}", img="lookleftdown_normal",
            reverse=True, mid_eye_frames=["lookleftdown_semi", "closed"],
        )
        attribute lookleftdown_semi EasyBlink(
            path="andrea_[andrea_pose]_eyes_{img}", img="lookleftdown_semi",
            mid_eye_frames=["closed"],
        )

        attribute closed "andrea_[andrea_pose]_eyes_closed"

        attribute normal_dissolve EasyBlink(
            path="andrea_[andrea_pose]_eyes_{img}", img="normal",
            reverse=True, mid_eye_frames=["semi", "closed"],
            transitions=Dissolve(0.4),
            blink_framerate=0.1,
        )

    group hair:
        xanchor 0.5
        attribute hair default:
            "andrea_[andrea_pose]_hair_base"

layeredimage andrea_model_profile:
    
    group pose:
        xanchor 0.5
        attribute pose default:
            "andrea_peacesign"
            
    group mouth:
        xanchor 0.5
        attribute shut default:
            "andrea_peacesign_mouth_shut"

    group eyes:
        xanchor 0.5
        attribute normal default EasyBlink(
            path="andrea_peacesign_eyes_{img}", img="normal",
            reverse=True, mid_eye_frames=["semi", "closed"],
        )
        
    group hair:
        xanchor 0.5
        attribute hair default:
            "andrea_peacesign_hair_base"

## neda ##

image neda_animation_talk:
    "images/characters/neda/neda_[neda_pose]/neda_[neda_pose]_mouth_open.png" with dissolve
    0.2
    "images/characters/neda/neda_[neda_pose]/neda_[neda_pose]_mouth_shut.png" with dissolve 
    0.2
    repeat 

layeredimage neda_model:

    group pose:
        xanchor 0.5
        attribute pose default:
            "neda_[neda_pose]"
            
    group mouth:
        xanchor 0.5
        attribute shut default:
            "neda_[neda_pose]_mouth_shut"
        attribute open:
            "neda_[neda_pose]_mouth_open"
        attribute talking:
            "neda_animation_talk"

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

layeredimage neda_model_profile:
    
    group pose:
        xanchor 0.5
        attribute pose default:
            "neda_armhug"
            
    group mouth:
        xanchor 0.5
        attribute shut default:
            "neda_armhug_mouth_shut"

    group eyes:
        xanchor 0.5
        attribute normal default EasyBlink(
            path="neda_armhug_eyes_{img}", img="normal",
            reverse=True, mid_eye_frames=["semi", "closed"],
        )
        
    group hair:
        xanchor 0.5
        attribute hair default:
            "neda_armhug_hair_base"