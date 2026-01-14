transform rightside:
    yalign 1.0
    xpos 1600

transform rightsidestill:
    yalign 1.0
    xpos 1600
    xanchor 0.5

transform middle:
    yalign 1.0
    xpos 960

transform leftside:
    yalign 1.0
    xpos 320

transform leftsidestill:
    yalign 1.0
    xpos 320
    xanchor 0.5

label start:

    ###############################
    call test
    ##################################


    stop music fadeout 4
    scene bg blank
    nar "I wake up with a start." 
    nar "It's that damn dream again."
    nar "I can't even describe what it's about. In my mind it's nothing but a gray blur."
    nar "I scratch my head, my hand passing through my long black hair. I turn over, only for my eyes to meet my alarm clock."

    jay "Shit..."
    jay "I'm gonna be late for school."

    scene bg street_summer_day
    play music "audio/vntrack01.mp3" volume 0.5 fadein 2.0 

    nar "Soon, I'm dashing down the street, the wind brushing against my white dress-shirt and black pants. My shoes clop on the ground as I run over the crosswalk, dodging out of the way of an oncoming car that misses me by about an inch."
    nar "I barely pay any attention to the honking cars, however, as my one and only focus is getting to the high school on time. If I get caught by any of the teachers for being late, I will most certainly be sent to detention after school, and that would be catastrophic, not even just for the normal reasons." 
    nar "Detention doesn't matter to me; all I care about is my club."
    nar "I'm part of the newspaper club, where my only friends and I go around and write about anything notable we encounter. I don't actually care about reporting or writing; I just like to slack off with my friends." 
    nar "I do like reading though, or more accurately, I love reading ... too much for my own good, it turns out, as reading all night long is what threw off my sleep schedule and caused me to wake up later than usual."
    
    call char_jay_update from _call_char_jay_update

    scene bg school_exterior
    nar "I arrive just in time at the front gates of the school. With a sigh of relief, I walk through the door of Leadville High."
    
    scene bg classroom 1
    nar "Even though I'm almost late, I still have time to relax. My teacher for my first class is often a little late too, so when I walk into class and see everyone chilling and messing around, I stop worrying about the time."

    play music "audio/The Protagonist.wav" volume 0.5 fadeout 1.5 fadein 3.0

    nar "I slump into my chair. My classmates appear to be mingling and chatting as usual, but something is off about the atmosphere of the room, and I can't seem to place what it is."

    i "Hey!" 
    nar "I turn my head towards the cheerful voice."

    $ kit_pose = "armscrossed"
    show kit_model at rightside

    nar "It's Kit, one of my friends from the newspaper club." 

    call char_screen_update from _call_char_screen_update
    call char_kit_update from _call_char_kit_update

    kit "..."
    
    $ kit_pose = "explaining"

    kit "I saw you run by through the window... almost late it seems." 
    nar "Kit usually teases me like this."
    jay "Yeah, yeah"
    nar "I groan as I slump my face between my arms, which I have crossed on my desk." 
    jay "I spent all night reading."
    
    $ kit_pose = "armscrossed"
    show kit_model open closed

    kit "You sure do love your books, huh?" 

    nar "Before I can respond, the door creaks open. Our teacher has just arrived to class earlier than she usually does." 

    show kit_model shut lookright

    kit "Oh shit."
    nar "He turns back towards his own desk not wanting to get caught away from it. But before he can get even a foot away from me he freezes and turns his head back to me." 

    show kit_model normal

    kit "By the way... I got some big info to share with everyone in the club tonight, be ready." 
    nar "He smirks and continues to his desk before the teacher starts to take attendance."
    
    hide kit_model

    nar "Kit always has interesting things to bring up during club, but this time he said this in a more uneasy tone than that was his usual voice." 
    nar "I assume he was adding more intrigue to really get me riled up. Knowing Kit, he has probably already riled up the others in the club as well. One thing I am expecting is that they won't be getting any work done for the newspaper today."
    nar "I'm so lost in thought that I almost miss my cue when my name is called for attendance. After my name is called I relax back in my chair and continue to observe my classmates." 
    nar "Kit is twirling his pencil, not paying attention to the teacher."
    nar "Nothing new there, but it isn't just Kit; it is almost everyone in class."
    nar "Of course, there are a few overattentive students still focusing, but most others are whispering and passing notes to each other."
    nar "They can't seem to shut up about something, and they aren't hiding it either." 
    nar "Our teacher starts out annoyed at all the chatter, throwing a few 'Quiet down' or 'stop that' requests at the troublemaking students but gradually gives up on trying to make the class listen to her with less and less objections as the class goes on." 
    nar "When I notice that the only authority in the room has abandoned all attempts at regulation I start to feel left out on whatever this is."
    nar "I whisper to the girl seated to the left of me, I think her name is Neda if I remember correctly."

    $ neda_pose = "armhug"
    show neda_model at leftside
    
    call char_neda_update from _call_char_neda_update

    jay "Hey, what's everyone talking about?" 
    nar "She leans towards me and cups her hand around the side of her mouth."
    neda "You haven't heard? Did you not watch the news this morning or something?"
    jay "No, I woke up late, what happened?"

    stop music fadeout 1.0

    neda "..."
    neda "Well..." 
    nar "she whispers cautiously."
    neda "They're calling it the Human Kebab."

    hide neda
    scene bg blank

    $ renpy.movie_cutscene("images/videos/animation v03.webm", delay=None, loops=0, stop_music=True)
   
    scene bg cafeteria 1
    play music "audio/vntrack12.mp3" volume 0.5 fadein 2.0

    nar "I sit staring out the window during lunch as my nachos get cold." 
    nar "I shiver again as I have done many times since my first class. The human kebab is what is on my mind." 
    nar "I haven't seen any pictures so I can only use my imagination. I review what has been told to me by different people I have talked to over the course of the morning."
    nar "I try to compile all the information in my mind." 
    nar "In short it is a murder case: a very disturbing one. Last night a body had been found in an alley, with its limbs severed and all the pieces impaled onto a piece of rebar in a fashion that resembled a kebab, as the name implies." 
    nar "It was a truly gruesome sight with blood splattered everywhere. Suicide was ruled out almost immediately and it was determined that the murder clearly happened on location." 
    nar "The body was so disfigured that the police hadn't been able to identify it. Apparently there was no evidence left behind either, or at least none has been found left behind." 
    i "The killer is said to still be on the loose... and no one knows why they did it"
    nar "I hear from one classmate nearby"
    i "Who knows if or when they could strike again"
    nar "I hear from another"
    nar "On another note, an announcement had been given during my second class that tomorrow there would be an assembly to discuss how to keep yourself safe and what to do if you see someone suspicious. They also said not to go in public alone, especially at night."
    nar "When I leave lunch for my next class, I am hoping that the murderer will be caught before I have to waste any time at an assembly." 

    scene bg classroom 1

    nar "When I sit down at my desk, I check my watch, only to realize I had left it during my rush in the morning." 
    jay "Dammit"
    nar "I take out my flip phone to check the time instead." 
    nar "1:03."
    nar "Only 2 more classes until I am free form this torture and can forget all of today's absurdity." 
    nar "I let my mind wander to my friends, Kit, Vida, Andrea, and James, all laughing at some stupid joke together." 
    nar "It has only been a weekend since we have been together, but I felt like I haven't seen them in forever." 
    nar "I also think that I need them more now than ever, after all it was only the start of the week and so much has happened already."

    scene bg hallway 3

    nar "I walk through the hallways after my last class of the day..."
    nar "I look around at the walls, which are covered with signage for different school clubs."
    nar "The walls are painted white and maroon red, supposedly the colors of the school mascot. Although Leadville high had infamously failed in sports so they haven't used a mascot in many years. I can't even remember what the mascot is supposed to be."
    nar "I climb the stairs, past a group of gossiping girls and continue to the second floor."
    nar "That is where the newspaper club is located. I stop at the top of the stairs to look at a billboard filled with more posters."
    nar "I often find myself looking at the board in my free time. This one has everything: all the clubs, student jobs, class openings, anything a student could ask for." 
    nar "Well, almost anything, as there sits an empty spot where the newspaper club is supposed to post their contribution to the school."
    nar "It is barren, and has been for a while. Me and my friends don't really put in the work for the newspaper so we haven't actually produced anything in a long while."
    nar "Although no one seems to care that it is absent so I think 'why bother?'" 
    nar "I continue to scan the board until I see the words 'Human Kebab'."
    
    play music "audio/Dark Atmosphere to Synth.wav" volume 0.25 fadeout 2.0 fadein 3.0

    nar "I lower my head to the ground and turn down the rest of the hallway. I can't deal with whatever else it says, I just can't handle it right now." 
    nar "I march onwards toward the door with the hanging sign that reads 'Newspaper Club'."

    scene bg classroom 2 reverse
    play music "audio/vntrack01.mp3" volume 0.5 fadeout 0.5 fadein 1.0 

    nar "When I walk into the club room, most of the other members are already there." 

    $ vida_pose = "behindback"
    show vida_model at leftside

    nar "Vida leans against the wall next to a rollable whiteboard."

    call char_vida_update from _call_char_vida_update

    $ andrea_pose = "peacesign"
    show andrea_model at middle

    nar "Andrea is sitting in a chair at the rectangular table in the center of the room."

    $ andrea_pose = "onearmonhip"

    call char_andrea_update from _call_char_andrea_update

    $ kit_pose = "armscrossed"
    show kit_model at rightside

    nar "Kit is sitting atop the same table." 
    nar "While I enter the cluttered room, he looks around and notices that someone is missing." 
    jay "Where's James?"
    nar "James is the unofficial leader of the group and the president of the club." 
    nar "I recall the first time I and James met, James was incredibly helpful when no one else noticed me struggling to carry... carry what? I can't remember exactly..."
    nar "II decide to ignore it, what matters is that James was friends with everyone here individually first then he introduced everyone to each other. Therefore having a meet up without him feels a little awkward for me."
    andrea "He hasn't come in yet." 
    nar "She is tapping away at her phone. She leans back in her chair with her legs on the table in the center of the room."
    vida "No one's seen him all day."

    $ kit_pose = "shrug"
    show kit_model closed at rightside

    kit "He might be sick."
    nar "Kit says while smiling at me, though to me the smile looks more like a frown, as Kit is lying on his back with his head hanging over the edge of the table."
    nar "Kit continues to smile at me, then when he gets no feedback on his quirky position he tries again with Andrea and Vida."

    $ kit_pose = "armscrossed"
    show kit_model lookright_semi open

    kit "Y'all are no fun..."
    hide kit_model
    show kit hurt at rightsidestill 
    $ andrea_pose = "armsonhips"
    show andrea_model smile lookright at middle
    
    nar "He turns over onto his stomach, only to be kicked on the head by Andrea, who shows her full appreciation to Kit's stunt with a smug grin of her own."
    hide kit hurt
    show kit_model open lookleft_semi at rightside
    nar "While the two friends bicker in the background, Vida turns to me."
    vida "I hope it isn't bad."
    jay "Huh? Oh right, James..."
    nar "I was briefly distracted by the argument happening beside us."
    jay "Knowing him, it won't keep him down for lon-"

    $ kit_pose = "explaining_armonhip"
    show kit_model shut normal at rightside
    show vida_model shut lookright at leftside
    show andrea_model open lookright at middle

    kit "Alrighty then!" 
    nar "Kit shouts, cutting me off." 
    show andrea_model shut lookright at middle
    nar "He turns around, seemingly mid conversation with Andrea, and climbs atop the table he had once been lying on. He turns, once again, to address his audience of three newspaper club members." 
    kit "Since James isn't here, we'll have to start without him!"
    jay "Start what?" 

    $ kit_pose = "gesture"

    nar "Kit crouches down and leans towards me." 
    kit "Our venture to make the newspaper club relevant again!"
    jay "No one cares about the school newspaper anymore..."
    vida "No one has ever cared about it."
    nar "Kit ignores her and continues talking."

    $ kit_pose = "explaining"

    kit "That's a problem because I heard that the school is gonna start closing clubs that they deem unnecessary, so we have to make sure we're not on that list."
    andrea "Wait, so the club could be disbanded!?"
    kit "It's not..."
    kit "Because I have a plan, all we have to do is make people read a paper we put out and the school will automatically accept us."
    jay "Ok..."
    jay "That makes sense..."
    jay "But what could we write about to ever make people read the paper?" 
    andrea "That would require us to do work though..."
    vida "What is there even to write about in this school?"

    $ kit_pose = "armscrossed"
    show kit_model grin at rightside

    nar "The group continues to question each other for a little while as Kit watches with an eager grin on his face."
    kit "Silence!" 
    kit "I have everything laid out already!"
    andrea "Where?" 
    nar "Vida sarcastically asks." 
    kit "In my head."
    nar "He acknowledges her for the first time in a while. The room is silent for a moment with everyone staring at Kit." 
    kit "I have the perfect topic that will make everyone read our paper..."
    
    $ kit_pose = "explaining_armonhip"

    nar "He jumps off the table he was still atop and lands in front of a crowd eager for him to get to the point."
    kit "It will keep our club alive and well, while being relatively low effort!" 

    show kit_model lookleft at rightside

    nar "He says turning toward Vida for the last part."
    jay "Well what is the topic?" 
    nar "I ask, annoyed with Kit's shenanigans."

    play  music "audio/Dark Atmosphere to Synth.wav" volume 0.25 fadeout 2.0 fadein 5.0

    $ kit_pose = "armscrossed" 
    show kit_model normal at rightside

    nar "Kit leans in the direction of Jay and slowly turns his head to also face him."
    nar "He whispers..."
    kit "The Human Kebab..."

    $ andrea_pose = "nervous"
    show andrea_model lookleftdown frown
    $ vida_pose = "nervous"
    show vida_model lookleftdown frown
    
    jay "What!!"
    vida "..."
    andrea "..."

    show andrea_model lookleftdown frown
    show vida_model lookleftdown frown

    jay "Can't we just do an article about the status of the school's water fountains?"
    nar "I ask half jokingly."
    nar "It's clear the three of us have worries about covering the topic. Though Kit waves his hands as if to calm us down."

    $ kit_pose = "raisedarms"

    kit "Just think about it... it's the talk of the town... so everyone will read the paper!"
    kit "Also we can't get in trouble for covering it because we can force an outcry from the students if the teachers try to take it down..."
    kit "It's almost guaranteed to garner attention to the club!"

    $ kit_pose = "armscrossed"
    show kit_model at rightside

    nar "We all think about it for a minute."
    andrea "I hate to admit it but you might have come up with a good idea..."

    show andrea_model lookright
    show vida_model lookright

    nar "Vida nods."
    nar "I am still concerned as I try to think of a way out of this."
    jay "B-But since it's so popular... Everyone already knows everything about it from the news... so there's no use in us covering it... right?"

    show andrea_model lookleftdown frown
    show vida_model lookleftdown frown

    nar "I watch my friends' faces and see Vida and Andrea seem to reconsider the idea..."
    nar "But all hopes of getting out of this are shattered when Kit utters the words:"
    show kit_model grin at rightside
    kit "I haven't yet shared what I told you all about this morning..."
    show kit_model grin at rightside

    menu:
        "I feel uneasy, so I decide to..."
        
        # A #
        "Hear what Kit has to say.":
            jump hear_what_kit_has_to_say
        # B #
        "Walk out of the room.":
            jump walk_out_of_the_room


