##
define wait_for_vida = False
##
label wait_for_vida:

    ###########################################################################################
    return
    ###########################################################################################

    $ wait_for_vida = True

    nar "I stand still and turn to face Vida."
    show vida nervous at middle
    vida "Are you ok Jay?"
    vida "You walked out all of a sudden..."
    jay "Y-yeah... I'm alright, just needed a second to think."
    vida "Is it about the murder?"
    jay "Yes. I'm just a little concerned about covering it."
    show vida explaining at middle
    vida "Well I am too, but I think whatever Kit knows will help keep the club afloat."
    vida "How about we go back to the club room and at least listen to what he has to say."
    vida "Ok?" 

    menu:
        nar "I think about it and decide to..."
        # A #
        "Walk back to the club room":
            jump hear_what_kit_has_to_say
        # BAB #
        "Leave":
            jump walk_out_of_school
