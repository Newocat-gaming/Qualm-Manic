label walk_out_of_the_room:

    hide vida_model
    hide andrea_model
    hide kit_model
    scene bg hallway 3

    nar "I leave the club room..."
    nar "I can't handle this anymore..."
    nar "My friends whom I have usually found comfort in had started to make me uncomfortable."
    vida2 "Jay!"
    vida2 "Wait up!"

    menu:
        jay "..."
        # BA #
        "Wait for Vida":
            jump wait_for_vida
        # BB #
        "Leave":
            jump walk_out_of_school