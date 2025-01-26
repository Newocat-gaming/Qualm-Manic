
image jay animation_talk:
    "jay head/jay talking.png" with dissolve
    0.2
    "jay head/jay shut.png" with dissolve 
    0.2
    repeat

init -50 python:

    def talking_callback(event, interact=True, image_talking = " ", ** kwargs):
        if event == "begin":
            renpy.show(image_talking + " animation_talk")
        elif event == "end": 
            renpy.show(image_talking + " shut")