label hear_what_kit_has_to_say:

    if wait_for_vida:

        jay "Ok, let's head back..."

        scene bg classroom 2 reverse
        show kit_model at rightside
        $ kit_pose = "armscrossed"
        show andrea_model normal at middle
        $ andrea_pose = "neutral"
        show vida_model normal at leftside
        $ vida_pose = "behindback"

        kit "You good Jay?"
        andrea "Yeah is everything alright?"
        jay "Yeah yeah I'm fine..."
        jay "Can we just continue from where we left off?"
        kit "Of course! Let me tell you all what I know!"
        kit "It's something that will definitely save our club!"
        nar "He leans in and smiles." 

    $ kit_pose = "armscrossed"
    show kit_model grin at rightside

    kit "I know where the human kebab murder happened..."

    $ vida_pose = "nervous"
    show vida_model lookright at leftside
    $ andrea_model = "nervous"
    show andrea_model lookright at middle

    nar "Kit whispers."
    nar "The rest of us in the club room can't even speak."
    vida "H-how?"

    show kit_model lookleft at rightside

    kit "I was hoping you would have asked where... To answer your question..."
    kit "I was watching the news about it when I noticed something in the alley that looked familiar." 

    show kit_model normal at rightside

    jay "What was it?" 
    kit "I saw a sign in the background that had a sticker on it."

    $ kit_pose = "gesture"

    nar "Kit reaches into his pocket and pulls out a sticker with a bird emblem on it."
    kit "This sticker." 
    nar "The three of us stand there shocked, before we can say anything Kit explains."
    kit "This is from the same pack of stickers I had as a kid. I used to take a shortcut to school through some alleyways and placed these stickers along the way in case I got lost."
    kit "So years ago I must have placed that sticker next to where the murder recently took place."

    $ kit_pose = "raisedarms"

    nar "He leans back in his chair and pumps both his hands in the air."
    kit "Which means! I know where it happened..."

    stop music
    hide kit_model
    hide andrea_model
    hide vida_model
    scene bg blank

    return ############################################################################################
    ###################################################################################################

    nar "The next day, all four of us are standing on the rooftop of a building during sunset."

    scene bg rooftop
    play  music "audio/Night_1.mp3" volume 0.5 fadeout 2.0 fadein 2.0

    jay "I can't believe you convinced me to do this..." 

    $ kit_pose = "armscrossed"
    show kit_model normal shut at middle

    kit "You don't want the club to be disbanded, do you?" 

    hide kit_model

    nar "Kit makes the jump from one rooftop to the next."
    jay "So what's the plan again?"

    $ andrea_pose = "armsonhips"
    show andrea_model at leftside
    
    andrea "Find murder site, find new info, write paper, profit." 
    nar "Andrea says as she is jumping in place in order to prepare herself for the jump. The jump itself is only around two feet but still feels massive when they are so high up." 
    
    $ vida_pose = "wave"
    show vida_model at rightside

    vida "How many of these jumps do we have to do?"
    nar "She says already on the other side of the gap."

    $ kit_pose = "raisedarms"
    show kit_model grin at middle

    kit "I don't know!"

    show kit_model grin at middle

    nar "Kit shouts cheerfully. This is not what I expected to be doing instead of today's assembly."
    jay "You sure we should be doing this, it's technically still school hours?"

    $ kit_pose = "shrug"
    show kit_model closed open at middle

    kit "Stop worrying, you didn't want to go to it anyways, and we have to strike the iron while it's hot." 

    menu:
        "I thought about it, standing on the roof across from my friends."
        # AA #
        "Take the Jump.":
            jump jump_along_rooftops 
        # AB #
        "Leave now.":
            jump walk_away_from_rooftops

