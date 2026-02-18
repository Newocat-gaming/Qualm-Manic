label minigame_tutorial:
    show tutorial_background

    i "You will be given two or more options. \nThe arrow above will Move between the available options."
    i "Select your desired option by using the Spacebar key when the arrow is above it.\nThe arrow will move faster over time."
    i "Good luck..."
    hide tutorial_background
    $ persistent.minigame_levels_unlock = True

    return