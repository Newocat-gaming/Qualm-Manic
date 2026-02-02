define config.end_splash_transition = Fade(2.0, 0.0, 2.0)

define fadesplash = Fade(2.0, 2.5, 2.0)
define titlefadesplash = Fade(3.0, 3.5, 3.0)

#transform fadesplash:
#    align (0.5, 0.5)
#    Fade(2.0, 2.5, 2.0)

image splash1 = "images/splashscreen/Ren'Py_Logo nc.png"
image splash2 = "images/splashscreen/Mannequin_Logo nc.png" 
image splash3 = "images/splashscreen/BCOF_Logo small nc.png" 
image title = "images/splashscreen/Qualm_manic.png"

image splashscreen_animation = Movie(size=(1920,1080), play="images/splashscreen/splashscreen_video.webm")
    
image splashscreen_animationtest = "images/splashscreen/Qualm_manic.png"

screen presplashskip:
    zorder 10
    textbutton "Skip ->" action Return() align(.95, .95)


label splashscreen:
    
    scene black
    play music "audio/Made_In_Japan_YoshiStudios lower.mp3" fadein 3.0
    show screen presplashskip
    show splashscreen_animation
    $ renpy.pause(16, hard=True)
    
    return
