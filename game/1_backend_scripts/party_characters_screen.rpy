screen party_screen():
    tag menu

    use game_menu("Party"):

        vbox:
            xsize 1400
            ysize 850
            frame:
                xsize 1400
                ysize 500
                hbox:
                    yalign 0.5
                    style "party_spacing"
                    frame:
                        xsize 275
                        text "[player_slot_1.name]"
                    frame:
                        xsize 275
                        text "[player_slot_2.name]"
                    frame:
                        xsize 275
                        text "[player_slot_3.name]"
                    frame:
                        xsize 275
                        text "[player_slot_4.name]"
                    frame:
                        xsize 275
                        text "[player_slot_5.name]"



            frame:
                xsize 1400
                ysize 300
                vpgrid:
                    cols 30 #change when adding more characters
                    rows 1
                    xsize 1400
                    ysize 300
                    draggable True
                    scrollbars "horizontal"
                    yalign 0.5
                    xalign 0.5

                    frame:
                        xsize 275
                        ysize 275
                        text "[player_kit.name]"
                        if in_combat == True:
                            text "In Combat"
                        elif player_kit.name in party_list_names:
                            textbutton "Remove from Party":
                                    if player_kit.name == party_list_names[1]:
                                        action [SetDict(party_list_names, 1, ""), SetVariable("player_slot_2", player_2)]
                                    elif player_kit.name == party_list_names[2]:
                                        action [SetDict(party_list_names, 2, ""), SetVariable("player_slot_3", player_3)]
                                    elif player_kit.name == party_list_names[3]:
                                        action [SetDict(party_list_names, 3, ""), SetVariable("player_slot_4", player_4)]
                                    elif player_kit.name == party_list_names[4]:
                                        action [SetDict(party_list_names, 4, ""), SetVariable("player_slot_5", player_5)]
                        else:
                            textbutton "Add to Party":
                                action [SetVariable("add_to_party_temp", player_kit), Show("add_to_party")] 
                    frame:
                        xsize 275
                        ysize 275
                        text "[player_vida.name]"
                        if in_combat == True:
                            text "In Combat"
                        elif player_vida.name in party_list_names:
                            textbutton "Remove from Party":
                                if player_vida.name == party_list_names[1]:
                                    action [SetDict(party_list_names, 1, ""), SetVariable("player_slot_2", player_2)]
                                elif player_vida.name == party_list_names[2]:
                                    action [SetDict(party_list_names, 2, ""), SetVariable("player_slot_3", player_3)]
                                elif player_vida.name == party_list_names[3]:
                                    action [SetDict(party_list_names, 3, ""), SetVariable("player_slot_4", player_4)]
                                elif player_vida.name == party_list_names[4]:
                                    action [SetDict(party_list_names, 4, ""), SetVariable("player_slot_5", player_5)]
                        else:
                            textbutton "Add to Party":
                                action [SetVariable("add_to_party_temp", player_vida), Show("add_to_party")] 
                    frame:
                        xsize 275
                        ysize 275
                        text "[player_andrea.name]"
                        if in_combat == True:
                            text "In Combat"
                        elif player_andrea.name in party_list_names:
                            textbutton "Remove from Party":
                                if player_andrea.name == party_list_names[1]:
                                    action [SetDict(party_list_names, 1, ""), SetVariable("player_slot_2", player_2)]
                                elif player_andrea.name == party_list_names[2]:
                                    action [SetDict(party_list_names, 2, ""), SetVariable("player_slot_3", player_3)]
                                elif player_andrea.name == party_list_names[3]:
                                    action [SetDict(party_list_names, 3, ""), SetVariable("player_slot_4", player_4)]
                                elif player_andrea.name == party_list_names[4]:
                                    action [SetDict(party_list_names, 4, ""), SetVariable("player_slot_5", player_5)]
                        else:
                            textbutton "Add to Party":
                                action [SetVariable("add_to_party_temp", player_andrea), Show("add_to_party")] 
                    frame:
                        xsize 275
                        ysize 275
                        text "Neda"
                        text "Can't Add to Party"
                    frame:
                        xsize 275
                        ysize 275
                        text ""
                        text "Can't Add to Party"
                    frame:
                        xsize 275
                        ysize 275
                        text ""
                        text "Can't Add to Party"
                    

default add_to_party_temp = party_list[0]
screen add_to_party():
    vbox:
        pos(845,700)
        textbutton "Slot 2":
            action [SetVariable("player_slot_2", add_to_party_temp), SetDict(party_list_names, 1, add_to_party_temp.name), Hide("add_to_party")]
        textbutton "Slot 3":
            action [SetVariable("player_slot_3", add_to_party_temp), SetDict(party_list_names, 2, add_to_party_temp.name), Hide("add_to_party")]
        textbutton "Slot 4":
            action [SetVariable("player_slot_4", add_to_party_temp), SetDict(party_list_names, 3, add_to_party_temp.name), Hide("add_to_party")]
        textbutton "Slot 5":
            action [SetVariable("player_slot_5", add_to_party_temp), SetDict(party_list_names, 4, add_to_party_temp.name), Hide("add_to_party")]
        textbutton "cancel":
            action Hide("add_to_party")


          
            

                    
style party_spacing:
    spacing 3





## Character UI
screen character_screen():
    tag menu

    use game_menu("Characters"):

        hbox:
            ysize 1080
            xsize 1520
            frame:
                # Remove hashtag in the next line to remove the black and blue background
                background None
                style_prefix "character"
                ysize 1080
                xsize 400
                viewport:
                    area (100, 100, 300, 600)
                    mousewheel True
                    scrollbars "vertical"
                    vbox:
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
                            ######################################################################################################
                        textbutton [persistent.neda_profile.name]:
                            action SetVariable("persistent.selectedCharacter", persistent.neda_profile)
                            xsize 200

            frame:
                background None
                ysize 1080
                xsize 500
                vbox:
                    xalign 0.0
                    xsize 500
                    spacing 20
                    xoffset 50
                    text "Name: [persistent.selectedCharacter.name]"
                    text "Info: [persistent.selectedCharacter.desc]"

            frame:
                background None
                ysize 1080
                xsize 620

        if persistent.selectedCharacter.imageName == "locked profile":
            add persistent.selectedCharacter.imageName pos(1.0, 1.0)  xanchor 0.5
        else:
            add persistent.selectedCharacter.imageName pos(1.0, 1.0) anchor(0.5, 1.0) yoffset 45
                 

   

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



