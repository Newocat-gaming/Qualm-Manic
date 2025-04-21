screen character_UI():

    ## Ensure this appears on top of other screens.
    zorder 100

    if character_button:

        vbox:
            style_prefix "quick"

            align (1.0, 0.0)
            offset (-10, 10)

            textbutton "Characters" action ShowMenu('character_screen')

default character_button = False

## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:

    config.overlay_screens.append("character_UI")


## Character UI
screen character_screen():
    tag menu
    add "bg/bg sky.png"
    hbox:
        ysize 1080
        xsize 1920

        frame:
            background None
            ysize 1080
            xsize 400
            vbox:
                xpos gui.navigation_xpos 
                yalign 0.5
                spacing 20
                textbutton "Main characters":
                    action ShowMenu("character_screen"), SetVariable("persistent.selectedCharacter", persistent.jay_profile)
                    xsize 300
                textbutton "Side characters":
                    action ShowMenu("side_character_screen"), SetVariable("persistent.selectedCharacter", persistent.neda_profile)
                    xsize 300


            textbutton "Return":
                style "return_button"
                xpos gui.navigation_xpos
                yalign 1.0
                yoffset -45

                action Return()
    
        frame:
            # Remove hashtag in the next line to remove the black and blue background
            background None
            style_prefix "character"
            ysize 1080
            xsize 420
            vbox:
                xalign 0.5
                yalign 0.5
                textbutton [persistent.jay_profile.name]:
                    action SetVariable("persistent.selectedCharacter", persistent.jay_profile)
                    xsize 200
                textbutton [persistent.kit_profile.name]:
                    action SetVariable("persistent.selectedCharacter", persistent.kit_profile)
                    xsize 200
                textbutton [persistent.vida_profile.name]:
                    action SetVariable("persistent.selectedCharacter", persistent.vida_profile)
                    xsize 200
                textbutton [persistent.andrea_profile.name]:
                    action SetVariable("persistent.selectedCharacter", persistent.andrea_profile)
                    xsize 200
                textbutton [persistent.manic_profile.name]:
                    action SetVariable("persistent.selectedCharacter", persistent.manic_profile)
                    xsize 200

        frame:
            background None
            ysize 1080
            xsize 600
            vbox:
                xalign 0.0
                xsize 500
                xoffset 0
                yoffset 200
                spacing 20
                text "Name: [persistent.selectedCharacter.name]"
                text "Info: [persistent.selectedCharacter.desc]"

        frame:
            background None
            ysize 1080
            xsize 500

    if persistent.selectedCharacter.imageName == "locked profile":
        add persistent.selectedCharacter.imageName yalign 1.0 xpos 1600 xanchor 0.5
    else:
        add persistent.selectedCharacter.imageName yalign 1.0 xpos 1600  

screen side_character_screen():
    tag menu
    add "bg/bg sky.png"
    hbox:
        ysize 1080
        xsize 1920

        frame:
            background None
            ysize 1080
            xsize 400
            vbox:
                xpos gui.navigation_xpos 
                yalign 0.5
                spacing 20
                textbutton "Main characters":
                    action ShowMenu("character_screen"), SetVariable("persistent.selectedCharacter", persistent.jay_profile)
                    xsize 300
                textbutton "Side characters":
                    action ShowMenu("side_character_screen"), SetVariable("persistent.selectedCharacter", persistent.neda_profile)
                    xsize 300

            textbutton "Return":
                style "return_button"
                xpos gui.navigation_xpos
                yalign 1.0
                yoffset -45

                action Return()
    
    
        ## LEFT FRAME
        frame:
            #Remove hashtag in the next line to remove the black and blue background
            background None
            style_prefix "character"
            ysize 1080
            xsize 420
            vbox:
                xalign 0.5
                yalign 0.5
                textbutton [persistent.neda_profile.name]:
                    action SetVariable("persistent.selectedCharacter", persistent.neda_profile)
                    xsize 200

        ## RIGHT FRAME
        frame:
            background None
            ysize 1080
            xsize 600
            vbox:
                xalign 0.0
                xsize 500
                xoffset 0
                yoffset 200
                spacing 20
                text "Name: [persistent.selectedCharacter.name]"
                text "Info: [persistent.selectedCharacter.desc]"

        frame:
            background None
            ysize 1080
            xsize 500   

    if persistent.selectedCharacter.imageName == "locked profile":
        add persistent.selectedCharacter.imageName yalign 1.0 xpos 1600 xanchor 0.5
    else:
        add persistent.selectedCharacter.imageName yalign 1.0 xpos 1600 
       
style character_button_text:
    xalign 0.5

python early:
    class CharacterProfile:
        def __init__(self, name = "???", imageName = "", desc = "", trueName = ""):
            self.name = name
            #### The portraits are located in game/images/characters folder
            #### self.imageName = "character profiles/"+ imageName + ".png"
            self.imageName = imageName
            self.desc = desc
            self.trueName = trueName

        def __eq__(self, other):

            if isinstance(other, CharacterProfile):

            # Check if all their attributes are the same
                return (self.name == other.name
                    and self.imageName == other.imageName
                    and self.desc == other.desc
                    and self.trueName == other.trueName)

            # If not, they can't possibly be the same
            else:
                return False

        def __ne__(self, other):
            return not self.__eq__(other)

default persistent.jay_profile = CharacterProfile(name="???", imageName="locked profile", desc = "???", trueName = "jay")
default persistent.kit_profile = CharacterProfile(name="???", imageName="locked profile", desc = "???", trueName = "kit")
default persistent.vida_profile = CharacterProfile(name="???", imageName="locked profile", desc = "???", trueName = "vida")
default persistent.andrea_profile = CharacterProfile(name="???", imageName="locked profile", desc = "???", trueName = "andrea")


default persistent.manic_profile = CharacterProfile(name="???", imageName="locked profile", desc = "???", trueName = "manic")

default persistent.neda_profile = CharacterProfile(name="???", imageName="locked profile", desc = "???", trueName = "neda")

default persistent.selectedCharacter = persistent.jay_profile



