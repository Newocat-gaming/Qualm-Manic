define config.end_splash_transition = Fade(2.0, 0.0, 2.0)


define fadesplash = Fade(2.0, 0.0, 2.0)
define titlefadesplash = Fade(3.0, 0.0, 3.0)

image splash1 = "images/splashscreen/Ren'Py_Logo nc.png" 
image splash2 = "images/splashscreen/Mannequin_Logo nc.png" 
image splash3 = "images/splashscreen/BCOF_Logo small nc.png" 
image title = "images/splashscreen/Qualm_manic.png"

label splashscreen:
    scene black

    show splash1 at truecenter
    show text "Made with"at truecenter:
        yoffset(-180)
    with fadesplash
    with Pause(2)

    scene black
    with fade

    show splash2 at truecenter
    show text "Made with"at truecenter:
        yoffset(-100)
    with fadesplash
    with Pause(2)
    
    scene black
    with fade

    show splash3 at truecenter
    with fadesplash
    with Pause(2)

    scene black
    with fade

    show title at truecenter
    with titlefadesplash
    with Pause(3)

    return