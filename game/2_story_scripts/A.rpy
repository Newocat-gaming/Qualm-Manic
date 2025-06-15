label hear_what_kit_has_to_say:

    #######################################
    return
    ###############################################

    if wait_for_vida:
        
        scene bg classroom 2
        show kit armscrossed at right
        show andrea neutral at middle
        show vida behindback at left

        kit "You good Jay?"
        andrea "Yeah is everything alright?"
        jay "Yeah yeah I'm fine..."
        jay "Can we just continue from where we left off?"
        kit "Of course! Let me tell you all what I know!"
        kit "It's something that will definitely save our club!"
        nar "He leaned in and smiled." 

    show kit smug at right
    kit "I know where the human kebab murder happened..."
    show vida nervous at left
    show andrea nervous at middle
    nar "Kit whispered."
    nar "The rest of us in the club room couldn't even speak."
    vida "H-how?"
    kit "I was hoping you would have asked where... To answer your question..."
    kit "I was watching the news about it when I noticed something in the alley that looked familiar." 
    jay "What was it?" 
    kit "I saw a sign in the background that had a sticker on it."
    show kit handing sticker
    nar "Kit reached into his pocket and pulled out a sticker with a bird emblem on it."
    kit "This sticker." 
    nar "The three of us stood there shocked, before we could say anything Kit explained."
    kit "This is from the same pack of stickers I had as a kid. I used to take a shortcut to school through some alleyways and placed these stickers along the way in case I got lost."
    kit "So years ago I must have placed that sticker next to where the murder recently took place."
    show kit raised arms at right
    nar "He leaned back in his chair and pumped both his hands in the air."
    kit "Which means! I know where it happened..."

    stop music
    hide kit
    hide andrea
    hide vida
    scene bg blank

    nar "The next day, all four of us were standing on the rooftop of a building during sunset."

    scene bg rooftop 1
    play  music "audio/rooftop wind sound.mp3" volume 0.5 fadeout 2.0 fadein 2.0

    jay "I can't believe you convinced me to do this..." 
    show kit armscrossed at middle
    kit "You don't want the club to be disbanded, do you?" 
    hide kit
    nar "Kit made the jump from one rooftop to the next."
    jay "So what's the plan again?"
    show andrea armsonhips at left
    andrea "Find murder site, find new info, write paper, profit." 
    nar "Andrea said as she was jumping in place in order to prepare herself for the jump. The jump itself was only around two feet but still felt massive when they were so high up." 
    show vida wave at right
    vida "How many of these jumps do we have to do?"
    nar "She said already on the other side of the gap."
    show kit raised arms at middle
    kit "I don't know!"
    nar "Kit shouted cheerfully. This was not what Jay expected to be doing instead of today's assembly."
    jay "You sure we should be doing this, it's technically still school hours?"
    show kit sigh at middle
    kit "Stop worrying, you didn't want to go to it anyways, and we have to strike the iron while it's hot." 

    menu:
        "I thought about it, standing on the roof across from my friends."
        # AA #
        "Take the Jump.":
            jump jump_along_rooftops 
        # AB #
        "Leave now.":
            jump walk_away_from_rooftops