label jump_along_rooftops:

    ###################################################
    return
    ####################################################



    vida "Just come on already, it will be fine!"
    nar "I took a set back, hesitated, and launched myself forward over the gap."

    hide andrea
    hide kit
    hide vida

    nar "The four of us walked across rooftops and jumped over a few more gaps of various sizes."
    nar "I noticed on my watch that we had been traveling for about fifteen minutes."
    jay "Hey, Kit. Are we almost there?"
    show kit smug at middle
    nar "Kit took a few more steps, turned around and smiled."
    kit "We're here."

    play  music "audio/Dark Atmosphere to Synth.wav" volume 0.5 fadeout 2.0 fadein 3.0

    nar "We stood at the edge of a rooftop with an alleyway down below behind us. Kit and Andrea crouched down and peered over the edge looking into the darkness below." 
    hide kit
    scene bg blank
    kit "Damn I can't see anything."
    nar "Suddenly they all heard footsteps down below." 
    jay "Quiet..."
    nar "I whispered as I examined the alleyway below."
    vida "That is why we're up here, I guess."
    nar "She whispered to Kit." 
    nar "We looked down below as two figures walked around the corner talking to each other. We couldn't make out what they were saying but they seemed to be the authorities as one man wore a police cap."
    scene bg alleyway 2
    nar "The two men held flashlights and scanned them over the alley; it featured garbage and debris, all of which was covered in dried blood."
    nar "It was definitely the murder site. From what he could see from the flashlights, he didn't know how they would have seen without them, in the alley there was no corpse so the victim must have already been removed."
    nar "Even without it the whole scene sent shivers down my spine."
    nar "Kit leaned his head sideways attempting to hear what the men were saying deep below them. To avoid the disgusting scene below me and my friends I looked towards his left at the crossroad of the alley, and there was the sign Kit had mentioned."
    nar "Supposedly it had a sticker on it, though it was so dark out he couldn't tell."
    andrea "I think I can still smell it from here..."
    nar "I sniffled subtly and almost threw up. It smelled so bad."
    nar "I couldn't help but look down into the alley in search of the source of the smell, refusing to believe such a smell could come from such a cause."
    nar "As I tried to focus on the scene down below me I started to feel more sick and slowly everything became blurry as I stumbled backward before tripping causing me to fall onto my back."
    scene bg blank
    vida "Jay... Jay!" 
    nar "Everyone huddled around me as I was passing out."
    scene bg sky
    nar "The men in the alley shined their flashlights up towards the rooftop to the sound of Jay falling over. This let me see... something... in the sky, illuminated by the flashlights, before my eyes fully closed."


    e "Not done yet."

    return

label walk_away_from_rooftops:

    e "Not done yet."


    # This ends the game.

    return

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

##
define wait_for_vida = False
##
label wait_for_vida:

    $ wait_for_vida = True

    nar "I stand still and turn to face Vida."

    $ vida_pose = "nervous"
    show vida_model at middle

    vida "Are you ok Jay?"
    vida "You walked out all of a sudden..."
    jay "Y-yeah... I'm alright, just needed a second to think."
    vida "Is it about the murder?"
    jay "Yes. I'm just a little concerned about covering it."

    $ vida_pose = "explaining"

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

label walk_out_of_school:


    ########################################################################################
    return
    #########################################################################################

    jay "I'm sorry vida... but I need some fresh air right now."
    vida "Ok then. Well I'll see you later, maybe tomorrow."
    vida "Bye for now... and stay safe."




    e "Not done yet."

    return 